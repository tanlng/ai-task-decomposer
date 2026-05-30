import argparse
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


SKILL_FILENAMES = ("SKILL.md", "skill.md")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
PROMOTED_KEYWORDS = (
    "use when",
    "when to use",
    "\u4f55\u65f6\u4f7f\u7528",
    "use this skill",
    "purpose",
    "\u9002\u7528",
)

try:
    import tiktoken  # type: ignore
except ImportError:
    tiktoken = None


@dataclass
class SectionNode:
    title: str
    level: int
    heading_line: str = ""
    body_lines: list[str] = field(default_factory=list)
    parent: "SectionNode | None" = None
    children: list["SectionNode"] = field(default_factory=list)

    def add_child(self, child: "SectionNode") -> None:
        child.parent = self
        self.children.append(child)

    @property
    def body_text(self) -> str:
        return "\n".join(self.body_lines).strip()

    @property
    def self_text(self) -> str:
        parts = []
        if self.heading_line:
            parts.append(self.heading_line)
        if self.body_text:
            parts.append(self.body_text)
        return "\n".join(parts).strip()

    def lineage(self) -> list["SectionNode"]:
        nodes: list[SectionNode] = []
        current: SectionNode | None = self
        while current is not None:
            nodes.append(current)
            current = current.parent
        return list(reversed(nodes))


@dataclass
class SkillMetrics:
    name: str
    path: str
    total_tokens: int
    default_tokens: int
    default_ratio: float
    branch_count: int
    max_branch_tokens: int
    avg_branch_tokens: float
    score: int
    warnings: list[str]
    branches: list[dict[str, Any]]
    meta: dict[str, Any]


