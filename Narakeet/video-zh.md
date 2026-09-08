---
size: 1080p
transition: crossfade 0.2
background: corporate-1 fade-in fade-out
theme: light
subtitles: embed
voice: Dawei
---

(pause: 1)

![](0_Sonar_Background.jpg)

(font-size: 30)

```
 <Gitar demo>
 Gitar 如何修复漏洞并通过 SonarQube 进行验证
```

在本演示中,我将展示Gitar如何检测并解决拉取请求(pull request)中的问题,随后SonarQube会重新分析该PR,以确保没有引入新的问题。

---

(pause: 1)

![](01_GH_OpenPR.mp4)
首先,让我们在GitHub上从一个功能分支向main分支发起一个新的拉取请求。

---

(pause: 1)

![](02_Gitar_analysis.mp4)
PR创建后,SonarQube和Gitar会自动开始各自的分析。

---

(pause: 1)

![](03_Gitar_review_done.mp4)
不久之后,Gitar完成分析,并在该PR中发现了两个问题。

---

(pause: 1)

![](04_Gitar_apply_fix.mp4)
Gitar的每条评论上都有一个"Apply fix"复选框,可以让你选择是否通过Gitar来修复该问题。
在本演示中,我将请Gitar来修复它。

---

(pause: 1)

![](05_Gitar_fix_done.mp4)

Gitar解决了该问题,并自动将修复提交推送到这个开放的PR中。

---

(pause: 1)

![](06_SQ_QG_Pass.mp4)

最后,SonarQube重新分析该PR,以验证修复效果,并确认没有引入新的问题。

这个工作流展示了Gitar和SonarQube如何无缝协作,检查代码、应用自动修复,并维护整体代码库质量。通过自动化修复流程,工程师只需审查建议的更改即可,从而大幅缩短问题解决时间。

我们的演示到此结束。感谢观看,期待下次与您相见!
