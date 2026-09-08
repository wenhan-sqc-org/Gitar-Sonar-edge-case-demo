---
size: 1080p
transition: crossfade 0.2
background: corporate-1 0.3 fade-in fade-out
theme: light
subtitles: embed
---

(pause: 1)

![](0_Sonar_Background.jpg)

(font-size: 30)

```
 <Gitar demo>
 How Gitar Fixes Bugs and Validates with SonarQube
```

In this demo, I will demonstrate how Gitar detects and resolves an issue within a pull request, followed by SonarQube re-analyzing the PR to ensure no new issues are introduced.

---

(pause: 1)

![](01_GH_OpenPR.mp4)
To begin, let's open a new pull request on GitHub from a feature branch into main.

---

(pause: 1)

![](02_Gitar_analysis.mp4)
Once the PR is created, both SonarQube and Gitar automatically initiate their analysis.

---

(pause: 1)

![](03_Gitar_review_done.mp4)
Shortly after, Gitar completes its analysis and identifies two issues within this PR.

---

(pause: 1)

![](04_Gitar_apply_fix.mp4)
There is a "Apply fix" checkbox on each comment from Gitar. It lets you choose whether you want to fix it via Gitar.
In this demo, I'm going to ask Gitar to fix it.

---

(pause: 1)

![](05_Gitar_fix_done.mp4)

Gitar resolves the issue and automatically pushes the commit to the open PR.

---

(pause: 1)

![](06_SQ_QG_Pass.mp4)

Finally, SonarQube re-analyzes the PR to verify the fix and confirm that no new issues have been introduced.

This workflow demonstrates how Gitar and SonarQube seamlessly collaborate to inspect code, apply automated fixes, and maintain overall codebase quality. By automating remediation, engineers only need to review the proposed changes, significantly reducing resolution time.

This concludes our demonstration. Thank you for watching, and I look forward to seeing you next time!
