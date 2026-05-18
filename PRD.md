# 域名扫描抢注 Agent — PRD

版本: v0.1 · 编写日期: 2026-05-15 · 状态: 待评审

---

## 1. 背景与目标

### 1.1 背景
- 每天有大量 `.com / .net` 域名因到期未续费被释放(drop)进入可注册池;其中不乏有商业价值的短词、双拼、字典词、品牌相关域名。
- 通过人工盯盘成本高、错过窗口期常见。
- 注册商 API 抢注链路重、风险高(押金、误下单、合规),本期**不做自动下单**。

### 1.2 本期目标(MVP)
做一个长期跑在服务器上的 Agent,能够:
1. **自动发现**每日新进入可注册池的 `.com / .net` 域名;
2. **按规则评分筛选**出值得关注的域名;
3. **第一时间推送**到飞书群(机器人 Webhook),并把详细信息写入飞书多维表格归档;
4. 提供一个**轻量 Web 控制台**,用于查看候选列表、命中记录、调整关键词规则、手动提交监控清单。
5. 抢注由人通过推送消息里的链接跳转到注册商手工下单完成。

### 1.3 非目标(本期不做)
- ❌ 自动对接注册商 API 下单
- ❌ 抢注押金、并发抢注、Drop-catch 极速抢注(毫秒级)
- ❌ 域名估值(DA / 反链 / 历史快照分析)—— v2 再考虑
- ❌ 支持 .com/.net 之外的 TLD —— v2 视效果再扩展
- ❌ 多用户/权限/SaaS 化

---

## 2. 用户与场景

| 角色 | 场景 |
| --- | --- |
| 域名运营(主用户) | 早上打开飞书,看群消息里今天的"高分推送";到 Web 控制台筛掉不要的;点链接到注册商抢注 |
| 域名运营 | 想新增一批关键词字典(如 "ai+短词")或一批手工监控的特定域名,在 Web 控制台粘进去 |
| 同事 | 飞书多维表格里翻历史命中,人工标注哪些抢到了 / 哪些后悔没抢,沉淀经验 |

---

## 3. 候选域名三大来源

### 3.1 每日删除池(Daily Drop List)
- **数据源**: 公开的每日删除清单。优先选择免费且稳定的源:
  - 主源:`https://www.whoisds.com/whois-database/newly-registered-domains/` 的 **deleted/expired** 板块(每日一份 zip,含全量 dropping 列表);
  - 备源:`https://member.expireddomains.net/` 的免费每日删除列表(需账号,可登录后抓);
  - 兜底:`https://www.publicdomainregistry.com` / `https://research.domaintools.com` 的 RSS 或 CSV(若可用)。
- **抓取频率**: 每天 UTC 02:00 跑一次(对应国内 10:00,首尔服务器 11:00),拉取过去 24h 的删除清单。
- **量级预估**: `.com + .net` 每日 drop 约 5w–15w 条。

### 3.2 关键词字典生成
- 用户在 Web 控制台维护**关键词字典**(分组管理),例如:
  - 前缀组:`ai / get / my / try / use / hi / go / lab / hub`
  - 词根组:`agent / flow / chat / vision / mind / data / cloud / pixel`
  - 后缀组:`(空) / ly / io-style / app / hub / lab`
- Agent 按 `prefix × root × suffix` 笛卡尔积生成候选,去重后加入待查队列。
- 上限:每个字典组合一次性最多生成 **10000** 条候选,避免爆量。

### 3.3 用户手动提交清单
- Web 控制台提供"批量粘贴"入口,支持一次提交最多 1000 条域名;
- 提交后进入**持续监控队列**(`watchlist`),Agent 每天检查一次可用性,直到:
  - 域名变成可注册 → 推送 + 入表 + 从队列移除;
  - 用户手动取消监控;
  - 监控满 365 天自动归档。

---

## 4. 处理流水线

```
┌────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌─────────────┐
│ 三大数据源 │ → │ 候选入库去重 │ → │ 评分 / 过滤  │ → │ 可用性核查   │ → │ 推送 + 入表 │
│ (drop/字典/│   │ (Sqlite)     │   │ (规则引擎)   │   │ (RDAP/whois) │   │ (飞书)      │
│  watchlist)│   └──────────────┘   └──────────────┘   └──────────────┘   └─────────────┘
└────────────┘
```

### 4.1 评分规则(可在 Web 控制台调参)
得分 = 加分项之和 - 减分项之和,默认阈值 ≥ **60** 才推送。

