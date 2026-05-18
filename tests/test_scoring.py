from app.config import ScoringConfig
from app.domain import parse_domain
from app.scoring import score_domain

WEIGHTS = {
    "length_lte_4": 50,
    "length_5": 30,
    "length_6": 15,
    "pure_letters": 20,
    "has_number": -10,
    "has_hyphen": -20,
    "tld_com": 20,
    "tld_net": 5,
    "high_value_root": 25,
    "watchlist": 100,
    "pronounceable": 10,
}


def test_score_domain_matches_prd_weights() -> None:
    result = score_domain(
        parse_domain("getagent.com"),
        source="drop",
        scoring=ScoringConfig(threshold=60, weights=WEIGHTS),
    )

    assert result.score == 75
    assert result.should_push is True
    assert result.matched_rules == ("纯字母", ".com", "高价值词根", "可读性启发式")


def test_watchlist_domain_is_always_high_priority() -> None:
    result = score_domain(
        parse_domain("rough-name.net"),
        source="watchlist",
        scoring=ScoringConfig(threshold=60, weights=WEIGHTS),
    )

    assert result.score >= 60
    assert "watchlist" in result.matched_rules

