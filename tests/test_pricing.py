from shopcart.pricing import apply_coupon, get_discount


def test_known_coupon():
    assert get_discount("WELCOME10") == 0.10


def test_no_coupon():
    assert apply_coupon(100.0, None) == 100.0


def test_lowercase_coupon():
    assert get_discount("welcome10") == 0.10

def test_unknown_coupon():
    assert get_discount("invalid") == 0.0
