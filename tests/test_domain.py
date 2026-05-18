import pytest

from app.domain import parse_domain


def test_parse_domain_normalizes_supported_domain() -> None:
    domain = parse_domain(" GetAgent.COM. ")

    assert domain.value == "getagent.com"
    assert domain.sld == "getagent"
    assert domain.tld == ".com"
    assert domain.length == 8
    assert domain.is_pure_letters is True


def test_parse_domain_rejects_unsupported_tld() -> None:
    with pytest.raises(ValueError, match="Unsupported TLD"):
        parse_domain("vault.io")