def estimate_tokens(text: str) -> int:
    if not text.strip():
        return 0

    if tiktoken is not None:
        try:
            encoding = tiktoken.get_encoding("o200k_base")
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))

    cjk_units = len(re.findall(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", text))
    latin_words = len(re.findall(r"[A-Za-z0-9_./:`-]+", text))
    punctuation_units = len(re.findall(r"[^\w\s\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]", text))
    return max(1, cjk_units + math.ceil(latin_words * 1.3) + math.ceil(punctuation_units * 0.3))


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, "", text

    raw = match.group(1)
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, match.group(0).strip(), text[match.end() :]


def parse_sections(body: str) -> SectionNode:
    root = SectionNode(title="ROOT", level=0)
    stack = [root]

    for line in body.splitlines():
        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            node = SectionNode(title=title, level=level, heading_line=line.strip())

            while stack and stack[-1].level >= level:
                stack.pop()
            stack[-1].add_child(node)
            stack.append(node)
        else:
            stack[-1].body_lines.append(line)

    return root


def collect_leaves(node: SectionNode) -> list[SectionNode]:
    if not node.children:
        return [node]

    leaves: list[SectionNode] = []
    for child in node.children:
        leaves.extend(collect_leaves(child))
    return leaves


def shared_prefix_nodes(root: SectionNode) -> list[SectionNode]:
    shared = [root]
    current = root
    while len(current.children) == 1:
        current = current.children[0]
        shared.append(current)
    return shared


def branch_nodes(root: SectionNode) -> list[SectionNode]:
    leaves = [leaf for leaf in collect_leaves(root) if leaf is not root]
    return leaves


def build_branch_metrics(root: SectionNode, frontmatter_text: str) -> tuple[int, list[dict[str, Any]]]:
    leaves = branch_nodes(root)
    shared_nodes = shared_prefix_nodes(root)
    shared_node_set = {id(node) for node in shared_nodes}

    default_text_parts = []
    if frontmatter_text:
        default_text_parts.append(frontmatter_text)
    for node in shared_nodes:
        if node is root:
            if node.body_text:
                default_text_parts.append(node.body_text)
            continue
        if node.self_text:
            default_text_parts.append(node.self_text)
    default_tokens = estimate_tokens("\n\n".join(part for part in default_text_parts if part))

    branches: list[dict[str, Any]] = []
    for leaf in leaves:
        lineage = leaf.lineage()
        path_titles = [node.title for node in lineage if node is not root]
        path_text_parts = []
        branch_only_parts = []

        if frontmatter_text:
            path_text_parts.append(frontmatter_text)

        for node in lineage:
            if node is root:
                if node.body_text:
                    path_text_parts.append(node.body_text)
                continue
            if node.self_text:
                path_text_parts.append(node.self_text)
                if id(node) not in shared_node_set:
                    branch_only_parts.append(node.self_text)

        path_tokens = estimate_tokens("\n\n".join(path_text_parts))
        branch_only_tokens = estimate_tokens("\n\n".join(branch_only_parts))
        branches.append(
            {
                "path": " > ".join(path_titles) if path_titles else "(root)",
                "depth": len(path_titles),
                "path_tokens": path_tokens,
                "branch_only_tokens": branch_only_tokens,
            }
        )

    if not branches:
        path_text_parts = [frontmatter_text, root.body_text]
        only_path_tokens = estimate_tokens("\n\n".join(part for part in path_text_parts if part))
        branches.append(
            {
                "path": "(single)",
                "depth": 0,
                "path_tokens": only_path_tokens,
                "branch_only_tokens": max(0, only_path_tokens - default_tokens),
            }
        )

    branches.sort(key=lambda item: (-item["path_tokens"], item["path"]))
    return default_tokens, branches


def calc_score(
    total_tokens: int,
    default_tokens: int,
    branches: list[dict[str, Any]],
    meta: dict[str, str],
    body: str,
) -> tuple[int, list[str]]:
    warnings: list[str] = []
    score = 100

    default_ratio = (default_tokens / total_tokens) if total_tokens else 1.0
    max_branch_tokens = max(branch["path_tokens"] for branch in branches)

    if "name" not in meta:
        warnings.append("missing frontmatter name")
        score -= 12
    if "description" not in meta:
        warnings.append("missing frontmatter description")
        score -= 18

    description = meta.get("description", "")
    desc_token_count = estimate_tokens(description)
    if description and desc_token_count > 90:
        warnings.append("description is heavy for a trigger field")
        score -= 8
    if description and not any(keyword in description.lower() for keyword in PROMOTED_KEYWORDS):
        warnings.append("description may not clearly express trigger conditions")
        score -= 6

    if total_tokens > 1800:
        warnings.append("full skill load is expensive")
        score -= 14
    elif total_tokens > 1200:
        warnings.append("full skill load is moderately heavy")
        score -= 8

    if default_ratio > 0.75 and total_tokens > 400:
        warnings.append("most content sits in the default shared prefix")
        score -= 18
    elif default_ratio > 0.55 and total_tokens > 400:
        warnings.append("default shared prefix is larger than ideal")
        score -= 10

    if max_branch_tokens > 1200:
        warnings.append("heaviest branch path is expensive")
        score -= 12
    elif max_branch_tokens > 800:
        warnings.append("heaviest branch path is moderately heavy")
        score -= 7

    if len(branches) > 8:
        warnings.append("many branches may increase selection complexity")
        score -= 6

    if "references/" not in body and total_tokens > 900:
        warnings.append("long skill without explicit references split")
        score -= 8

    return max(0, score), warnings


def evaluate_skill(path: Path, root: Path) -> SkillMetrics:
    text = load_text(path)
    meta, frontmatter_text, body = parse_frontmatter(text)
    section_root = parse_sections(body)
    default_tokens, branches = build_branch_metrics(section_root, frontmatter_text)
    total_tokens = estimate_tokens(text)
    max_branch_tokens = max(branch["path_tokens"] for branch in branches)
    avg_branch_tokens = sum(branch["path_tokens"] for branch in branches) / len(branches)
    score, warnings = calc_score(total_tokens, default_tokens, branches, meta, body)

    return SkillMetrics(
        name=meta.get("name", path.parent.name),
        path=str(path.relative_to(root)),
        total_tokens=total_tokens,
        default_tokens=default_tokens,
        default_ratio=(default_tokens / total_tokens) if total_tokens else 1.0,
        branch_count=len(branches),
        max_branch_tokens=max_branch_tokens,
        avg_branch_tokens=avg_branch_tokens,
        score=score,
        warnings=warnings,
        branches=branches,
        meta=meta,
    )


def discover_skill_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for filename in SKILL_FILENAMES:
        files.extend(root.rglob(filename))
    return sorted(set(files))


def build_summary(skills: list[SkillMetrics]) -> dict[str, Any]:
    totals = [skill.total_tokens for skill in skills]
    defaults = [skill.default_tokens for skill in skills]
    return {
        "skill_count": len(skills),
        "avg_total_tokens": round(sum(totals) / len(totals), 1) if totals else 0,
        "avg_default_tokens": round(sum(defaults) / len(defaults), 1) if defaults else 0,
        "max_total_tokens": max(totals) if totals else 0,
        "max_default_tokens": max(defaults) if defaults else 0,
        "avg_score": round(sum(skill.score for skill in skills) / len(skills), 1) if skills else 0,
    }


def render_text(skills: list[SkillMetrics], summary: dict[str, Any], branch_limit: int) -> str:
    lines = []
    lines.append("Skill Evaluation Summary")
    lines.append("")
    lines.append(f"Skills: {summary['skill_count']}")
    lines.append(f"Avg total tokens: {summary['avg_total_tokens']}")
    lines.append(f"Avg default tokens: {summary['avg_default_tokens']}")
    lines.append(f"Avg score: {summary['avg_score']}")
    lines.append("")

    for skill in sorted(skills, key=lambda item: (item.score, -item.total_tokens, item.name)):
        lines.append(f"- {skill.name} [{skill.path}]")
        lines.append(
            f"  score={skill.score} total={skill.total_tokens} default={skill.default_tokens} "
            f"default_ratio={skill.default_ratio:.2f} branches={skill.branch_count} max_branch={skill.max_branch_tokens}"
        )
        if skill.warnings:
            lines.append(f"  warnings={'; '.join(skill.warnings)}")
        for branch in skill.branches[:branch_limit]:
            lines.append(
                f"  branch path={branch['path']} path_tokens={branch['path_tokens']} "
                f"branch_only={branch['branch_only_tokens']}"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_markdown(skills: list[SkillMetrics], summary: dict[str, Any], branch_limit: int) -> str:
    lines = []
    lines.append("# Skill Evaluation Summary")
    lines.append("")
    lines.append(f"- Skills: {summary['skill_count']}")
    lines.append(f"- Avg total tokens: {summary['avg_total_tokens']}")
    lines.append(f"- Avg default tokens: {summary['avg_default_tokens']}")
    lines.append(f"- Avg score: {summary['avg_score']}")
    lines.append("")

    for skill in sorted(skills, key=lambda item: (item.score, -item.total_tokens, item.name)):
        lines.append(f"## {skill.name}")
        lines.append("")
        lines.append(f"- Path: `{skill.path}`")
        lines.append(f"- Score: `{skill.score}`")
        lines.append(f"- Total tokens: `{skill.total_tokens}`")
        lines.append(f"- Default tokens: `{skill.default_tokens}`")
        lines.append(f"- Default ratio: `{skill.default_ratio:.2f}`")
        lines.append(f"- Branches: `{skill.branch_count}`")
        lines.append(f"- Max branch path tokens: `{skill.max_branch_tokens}`")
        if skill.warnings:
            lines.append(f"- Warnings: `{' ; '.join(skill.warnings)}`")
        lines.append("")
        lines.append("| Branch path | Path tokens | Branch-only tokens |")
        lines.append("| --- | ---: | ---: |")
        for branch in skill.branches[:branch_limit]:
            lines.append(
                f"| `{branch['path']}` | {branch['path_tokens']} | {branch['branch_only_tokens']} |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_json(skills: list[SkillMetrics], summary: dict[str, Any]) -> str:
    payload = {
        "summary": summary,
        "skills": [
            {
                "name": skill.name,
                "path": skill.path,
                "score": skill.score,
                "total_tokens": skill.total_tokens,
                "default_tokens": skill.default_tokens,
                "default_ratio": round(skill.default_ratio, 4),
                "branch_count": skill.branch_count,
                "max_branch_tokens": skill.max_branch_tokens,
                "avg_branch_tokens": round(skill.avg_branch_tokens, 2),
                "warnings": skill.warnings,
                "branches": skill.branches,
                "meta": skill.meta,
            }
            for skill in skills
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate skill files for context footprint, branching cost, and basic structure quality."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan. Default: current directory.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "markdown", "json"),
        default="text",
        help="Output format. Default: text.",
    )
    parser.add_argument(
        "--branch-limit",
        type=int,
        default=5,
        help="Max branches to show per skill in text/markdown output. Default: 5.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    skill_files = discover_skill_files(root)
    skills = [evaluate_skill(path, root) for path in skill_files]
    summary = build_summary(skills)

    if args.format == "json":
        output = render_json(skills, summary)
    elif args.format == "markdown":
        output = render_markdown(skills, summary, args.branch_limit)
    else:
        output = render_text(skills, summary, args.branch_limit)

    print(output, end="")


if __name__ == "__main__":
    main()
