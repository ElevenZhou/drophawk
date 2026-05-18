from dataclasses import dataclass

SUPPORTED_TLDS = {".com", ".net"}


@dataclass(frozen=True)
class DomainName:
    value: str
    sld: str
    tld: str

    @property
    def length(self) -> int:
        return len(self.sld)

    @property
    def has_number(self) -> bool:
        return any(char.isdigit() for char in self.sld)

    @property
    def has_hyphen(self) -> bool:
        return "-" in self.sld

    @property
    def is_pure_letters(self) -> bool:
        return self.sld.isalpha()


def parse_domain(raw_domain: str) -> DomainName:
    value = raw_domain.strip().lower().rstrip(".")
    if not value or "." not in value:
        raise ValueError(f"Invalid domain: {raw_domain!r}")

    sld, tld_without_dot = value.rsplit(".", 1)
    tld = f".{tld_without_dot}"
    if not sld or not tld_without_dot:
        raise ValueError(f"Invalid domain: {raw_domain!r}")
    if tld not in SUPPORTED_TLDS:
        raise ValueError(f"Unsupported TLD: {tld}")

    return DomainName(value=value, sld=sld, tld=tld)

