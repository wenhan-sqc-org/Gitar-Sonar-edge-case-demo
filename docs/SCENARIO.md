# Scenario — what this demo proves

> **Spoiler file.** This document names the planted defect. For a
> credibility-proof run where nothing in the repository hints at the answer,
> see [§ Blind run](DEMO_RUNBOOK.md#3-blind-run) in the runbook.

## The workflow being demonstrated

1. A pull request contains **one** edge case that SonarQube's rules cannot detect.
2. **Gitar** reviews the PR, finds it, and pushes a **fix as a follow-up commit** on the same branch.
3. That commit triggers **SonarQube Cloud PR analysis** again.
4. The **Quality Gate** check passes and the PR becomes mergeable.

## The planted issue

The pull request adds `average_order_value` to `orderstats/stats.py`. It
documents the module's empty-sequence convention and then fails to implement
it:

```python
def average_order_value(orders: Sequence[Order]) -> float:
    """...
    Returns:
        The mean order value, or ``0.0`` when ``orders`` is empty.
    """
    return total_order_value(orders) / len(orders)   # ZeroDivisionError when empty
```

The docstring promises `0.0`. The code raises `ZeroDivisionError`. That is the
entire issue — one line, one function, no side effects, no interaction with
anything else in the repository.

Confirm it is real:

```bash
python -c "from orderstats.stats import average_order_value; average_order_value([])"
# ZeroDivisionError: division by zero
```

The PR ships a happy-path test only (`test_average_order_value_returns_the_mean`).
The empty-input case the docstring explicitly promises to support is untested.

## Why SonarQube does not flag it

This is the point of the demo, so it is worth being precise. Nothing here is a
defect in SonarQube — it is the category boundary between rule-based static
analysis and reasoning about intent.

| Candidate detection | Why it does not fire |
|---|---|
| `python:S3518` — *Zero should not be a possible divisor* | Fires when the divisor can be **proven** zero by local dataflow (a literal `0`, or a variable assigned a constant `0`). Here the divisor is `len(orders)`, an opaque call on a caller-supplied argument, so it is never proven zero. |
| Contract / docstring rules | No analyzer rule cross-checks a `Returns:` clause against what the function actually does. The mismatch is only visible if you read the docstring **as a specification**. |
| Coverage on New Code | The happy-path test executes **both** new lines, so coverage on new code is 100% and the condition passes. |
| Duplication, complexity, hotspots | A two-line function: no duplication, trivial complexity, no security-sensitive API. |

Net effect on the first commit: **CI green, Quality Gate green.** Without
Gitar, this ships and crashes the first time a caller averages an empty result
set.

## Why Gitar does flag it

Gitar reviews for "security, bugs, performance, **edge cases**, and code
quality" and commits fixes back to the branch. Three properties of this example
make the finding reliable and the fix safe:

- **The intended behaviour is written down.** The docstring states `0.0` for
  empty input, so the correct fix is unambiguous — no guessing between `0.0`,
  `None`, and `raise ValueError`.
- **A reference implementation exists.** `total_order_value` already handles the
  empty case and its test asserts it, establishing the module convention.
- **The house rules are committed.** `.gitar/review/gotchas.md` states that a
  `Returns:` clause is a contract, that empty collections are always legal
  input, and that a behaviour fix must ship with a regression test.

`.gitar/review/gotchas.md` is written as general repository guidance — the kind
any real codebase would carry — and never names the affected function. Gitar
still has to find it.

## Expected end state

| | Commit 1 (author) | Commit 2 (`gitar-bot` fix) |
|---|---|---|
| CI build + tests | ✅ | ✅ |
| SonarQube Quality Gate | ✅ *(blind spot)* | ✅ *(re-analysed)* |
| Gitar review | ❌ blocking review | ✅ clean |
| Mergeable | **No** — held by Gitar | **Yes** |

The closing point: **SonarQube proves the fix introduced no new problems;
Gitar found the problem the rules could not see.** The gate is the safety net,
not the detector.
