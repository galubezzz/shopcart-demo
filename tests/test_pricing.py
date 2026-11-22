from shopcart.pricing import apply_coupon, get_discount


def test_known_coupon():
    assert get_discount("WELCOME10") == 0.10


def test_no_coupon():
    assert apply_coupon(100.0, None) == 100.0
