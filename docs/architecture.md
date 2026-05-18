# Architecture

> 状态:M1-A 骨架阶段。业务通路仍以 [PRD.md](../PRD.md) 第 4、5、6 节为准。

## 进程模型

DropHawk v1 采用单进程模型:
- `FastAPI` 提供健康检查与后续 Web 控制台;
- `APScheduler` 后续接入同一进程,负责每日 drop 抓取、watchlist 检查、备份任务;
- `SQLite` 放在 `data/` 下,通过 Docker volume 持久化。

这个模型优先保证部署简单。等抓取任务耗时或 Web 访问压力变大后,再评估拆出 worker。

## 当前模块

| 模块 | 责任 |
| --- | --- |
| `app/main.py` | FastAPI 应用入口、生命周期初始化、`/healthz` |
| `app/config.py` | 读取环境变量与 `config/config.yaml`,生成运行配置 |
| `app/domain.py` | 域名规范化、TLD 校验、基础特征提取 |
| `app/scoring.py` | 按 PRD 权重计算候选域名分数与命中规则 |
| `app/db.py` | SQLite 初始化、基础连接上下文 |
| `app/feishu/cards.py` | 生成飞书交互卡片 JSON,不负责真实发送 |
| `app/scheduler.py` | 定时任务占位,后续 M1-B/M2 填充 |

## 数据库

M1-A 初始化两张基础表:
- `candidates`:候选域名主表,先包含域名、TLD、来源、得分、状态、发现/推送时间;
- `app_state`:保存轻量运行状态,当前写入 `schema_version=1`。

索引:
- `(domain, source)` 唯一索引用于同来源去重;
- `score` 和 `found_at` 索引用于后续列表筛选与近期推送查询。

## 配置

非密钥配置放在 `config/config.yaml`,包括数据库路径、评分阈值/权重、RDAP QPS、定时表达式。密钥仅允许进入 `config/secrets.env.local` 或部署环境变量,仓库只保留 `config/secrets.env.example`。

## 待填充

- 三类来源的数据流实现;
- RDAP 核查、飞书真实推送与多维表格写入;
- 配置热加载;
- 失败重试、限流与运行日志。
