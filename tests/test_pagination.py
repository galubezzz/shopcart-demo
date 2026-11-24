from shopcart.pagination import get_page, total_pages


def test_total_pages():
    assert total_pages(25, 10) == 3


def test_first_page():
    assert get_page(list(range(25)), 1) == list(range(10))


def test_last_page():
    assert get_page(list(range(25)), 3) == list(range(20, 25))
