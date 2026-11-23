from shopcart.models import Item, Order
from shopcart.stats import average_order_value, total_revenue


def test_total_revenue():
    orders = [Order(1, [Item("a", 10.0)]), Order(2, [Item("b", 5.0, 2)])]
    assert total_revenue(orders) == 20.0


def test_average_order_value():
    orders = [Order(1, [Item("a", 10.0)]), Order(2, [Item("b", 30.0)])]
    assert average_order_value(orders) == 20.0


def test_average_order_value_empty():
    assert average_order_value([]) == 0.0
