---
name: structured-debugging
description: Structured root-cause analysis and observability-driven debugging workflow.
---

# Structured Debugging

## Goal

Systematically converge toward the real root cause.

Focus:
- investigation discipline
- instrumentation
- elimination chain
- measurable validation

---

# Rules

## One Variable At A Time

Never validate multiple major hypotheses simultaneously.

---

## Required Phase Structure

Every debugging phase must contain:

1. Hypothesis
2. Validation Method
3. Result
4. Conclusion

---

# Elimination Chain

Maintain:

Eliminated Causes

Record:
- why it was suspected
- what disproved it
- which metrics/logs eliminated it

---

# Instrumentation

Instrumentation is a long-term engineering asset.

Categories:
- Temporary
- Warn-only
- Metrics
- Diagnostic Trace
- Long-term Monitoring

Avoid:
- spam logging
- non-actionable logs

---

# Metrics Requirements

Validation should include:
- before/after comparison
- delta
- reproducibility
- time window
- frequency

---

# Output

Produce:

root-cause-report.md

Including:
- symptom
- affected systems
- investigation phases
- hypotheses
- eliminated causes
- confirmed root cause
- instrumentation added
- supporting metrics