| 维度 | 分值 | 说明 |
| --- | --- | --- |
| 长度 ≤ 4 字符 | +50 | 短即贵 |
| 长度 5 字符 | +30 |
| 长度 6 字符 | +15 |
| 长度 7+ | +0 |
| 纯字母(无数字、无连字符) | +20 |
| 含数字 | -10 |
| 含连字符 | -20 |
| TLD = .com | +20 |
| TLD = .net | +5 |
| 命中关键词字典中"高价值词根" | +25 |
| 命中用户 watchlist | +100(必推送) |
| Pronounceable(元音/辅音规律)| +10 | 简单启发式,如 `ai/io/ka/me` |

阈值、各项权重都做成**可配置**(存在 `config.yaml` + Web 表单,改完热加载)。

### 4.2 可用性核查
- 优先用 **RDAP**(`https://rdap.verisign.com/com/v1/domain/<name>`)代替传统 whois,速度快、限流宽松、返回结构化 JSON;
- 限流策略:每 IP 对 Verisign RDAP 控制在 **8 QPS** 以内(留余量);
- 失败兜底:DNS NS 查询 + whois 命令行(只用于复核高分候选)。
- **缓存**:已确认"已注册"的域名 7 天内不再核查(到期前另起监控周期)。

### 4.3 推送格式(飞书群机器人)
采用**交互卡片**(message_card),示例:

```
🔥 [高价值域名释放] getagent.com
得分: 92 | 长度: 8 | TLD: .com
来源: 每日删除池(2026-05-15)
命中规则: ai 词根 + 纯字母 + .com
[阿里云查询] [Namecheap 查询] [Dynadot 查询] [详情页]
```

按钮链接直接拼到注册商查询页(无需 API):
- 阿里云: `https://wanwang.aliyun.com/domain/searchresult?keyword=<domain>`
- Namecheap: `https://www.namecheap.com/domains/registration/results/?domain=<domain>`
- Dynadot: `https://www.dynadot.com/domain/search?domain=<domain>`

### 4.4 写入飞书多维表格
- Base:部署时从 `secrets.env.local` 或环境变量读取,不写入公开仓库。
- Table:部署时从 `secrets.env.local` 或环境变量读取,不写入公开仓库。
- **建议字段**(部署阶段我会先读取你的现有 schema,匹配映射;以下为期望字段,缺失的我会建议你新增):

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| 域名 | 文本 | `getagent.com` |
| TLD | 单选 | `.com / .net` |
| 长度 | 数字 |
| 得分 | 数字 |
| 来源 | 单选 | `drop / dict / watchlist` |
| 命中规则 | 多选 | `短域名/纯字母/AI词根/...` |
| 发现时间 | 日期时间 |
| 状态 | 单选 | `待查看 / 已注册 / 已放弃 / 我已抢到` |
| 阿里云链接 | URL |
| 备注 | 富文本 |

---

## 5. Web 控制台

### 5.1 技术栈
- 后端: **Python 3.11 + FastAPI**(和 Agent 同进程,共享数据库)
- 前端: **HTMX + Tailwind**(轻量,不打包,改一行 HTML 立即生效;避免 React 的部署复杂度)
- 数据库: **SQLite**(单文件,百万行内性能足够;放在 docker volume)
- 访问方式: 部署在服务器 `8088` 端口,通过你的 frps 反向代理出来,或 nginx + basic auth

### 5.2 页面清单

| 页面 | 内容 |
| --- | --- |
| `/` 仪表盘 | 今日推送数、本周命中数、各来源候选量、最近 20 条推送 |
| `/candidates` 候选列表 | 表格 + 筛选(来源、得分、长度、TLD、日期),支持手动标记/导出 |
| `/dict` 关键词字典 | 增删改前缀/词根/后缀分组,实时预览组合数 |
| `/watchlist` 监控清单 | 粘贴批量域名,查看每条状态(还在等 / 已可用 / 已推送) |
| `/rules` 评分规则 | 表单形式编辑各项权重和阈值,保存即热生效 |
| `/logs` 运行日志 | 最近一次抓取、推送失败、限流情况 |
| `/settings` 设置 | 飞书 webhook、Base/Table ID、RDAP QPS、定时表达式 |

### 5.3 鉴权
- v1 简单:**HTTP Basic Auth**,用户名密码写在环境变量,前置 nginx;
- v2 再考虑接入飞书 SSO。

---

## 6. 部署方案(腾讯云首尔 / Ubuntu / Docker)

