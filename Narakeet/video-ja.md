---
size: 1080p
transition: crossfade 0.2
background: corporate-1 0.3 fade-in fade-out
theme: light
subtitles: embed
voice: Yuriko
---

(pause: 1)

![](0_Sonar_Background.jpg)

(font-size: 30)

```
 <Gitar demo>
 GitarによるバグFixとSonarQubeによる検証の方法
```

このデモでは、Gitarがプルリクエスト内の問題を検出して解決し、その後SonarQubeがPRを再解析して新たな問題が発生していないことを確認する流れをご紹介します。

---

(pause: 1)

![](01_GH_OpenPR.mp4)
まずは、フィーチャーブランチからmainブランチへ、GitHub上で新しいプルリクエストを作成します。

---

(pause: 1)

![](02_Gitar_analysis.mp4)
PRが作成されると、SonarQubeとGitarの両方が自動的に解析を開始します。

---

(pause: 1)

![](03_Gitar_review_done.mp4)
しばらくすると、Gitarが解析を完了し、このPR内で2件の問題を検出します。

---

(pause: 1)

![](04_Gitar_apply_fix.mp4)
Gitarからの各コメントには「Apply fix」というチェックボックスがあり、Gitarによる修正を適用するかどうかを選択できます。
今回のデモでは、Gitarに修正を依頼します。

---

(pause: 1)

![](05_Gitar_fix_done.mp4)

Gitarが問題を解決し、修正内容のコミットを自動的にオープン中のPRへプッシュします。

---

(pause: 1)

![](06_SQ_QG_Pass.mp4)

最後に、SonarQubeがPRを再解析し、修正内容を検証するとともに、新たな問題が発生していないことを確認します。

このワークフローは、GitarとSonarQubeがシームレスに連携してコードを検査し、自動修正を適用しながらコードベース全体の品質を維持する様子を示しています。修正作業を自動化することで、エンジニアは提案された変更内容を確認するだけで済み、解決までの時間を大幅に短縮できます。

以上でデモは終了です。ご視聴ありがとうございました。また次回お会いしましょう!
