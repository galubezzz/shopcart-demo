"""Coupons and discounts."""

COUPONS = {"WELCOME10": 0.10, "BLACKFRIDAY": 0.30}


def get_discount(code: str | None) -> float:
    """Discount rate for a coupon code. Codes are case-insensitive; unknown codes give no discount (0.0)."""
    if not code:
        return 0.0
    # Normalise the coupon code to uppercase and strip whitespace before lookup.
    normalized = code.strip().upper()
    return COUPONS.get(normalized, 0.0)


def apply_coupon(amount: float, code: str | None) -> float:
    return round(amount * (1 - get_discount(code)), 2)
