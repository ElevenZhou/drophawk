# Internal API

> 状态:M1-A 骨架阶段。M4(Web 控制台)阶段继续扩展。

## 路由

### `GET /healthz`

用于容器健康检查与部署验证。

响应示例:

```json
{
  "ok": true,
  "service": "DropHawk",
  "environment": "local",
  "database": "Y:\\域名扫描抢注注册agent\\data\\drophawk.sqlite3",
  "started_at": "2026-05-15T00:00:00+00:00"
}
```

## 待填充

- Web 控制台路由;
- 候选列表、字典、watchlist、规则设置 API;
- 飞书 Webhook 发送接口与 dry-run 验证入口;
- Basic Auth 接入;
- 速率限制。
