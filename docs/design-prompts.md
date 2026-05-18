# DropHawk · GPT-Image-2 设计提示词

用于让 gpt-image-2 / Midjourney / nano-banana 之类的模型出**参考图**(不是终稿)。每条提示词已自带风格基底,**复制即用**。

---

## 输出路径约定

模型生成的图保存到本仓库:

```
docs/design/refs/
  01-logo-mark.png
  02-logo-lockup.png
  03-website-hero.png
  04-dashboard.png
  05-feishu-card.png
  06-brand-board.png
  07-favicon-set.png
  08-hawk-illustration.png
```

(`docs/design/refs/` 拿到第一张图时手动建一下即可。)

---

## 1. Logo Mark(方形,1:1)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B (primary background, depth), Hunter Gold #E8A93C (single accent, highlights only), Bone White #F5F2EC (light surface), Slate #5A6878 (secondary text, dividers). Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk watching the sky — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Design a square logo mark for a brand called "DropHawk". The mark is a single flat vector silhouette: a hawk diving downward, its head and beak forming the top, and its lowest point morphing seamlessly into a water-droplet shape that doubles as the letter "D". Two-color only: Night Indigo #0E1A2B silhouette on Bone White #F5F2EC background, with a single Hunter Gold #E8A93C highlight on the hawk's eye or beak tip. Geometric, confident, readable at 32px. No text. No outline. No gradient. No shadow. Centered. Generous padding. Aspect ratio 1:1.
```

---

## 2. Logo Lockup(横向,16:5)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Horizontal lockup of the DropHawk brand: the hawk-drop mark on the left, followed by the wordmark "DropHawk" in Inter Display SemiBold. Mark and wordmark share the same baseline-aligned visual weight. Below the wordmark, in JetBrains Mono small caps Slate #5A6878 color, the tagline: "SEE THE DROP. STRIKE FIRST." Background: Bone White #F5F2EC. Mark and wordmark in Night Indigo #0E1A2B. Tiny Hunter Gold #E8A93C accent on the mark's eye. Clean, minimal, lots of breathing room. Aspect ratio 16:5.
```

---

## 3. Website Hero(landing page,16:9)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Design a landing-page hero mockup for drophawk.flaios.com. Full-bleed Night Indigo #0E1A2B background with a faint topographic-line texture suggesting wind currents at altitude. Top-left: small DropHawk lockup. Top-right: minimal nav links "Product · Docs · Sign in" in Slate #5A6878. Center-left, large Inter Display headline in Bone White #F5F2EC: "See the drop. / Strike first." Below in Slate body text, two lines: "DropHawk watches every .com and .net release. / The good ones reach your Feishu before anyone else notices." Primary CTA button in Hunter Gold #E8A93C with Night Indigo text: "Request access". Center-right: a single hawk silhouette diving, small, Hunter Gold rim light, with a stylized terminal/log panel beside it showing a few monospace lines of domain hits (e.g. `getagent.com  92  .com  5ch  ai-root`). No stock photos. No people. No 3D. Flat, editorial, calm. Aspect ratio 16:9.
```

---

## 4. Web 控制台(Dashboard Mockup,16:10)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Design a single-page dashboard mockup for an internal tool called DropHawk. Layout: thin left sidebar with monochrome icons + labels (Dashboard, Candidates, Dictionary, Watchlist, Rules, Logs, Settings); main area on Bone White #F5F2EC with three KPI cards at top (Today's pushes / Week hits / Source health), then a wide data table titled "Recent candidates" with columns: Domain (JetBrains Mono), TLD, Length, Score (badge: Hunter Gold #E8A93C if >=80, Slate #5A6878 if 60-79), Source, Found at, Status. Row hover state subtle. Top-right shows a small DropHawk lockup and a Hunter Gold #E8A93C dot indicating "agent running". Overall: dense but legible, Linear-app energy, no rounded cartoon shapes, 8px grid, tasteful use of Hunter Gold only on score badges and the running indicator. Aspect ratio 16:10.
```

