from dataclasses import dataclass

from app.config import ScoringConfig
from app.domain import DomainName

DEFAULT_HIGH_VALUE_ROOTS = {
    "agent",
    "ai",
    "chat",
    "cloud",
    "data",
    "flow",
    "mind",
    "vision",
}


@dataclass(frozen=True)
class ScoreResult:
    score: int
    matched_rules: tuple[str, ...]
    should_push: bool


def score_domain(
    domain: DomainName,
    *,
    source: str,
    scoring: ScoringConfig,
    high_value_roots: set[str] | None = None,
) -> ScoreResult:
    roots = high_value_roots or DEFAULT_HIGH_VALUE_ROOTS
    weights = scoring.weights
    score = 0
    matched: list[str] = []

    def add(rule: str, weight_key: str) -> None:
        nonlocal score
        score += weights.get(weight_key, 0)
        matched.append(rule)

    if domain.length <= 4:
        add("短域名<=4", "length_lte_4")
    elif domain.length == 5:
        add("短域名5", "length_5")
    elif domain.length == 6:
        add("短域名6", "length_6")

    if domain.is_pure_letters:
        add("纯字母", "pure_letters")
    if domain.has_number:
        add("含数字", "has_number")
    if domain.has_hyphen:
        add("含连字符", "has_hyphen")

    if domain.tld == ".com":
        add(".com", "tld_com")
    elif domain.tld == ".net":
        add(".net", "tld_net")

    if any(root in domain.sld for root in roots):
        add("高价值词根", "high_value_root")

    if source == "watchlist":
        add("watchlist", "watchlist")

    if is_pronounceable(domain.sld):
        add("可读性启发式", "pronounceable")

    return ScoreResult(
        score=score,
        matched_rules=tuple(matched),
        should_push=score >= scoring.threshold,
    )


def is_pronounceable(value: str) -> bool:
    if not value.isalpha() or len(value) < 3:
        return False

    vowels = set("aeiou")
    has_vowel = any(char in vowels for char in value)
    has_consonant = any(char not in vowels for char in value)
    if not has_vowel or not has_consonant:
        return False

    vowel_runs = _longest_run(value, vowels)
    consonant_runs = _longest_run(value, set("abcdefghijklmnopqrstuvwxyz") - vowels)
    return vowel_runs <= 2 and consonant_runs <= 3


def _longest_run(value: str, charset: set[str]) -> int:
    longest = 0
    current = 0
    for char in value:
        if char in charset:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest

