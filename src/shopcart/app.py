"""Entry points that reproduce the demo bugs: python -m shopcart.app [aov|coupon|page]."""

import sys

from .models import Item, Order
from .pagination import get_page
from .stats import average_order_value


def report_for_new_shop() -> str:
    return f"AOV: {average_order_value([]):.2f}"


def checkout_with_lowercase_coupon() -> float:
    return Order(1, [Item("tee", 20.0, 2)], coupon="welcome10").total


def last_page_of_orders() -> list:
    orders = [Order(i) for i in range(25)]
    return get_page(orders, page=3, per_page=10)


if __name__ == "__main__":
    {"aov": report_for_new_shop, "coupon": checkout_with_lowercase_coupon, "page": last_page_of_orders}[sys.argv[1]]()
