from app.feishu.cards import DomainPush, build_domain_release_card


def test_build_domain_release_card_contains_links() -> None:
    card = build_domain_release_card(
        DomainPush(
            domain="getagent.com",
            tld=".com",
            length=8,
            score=75,
            source="drop",
            matched_rules=("纯字母", ".com", "高价值词根"),
        )
    )

    assert card["msg_type"] == "interactive"
    actions = card["card"]["elements"][1]["actions"]
    urls = [action["url"] for action in actions]
    assert "wanwang.aliyun.com" in urls[0]
    assert "namecheap.com" in urls[1]
    assert "dynadot.com" in urls[2]

