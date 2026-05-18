# DropHawk · 品牌与 VI 规范

> 本文件定义项目对外的视觉/语言身份。所有界面、文档、推送卡片、对外材料必须遵循此规范。

---

## 1. 名称

| 场合 | 写法 |
| --- | --- |
| 正式英文 | **DropHawk**(一个词,首字母大写,中间无空格无连字符) |
| 简写 | **DH**(仅限内部代码 / 容器名 / log prefix) |
| 中文别名 | **鹰隼**(可选,仅在中文语境且不影响识别时使用) |
| 域名 | `drophawk.flaios.com` |
| 仓库 / 镜像 | `drophawk`(全小写) |

**禁用写法**:Drop Hawk · drop-hawk · DROPHAWK · 抓鸟 · 鹰盯 · DropHawks(复数)

---

## 2. Slogan

| 语言 | 文案 |
| --- | --- |
| 英文(主) | **See the drop. Strike first.** |
| 中文(主) | **盯准释放,先人一步。** |
| 短版 | *Strike first.* / **先人一步。** |

Slogan 出现规则:
- 落地页 Hero 区、推送卡片底部 footer 可用;
- **不要**在内部 PR、commit message、log 里使用 Slogan(留给对外场景)。

---

## 3. 命名来源

- **Drop**:域名行业术语 —— 过期未续费的域名从注册局释放回公有池,这个动作叫 *drop*,对应的清单叫 *drop list*。直接采用行业黑话,圈内人一看就懂。
- **Hawk**:鹰。盯守、俯冲、果断的捕食姿态,精准对应"长期监控 + 发现即出击"的产品行为。
- 组合后单词独特、易拼、易读、`.com` 同名虽已被注册,但用 `flaios.com` 子域不冲突。

---

## 4. 色彩

| 角色 | 名称 | HEX | RGB | 用途 |
| --- | --- | --- | --- | --- |
| 主色 | Night Indigo | `#0E1A2B` | 14,26,43 | 背景、文字主色、Logo 暗部 |
| 强调色 | Hunter Gold | `#E8A93C` | 232,169,60 | CTA 按钮、高分高亮、Logo 亮部 |
| 成功 | Pine | `#3F8F6B` | 63,143,107 | "可注册"状态 |
| 警示 | Ember | `#C8553D` | 200,85,61 | 错误、限流告警 |
| 中性 1 | Bone White | `#F5F2EC` | 245,242,236 | 浅色背景、卡片底 |
| 中性 2 | Slate | `#5A6878` | 90,104,120 | 副文本、分隔线 |

**搭配规则**
- 主色 + 强调色比例约 `9 : 1`,Hunter Gold 只用在"需要被发现"的元素上(CTA / 高分标签 / Logo 亮部),不用作大面积底色。
- 文字对比度遵循 WCAG AA:深色背景上的正文用 `#F5F2EC`,浅色背景上用 `#0E1A2B`。

---

## 5. Logo

### 5.1 概念
鹰头剪影向下俯冲,头部最低点延伸为一滴水滴,水滴轮廓与 "D" 字母同构。整体在 1:1 方形内可读,在 64×64 px 仍能识别鹰的姿态。

### 5.2 版本
- **Mark**:仅图形,用于 favicon、容器图标、社媒头像。
- **Wordmark**:文字 "DropHawk",用于纯文字场合。
- **Lockup**:Mark + Wordmark 横排,用于落地页 Header、推送卡片 Header。

### 5.3 使用规则
- Logo 周围保留**至少等于 Mark 高度 1/4** 的安全空白。
- 不允许:拉伸变形、改色(只用品牌色)、加阴影 / 描边 / 渐变(单色平面)、旋转、置于花哨背景上。
- 最小尺寸:Mark 16 px、Lockup 横向不小于 96 px。

### 5.4 资产位置
> M1 阶段补齐。届时放置于 `app/web/static/brand/`,文件命名:
> - `logo-mark.svg` / `logo-mark-light.svg` / `logo-mark-dark.svg`
> - `logo-wordmark.svg`
> - `logo-lockup.svg`
> - `favicon.ico` / `favicon-32.png` / `apple-touch-icon.png`

---

## 6. 字体

| 用途 | 字体 | 回退 |
| --- | --- | --- |
| 标题 / Logo | Inter Display(SemiBold / Bold) | system-ui, sans-serif |
| 正文(英文) | Inter(Regular / Medium) | system-ui, sans-serif |
| 正文(中文) | Source Han Sans CN(思源黑体)Regular / Medium | "PingFang SC", "Microsoft YaHei", sans-serif |
| 代码 / 域名 | JetBrains Mono | ui-monospace, Menlo, Consolas |

**域名一律用等宽字体**,避免 `rn` 与 `m`、`l` 与 `1` 的视觉混淆。

---

## 7. 语气(Tone of Voice)

- **简短、克制、内行**。像一个老猎手在用对讲机汇报,不像营销稿。
- 推送卡片:陈述事实 + 数据,不要感叹号堆叠。
- 错误/告警:说**发生了什么 + 下一步该做什么**,不卖惨。
- 禁用词:"震撼""王炸""速来""错过悔一辈子"等情绪化营销词。

### 示例
> ✅ "释放:`getagent.com` · 92 分 · .com · 5 字符 · 命中 AI 词根"
> ❌ "🔥🔥重大发现!!!绝佳域名 getagent.com 火速抢注!!!"

---

## 8. 推送卡片视觉

飞书机器人卡片配色:
- 标题栏:Night Indigo 底 + Hunter Gold 文字
- 主体:浅色卡片,Slate 副文本
- 按钮:Hunter Gold 主按钮 + Slate 次按钮
- 得分徽章:≥80 用 Hunter Gold,60–79 用 Slate,<60 一般不推送

---

## 9. 修订

| 版本 | 日期 | 变更 |
| --- | --- | --- |
| v0.1 | 2026-05-15 | 初稿:命名、Slogan、色彩、Logo 概念、字体、语气 |