### 6.1 目录结构(本地仓库)
```
Y:\域名扫描抢注注册agent\
├── PRD.md                  # 本文件
├── README.md
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── app/
│   ├── main.py             # FastAPI entry
│   ├── scheduler.py        # APScheduler 定时任务
│   ├── sources/            # drop/dict/watchlist 三类源
│   ├── scoring.py
│   ├── rdap.py
│   ├── feishu/             # webhook + bitable client
│   ├── web/                # HTMX templates + static
│   └── db.py               # sqlite 模型
├── data/                   # 挂载,放 sqlite + 抓取的 drop 列表归档
├── config/
│   ├── config.yaml         # 配置(评分权重、定时、QPS)
│   └── secrets.env.local   # webhook url / bitable token,不入仓
└── scripts/
    ├── deploy.sh
    └── backup.sh
```

### 6.2 docker-compose 服务
- `app` — Python 服务,跑 FastAPI + APScheduler(同进程,够用)
- `caddy`(可选) — 自动 HTTPS + Basic Auth,或者直接用你已有的 nginx

### 6.3 部署流程
1. 本地完成开发 + 跑单元测试;
2. `git push` 到你的私有仓(待定);或者直接 `rsync` 到服务器 `/opt/domain-agent/`;
3. 服务器上 `docker compose up -d --build`;
4. 数据持久化:`./data` 和 `./config` 挂载;
5. 健康检查:`/healthz` 返回 `{ok:true, last_drop_pull:...}`;
6. 故障恢复:`docker compose restart app`;数据库每天 04:00 自动备份到 `data/backup/`。

### 6.4 飞书认证
- 推送用**群机器人 Webhook**:部署时通过 `FEISHU_WEBHOOK_URL` 注入,不写入公开仓库;
- 写多维表格需要**应用身份**(tenant_access_token):
  - 创建一个**自建应用**,开通"多维表格"权限;
  - 把应用加为目标 Base 的协作者(可编辑);
  - app_id / app_secret 放进 `secrets.env.local`;
  - **本地已经有 lark-cli 配置**,可以复用其凭据,不必新建应用。部署阶段确认即可。

---

## 7. 里程碑与排期

| 里程碑 | 内容 | 预计 |
| --- | --- | --- |
| **M1 数据通路打通**(D+2) | 飞书 Webhook 推送 + 多维表格写入跑通,推一条假数据验证 | 2 天 |
| **M2 Drop 池抓取 + 评分** (D+4) | whoisds 抓取 → 解析 → 评分 → 触发推送 | 2 天 |
| **M3 RDAP 可用性核查 + 字典生成 + watchlist**(D+7) | 三类源齐活,推送内容稳定 | 3 天 |
| **M4 Web 控制台**(D+10) | 仪表盘 / 候选列表 / 字典 / watchlist / 规则 / 设置 | 3 天 |
| **M5 部署到首尔服务器**(D+11) | Docker 化 + 持久化 + 健康检查 + 日志 | 1 天 |
| **M6 试运行调优**(D+14) | 跑 3 天,根据噪声/漏报调评分阈值 | 3 天 |

---

## 8. 关键风险与对策

| 风险 | 对策 |
| --- | --- |
| Drop 列表数据源停服或封 IP | 多源切换 + 失败重试 + 在 Web 显示数据源健康度;必要时上代理 |
| RDAP 限流被封 | 严格限速 + 失败退避 + 关键候选才查 |
| 噪声推送过多导致群骚扰 | 默认只推 ≥60 分;支持"安静时段";支持"日报模式"(每天 10:00 汇总推一次) |
| 多维表格写入额度 | 飞书 Open API 写入有 QPS 限制,批量写时分批 + 退避 |
| 数据库膨胀 | 候选表只留 90 天;归档表移到月度文件;每周 vacuum |
| 服务器 SSH 偶发不通 | 部署完成后用 frps 反代 + Web 控制台远程管理,SSH 仅作兜底 |

---

## 9. 待你确认的事项

1. **评分阈值 60 分、关键词字典示例**:是否合用,还是你心里有更具体的目标域名画像?
2. **推送节奏**:实时推(发现一条推一条) vs 每天 10:00 汇总日报推?(我倾向"高分实时 + 中分日报")
3. **Web 控制台访问**:走 frps 暴露公网 + Basic Auth,还是只在内网/跳板访问?
4. **飞书应用**:复用本地 lark-cli 已配置的自建应用,还是另起一个专用应用?
5. **多维表格字段**:你的现有表 schema 是否已经包含上面期望的字段?需要我先用 lark-cli 读一下吗?
