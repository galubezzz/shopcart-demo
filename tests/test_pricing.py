from shopcart.pricing import apply_coupon, get_discount


def test_known_coupon():
    assert get_discount("WELCOME10") == 0.10


def test_no_coupon():
    assert apply_coupon(100.0, None) == 100.0


def test_lowercase_coupon():
    # Coupon codes should be case‑insensitive
    assert get_discount('welcome10') == 0.10
    # Applying the coupon should give the discounted amount
    assert apply_coupon(100.0, 'welcome10') == 90.0


def test_unknown_coupon():
    # Unknown coupon codes should result in no discount, not an exception
    assert get_discount('invalidcode') == 0.0
    assert apply_coupon(100.0, 'invalidcode') == 100.0
