# Demo runbook

Operational setup and the click-by-click script. What the demo proves, and the
planted defect itself, are in [`SCENARIO.md`](SCENARIO.md).

---

## 1. One-time setup

### 1.1 SonarQube Cloud

1. In your SonarQube Cloud organisation `wenhan-sqc-org`, create/import the
   project so its key is exactly:

   ```
   wenhan-sqc-org_Gitar-Sonar-edge-case-demo
   ```

   If your key differs, update `sonar.projectKey` in `sonar-project.properties`.
2. Turn **off** Automatic Analysis for the project
   (*Administration → Analysis Method*). CI-based analysis and Automatic
   Analysis are mutually exclusive, and this demo needs the CI path.
3. Make sure the **SonarQube Cloud GitHub App** is installed on the repository
   so PR decoration works.
4. Generate a token and add it to the GitHub repo as secret **`SONAR_TOKEN`**
   (*Settings → Secrets and variables → Actions*).

> `SONAR_HOST_URL` is **not** required for SonarQube Cloud and is intentionally
> absent from the workflow.

### 1.2 New Code definition

Leave the project on the default **Previous version** / reference-branch
definition. For pull requests "new code" is the PR diff regardless, which is
what both the blind-spot claim and step 4 depend on.

### 1.3 Quality Gate

The default **Sonar way** gate works as-is. Its conditions on new code:

| Condition | Commit 1 | After Gitar's fix |
|---|---|---|
| Issues = 0 | ✅ no rule fires | ✅ |
| Security Hotspots Reviewed = 100% | ✅ none raised | ✅ |
| Duplicated Lines ≤ 3% | ✅ | ✅ |
| Coverage ≥ 80% | ✅ 100% | ✅ **if the fix ships a test** |

> **The one thing to watch.** Gitar's fix adds ~2 lines (`if not orders:` /
> `return 0.0`). If it lands *without* a regression test, those are uncovered
> new lines, which can push Coverage on New Code below 80% and turn the gate
> red — inverting step 4. This is why `.gitar/review/gotchas.md` rule 4
> requires a regression test with every behaviour fix. If a run ever produces a
> bare fix, either reply in the PR asking Gitar to add a regression test for the
> empty case, or use a demo-specific gate with the Coverage condition removed.

### 1.4 Gitar

1. Install the Gitar GitHub App on this repository.
2. In the Gitar dashboard **organisation settings**, set the merge-blocking
   severity threshold to **Important** (or **Critical**) so the review verdict
   submits a blocking review. This is an org-level setting and cannot be
   committed to the repo.
3. Optional, for a hands-off run: enable auto-apply so Gitar commits the fix
   unprompted. Leave it **off** if you want to demo the `gitar fix` reply live
   — it is the more convincing beat.

`.gitar/review/gotchas.md` and `.gitar/rules/pr-lifecycle.md` are picked up from
the branch automatically; they need no dashboard configuration.

### 1.5 Branch protection — this is what makes "mergeable" real

*Settings → Branches → Add rule* for `main`:

- ✅ Require status checks to pass before merging
- Add **`Test + SonarQube analysis`** (the workflow job — it fails when the gate
  is red) and the **SonarQube Cloud** check
- ✅ Require a pull request before merging, with 1 approval — so Gitar's
  blocking review genuinely holds the merge

---

## 2. Running the demo

```bash
git push -u origin main
git push -u origin feat/average-order-value
gh pr create --base main --head feat/average-order-value --fill
```

Then narrate:

1. **Checks go green.** CI passes, SonarQube Cloud reports **Quality Gate
   passed** — 0 new issues, 100% coverage on new code. Open the Sonar PR page
   and show there is nothing there. *"By every rule-based measure, this PR is
   clean."*
2. **Gitar disagrees.** `gitar-bot` posts an inline finding on the division
   line, explaining that the docstring promises `0.0` for empty input while the
   code raises `ZeroDivisionError`, and submits a blocking review. The PR is
   **not mergeable** — despite a green gate.
3. **Fix on the same PR.** Reply `gitar fix` to the finding (or let auto-apply
   run). Gitar pushes a **new commit** — no force-push, commit 1 stays visible
   in the history. Show the guard clause and the added regression test.
4. **Sonar re-analyses.** The new commit re-triggers the workflow: tests pass,
   PR analysis re-runs, **Quality Gate passes**, coverage on new code stays at
   100%. Gitar's blocking review resolves to an approval and **Merge** turns
   green.

Closing line: *SonarQube proves the fix introduced no new problems; Gitar found
the problem the rules could not see.*

---

## 3. Blind run

`docs/` is the only place in the repository that describes the scenario or names
the defect. For a run where a skeptical audience can verify Gitar was given no
hints:

```bash
git switch feat/average-order-value
git rm -r --quiet docs/
git commit -qm "Remove demo documentation"
```

What remains is an ordinary Python repository: a library with a documented
house rule, a test suite, a Sonar pipeline, and `.gitar/review/gotchas.md` —
generic engineering standards of the kind any real codebase carries, which never
name the affected function. Gitar has to find the defect from the code alone.

Keep `.gitar/` in place. Removing it does not make the demo more honest, it just
makes the finding less reliable — committed review conventions are a documented,
intended Gitar feature.

---

## 4. Verifying the blind spot yourself

Before demoing, confirm Sonar really is silent on commit 1:

```bash
sonar list-issues -p wenhan-sqc-org_Gitar-Sonar-edge-case-demo --pull-request <PR#>
sonar quality-gate -p wenhan-sqc-org_Gitar-Sonar-edge-case-demo
```

Expect zero issues and a passing gate. And confirm the defect is real:

```bash
python -c "from orderstats.stats import average_order_value; average_order_value([])"
# ZeroDivisionError: division by zero
```

---

## 5. Resetting between demos

Capture the PR commit once, so you can always recreate it:

```bash
git format-patch main..feat/average-order-value -o .demo-patches/
```

Then reset:

```bash
gh pr close <PR#> --delete-branch
git branch -D feat/average-order-value
git switch -c feat/average-order-value main
git am .demo-patches/0001-*.patch
```

---

## 6. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| No SonarQube check on the PR | GitHub App not installed, or Automatic Analysis still enabled — disable it. |
| `Project not found` | `sonar.projectKey` / `sonar.organization` do not match the Cloud project. |
| Coverage 0% on new code | `coverage.xml` missing, or its paths are not repo-relative. Keep `include = ["orderstats/*"]` in `pyproject.toml` (**not** `source =`) and run `coverage` from the repo root. |
| Quality Gate step times out | The gate task had not finished. Raise `timeout-minutes` on the gate step. |
| Gitar does not comment | App not installed on the repo, or the PR carries the `gitar-skip` label. |
| Gitar comments but does not block | Merge-blocking threshold not set in Gitar **org settings** (see 1.4), or branch protection has no approval requirement. |
| Gate goes red after the fix | The fix landed without a test — see the warning in 1.3. |