---

## 5. 飞书推送卡片(vertical,3:4)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Mockup of a Feishu (Lark) bot message card for DropHawk. Vertical card on Bone White #F5F2EC, rendered inside a faint Feishu chat window chrome (just enough to feel like a real message). Card header strip in Night Indigo #0E1A2B with "DropHawk" wordmark and a tiny mark on the left, right side a small Hunter Gold #E8A93C score pill "92". Card body in three short rows of Inter / JetBrains Mono: Title "Domain release detected"; Domain "getagent.com" (monospace, large, Night Indigo); Meta ".com · 8 chars · ai-root · pure-letters · drop-list 2026-05-15"; Reason "matched AI-root dictionary + letters-only + .com bonus". Three buttons in a row at the bottom: [Aliyun lookup] [Namecheap] [Dynadot]. Primary button Hunter Gold #E8A93C, others Slate #5A6878 outlined. Footer in tiny Slate text: "See the drop. Strike first." Aspect ratio 3:4.
```

---

## 6. Brand Board(4:3 一张图汇总)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Single brand-board reference image for DropHawk, arranged as a tidy poster on Bone White #F5F2EC. Four panels: (top-left) the logo mark large, with size-down variants showing it still reads at 16px; (top-right) color swatches in a 1x4 row labeled Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878, with their RGB values in JetBrains Mono below; (bottom-left) typography sample: "DropHawk" in Inter Display Bold, followed by "See the drop. Strike first." in Inter Medium, followed by a monospace domain "getagent.com" in JetBrains Mono; (bottom-right) "Do / Don't" pair showing the correct logo on Bone White and a crossed-out distorted gradient version. Editorial, gallery-catalogue aesthetic. No decorative noise. Aspect ratio 4:3.
```

---

## 7. Favicon Set(3:1,展示用)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

Show the DropHawk mark adapted for favicon use, rendered as a 3x1 row of preview tiles on Bone White #F5F2EC: 16px on a fake browser tab; 32px on a fake bookmark bar; 180px Apple touch icon with rounded square mask, Night Indigo #0E1A2B background and the mark in Bone White with a Hunter Gold #E8A93C eye accent. Below each tile, tiny Slate #5A6878 caption with the pixel size. Aspect ratio 3:1.
```

---

## 8. Hero Illustration / 主插画(16:9)

```
Style: minimal modernist tech brand identity, restrained and confident, inspired by Linear / Vercel / Stripe but with a touch of analog falconry warmth. Color palette MUST use exactly these hex values: Night Indigo #0E1A2B, Hunter Gold #E8A93C, Bone White #F5F2EC, Slate #5A6878. Typography vibe: Inter Display for headings, JetBrains Mono for code/domains. Mood: a falconer at dusk — patient, sharp, decisive. NOT cartoonish, NOT cyberpunk neon, NOT gradient-heavy, NOT 3D-render glossy.

A single editorial illustration for DropHawk's marketing site. A lone hawk perched on a thin geometric line at dusk, looking down at a field of faint monospace domain names floating below like a star map (getagent.com, vault.io, lumen.net, etc., partially faded). One domain in the foreground glows in Hunter Gold #E8A93C; the rest in Slate #5A6878. Flat vector, two-tone with Night Indigo #0E1A2B sky and Bone White #F5F2EC horizon, no painterly textures, no realism, no human figures. Mood: patient, surgical, slightly cinematic. Aspect ratio 16:9.
```

---

## 使用建议

1. **一次只跑 1–2 张**,先确认风格对路,再批量出剩下的。
2. 如果模型出来太"花",在提示词末尾再加一句:`Reduce visual noise by 50%. Favor empty space.`
3. 出图后按文件里**输出路径约定**命名,放到 `docs/design/refs/`。
