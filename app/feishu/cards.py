from dataclasses import dataclass
from urllib.parse import quote


@dataclass(frozen=True)
class DomainPush:
    domain: str
    tld: str
    length: int
    score: int
    source: str
    matched_rules: tuple[str, ...]


def build_domain_release_card(push: DomainPush) -> dict[str, object]:
    domain = push.domain
    return {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "template": "yellow",
                "title": {"tag": "plain_text", "content": f"释放:{domain}"},
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": (
                            f"**得分:** {push.score} | **长度:** {push.length} | "
                            f"**TLD:** {push.tld}\\n"
                            f"**来源:** {push.source}\\n"
                            f"**命中规则:** {', '.join(push.matched_rules) or '无'}"
                        ),
                    },
                },
                {
                    "tag": "action",
                    "actions": [
                        _button("阿里云查询", aliyun_url(domain), "primary"),
                        _button("Namecheap 查询", namecheap_url(domain), "default"),
                        _button("Dynadot 查询", dynadot_url(domain), "default"),
                    ],
                },
                {
                    "tag": "note",
                    "elements": [
                        {"tag": "plain_text", "content": "See the drop. Strike first."},
                    ],
                },
            ],
        },
    }


def _button(text: str, url: str, button_type: str) -> dict[str, object]:
    return {
        "tag": "button",
        "text": {"tag": "plain_text", "content": text},
        "url": url,
        "type": button_type,
    }


def aliyun_url(domain: str) -> str:
    return f"https://wanwang.aliyun.com/domain/searchresult?keyword={quote(domain)}"


def namecheap_url(domain: str) -> str:
    return f"https://www.namecheap.com/domains/registration/results/?domain={quote(domain)}"


def dynadot_url(domain: str) -> str:
    return f"https://www.dynadot.com/domain/search?domain={quote(domain)}"

