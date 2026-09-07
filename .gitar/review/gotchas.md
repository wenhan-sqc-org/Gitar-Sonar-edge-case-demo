# Review gotchas — orderstats

These are the house rules for this repository. They are deliberately written as
general expectations, not as pointers to any specific line of code.

## 1. A docstring `Returns:` clause is the contract

Every public function in `orderstats/` documents its result in a `Returns:`
clause. Treat that clause as the specification. If the implementation cannot
produce the documented result for some input the caller is allowed to pass,
that is a **bug in the implementation** — not a stale docstring. Report it and
correct the code so it satisfies the documented contract.

## 2. Empty collections are always a legal input

Every aggregation helper in this module accepts an empty sequence. The
convention is to return the neutral value for the aggregation:

- it must **not** raise,
- it must **not** return `None`,
- it must **not** return a sentinel such as `-1`.

`total_order_value` is the reference implementation of this convention. Any
helper that aggregates over orders and cannot survive an empty sequence is
inconsistent with the rest of the module.

## 3. Look for inputs the tests do not exercise

When a change adds a function, check which of its documented input classes have
no corresponding test. An untested boundary that the docstring explicitly
promises to support is a finding, even when every shipped test passes.

## 4. Behaviour fixes ship with a regression test

Any fix that changes runtime behaviour must add or extend a test under `tests/`
that fails before the fix and passes after it. This keeps coverage on new code
at 100% and stops the same regression coming back.

## 5. Keep fixes minimal and local

Prefer a guard clause at the top of the affected function over restructuring
it. Do not reformat surrounding code, rename anything, or add dependencies as
part of a fix.
