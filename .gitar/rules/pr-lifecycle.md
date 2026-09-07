# Pull-request lifecycle

- When a review finds an issue of severity Critical or Important, submit a
  blocking review and keep the pull request blocked until it is resolved.
- Apply a fix as a **new commit** on the pull-request branch. Never force-push
  and never rewrite the author's commits — the demo depends on the original
  commit staying visible in the PR history.
- After a fix is pushed, wait for CI and the SonarQube Quality Gate to complete
  on the new commit before re-evaluating the verdict.
- When all findings are resolved and every required check is green, approve the
  pull request.

> Note: the authoritative merge-blocking severity threshold is an **organisation
> setting** in the Gitar dashboard, not a repository file. This file states the
> intent for reviewers; see `docs/DEMO_RUNBOOK.md` for the setting to flip.
