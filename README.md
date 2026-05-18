# DropHawk · 鹰隼

> **See the drop. Strike first.**
> **盯准释放,先人一步。**

DropHawk 是一个长期驻守的域名情报 Agent:
监控每日 `.com / .net` 删除池,按规则筛出高价值释放域名,**第一时间推送飞书 + 归档多维表格**,抢注由人工跳转注册商完成。

- 主域:**drophawk.flaios.com**(部署待定)
- 部署:腾讯云首尔 · Ubuntu · Docker
- 状态:**WIP**(M0 — 文档与规范阶段)

---

## 文档地图(必读)

| 文档 | 用途 |
| --- | --- |
| [PRD.md](./PRD.md) | 产品需求文档 —— **任何代码变更前先读这个** |
| [docs/brand.md](./docs/brand.md) | 命名、Slogan、VI 规范 |
| [docs/architecture.md](./docs/architecture.md) | 技术架构(M1 起填充) |
| [docs/data-sources.md](./docs/data-sources.md) | 三类候选来源的抓取/解析/限流细节 |
| [docs/deployment.md](./docs/deployment.md) | 部署与运维手册 |
| [docs/runbook.md](./docs/runbook.md) | 故障处理 / 常见问题 |
| [CHANGELOG.md](./CHANGELOG.md) | 版本变更记录 |

---

## 目录结构

```
drophawk/
├── README.md              # 本文件
├── PRD.md                 # 产品需求(权威)
├── CHANGELOG.md           # 变更日志
├── .gitignore
│
├── docs/                  # 所有非代码文档集中在这里
│   ├── brand.md
│   ├── architecture.md
│   ├── data-sources.md
│   ├── deployment.md
│   ├── runbook.md
│   └── api.md
│
├── app/                   # Python 应用代码(FastAPI + Scheduler)
│   ├── main.py
│   ├── scheduler.py
│   ├── sources/           # drop / dict / watchlist
│   ├── scoring.py
│   ├── rdap.py
│   ├── feishu/            # webhook + bitable 客户端
│   ├── web/               # HTMX 模板 + 静态资源
│   └── db.py
│
├── config/
│   ├── config.yaml        # 评分权重 / 定时 / QPS,入仓
│   └── secrets.env.local  # webhook / token / 密码,**不入仓**
│
├── data/                  # SQLite + drop 归档,运行时挂载,**不入仓**
├── scripts/               # deploy / backup / 一次性脚本
├── tests/
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

---

## 协作规则(强约束 · 人与 AI 同等遵守)

后续任何参与者(人类工程师 / AI Agent)都必须按以下规则执行。**违反任意一条都视为不合格交付。**

### R1 · 先读文档,再动代码
- 任何功能性改动开工前,**必须先读 [PRD.md](./PRD.md) 当前版本**。PRD 没覆盖的需求,**先更新 PRD 再写代码**。
- 架构性改动同步更新 `docs/architecture.md`。
- 不允许"代码先行、文档后补",也不允许"凭记忆写"。

### R2 · 密钥与本地敏感信息
- 文件名带 `.local.` 的一律**不入仓**(已在 `.gitignore`)。例:`secrets.env.local`、`credentials.local.json`。
- **不要把 webhook URL、app_secret、SSH 密码、服务器 IP 写进任何入仓文件**(包括注释、commit message、PR 描述)。
- 服务器凭据只放在 `Y:\服务器管理\` 对应子目录中,**不进入本仓库**。

### R3 · 命名与风格
- 仓内外、文档、代码、Slack/飞书:统一用 **DropHawk**(首字母大写,无空格)。
- 中文场合允许说"鹰隼",不要写成"鹰盯""抓鸟""drop hawk""drop-hawk"。
- 域名一律小写;TLD 保留前导点(`.com`),不写 `com` 或 `COM`。
- Python:PEP 8 + `ruff` 默认规则;变量用 `snake_case`,类用 `PascalCase`。
- Markdown:中文与英文/数字之间**留一个半角空格**(本文档示例)。

### R4 · 提交规范
- 一个 commit 做一件事。`feat: / fix: / docs: / chore: / refactor:` 前缀。
- commit message 写 **WHY**,不写 **WHAT**(代码本身已说明 what)。
- 直接推 `main` 仅限于:文档 typo、CI 修复、紧急回滚。其它都走 PR。

### R5 · 部署与运维
- 生产环境只接受从 `main` 分支构建的镜像。
- 任何在服务器上手动改的东西(配置、cron、文件),**24h 内必须回流到仓库**,否则下次重建会丢。
- 备份不可跳过:`data/` 每天 04:00 自动备份到 `data/backup/`,保留 14 天。

### R6 · AI Agent 专用规则
如果你是 AI(Claude / Codex / 其他):
- **不要**主动创建 README、文档或总结性 `.md` 文件,除非用户明确要求。本仓库的文档结构已固定,**新增文档需先在 PR 描述中说明位置和理由**。
- **不要**为了"健壮性"添加用户没要求的兜底、重试、特性开关、抽象层。三行重复优于一个早产的封装。
- 改动前用 `Read` / `Grep` 确认现状;改动后**只汇报变更**,不要重述代码逻辑。
- 涉及密钥、推送、写入多维表格、SSH 远程的操作,**先列出准备执行的命令,等用户确认再执行**。
- 服务器侧操作:除非用户授权,**只生成命令给用户复制粘贴**,不要自己 SSH 上去跑。

### R7 · 文档更新节奏
- 完成一个里程碑(M1/M2/...)→ 更新 `CHANGELOG.md` + 对应 `docs/*`。
- PRD 内容发生与代码不一致的改动 → 先改 PRD,在 commit message 中引用 PRD diff 链接。

---

## 快速开始

> M1 完成后填充。当前阶段不可运行。

---

## 联系与反馈

内部项目,反馈走飞书。
