---
size: 1080p
transition: crossfade 0.2
background: corporate-1 fade-in fade-out
theme: light
subtitles: embed
voice: Min-ho
---

(pause: 1)

![](0_Sonar_Background.jpg)

(font-size: 30)

```
 <Gitar demo>
 Gitar가 버그를 수정하고 SonarQube로 검증하는 방법
```

이번 데모에서는 Gitar가 풀 리퀘스트 내의 이슈를 감지하고 해결한 후, SonarQube가 해당 PR을 다시 분석하여 새로운 이슈가 발생하지 않았는지 확인하는 과정을 보여드리겠습니다.

---

(pause: 1)

![](01_GH_OpenPR.mp4)
먼저, 기능 브랜치에서 main 브랜치로 GitHub에서 새로운 풀 리퀘스트를 열어보겠습니다.

---

(pause: 1)

![](02_Gitar_analysis.mp4)
PR이 생성되면 SonarQube와 Gitar가 자동으로 분석을 시작합니다.

---

(pause: 1)

![](03_Gitar_review_done.mp4)
잠시 후 Gitar가 분석을 완료하고 이 PR에서 두 가지 이슈를 발견합니다.

---

(pause: 1)

![](04_Gitar_apply_fix.mp4)
Gitar의 각 댓글에는 "Apply fix" 체크박스가 있어, Gitar를 통해 수정할지 여부를 선택할 수 있습니다.
이번 데모에서는 Gitar에게 수정을 요청하겠습니다.

---

(pause: 1)

![](05_Gitar_fix_done.mp4)

Gitar가 이슈를 해결하고 수정 커밋을 열려 있는 PR에 자동으로 푸시합니다.

---

(pause: 1)

![](06_SQ_QG_Pass.mp4)

마지막으로 SonarQube가 PR을 다시 분석하여 수정 사항을 검증하고 새로운 이슈가 발생하지 않았는지 확인합니다.

이 워크플로우는 Gitar와 SonarQube가 원활하게 협력하여 코드를 검사하고, 자동 수정을 적용하며, 전체 코드베이스 품질을 유지하는 방법을 보여줍니다. 수정 작업을 자동화함으로써 엔지니어는 제안된 변경 사항만 검토하면 되므로 해결 시간이 크게 단축됩니다.

이것으로 데모를 마치겠습니다. 시청해 주셔서 감사하며, 다음에 또 뵙겠습니다!
