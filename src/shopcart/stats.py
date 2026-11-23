"""Order statistics."""

from .models import Order


def total_revenue(orders: list[Order]) -> float:
    return sum(o.total for o in orders)


def average_order_value(orders: list[Order]) -> float:
    """Average order value. Returns 0.0 when there are no orders."""
    if not orders:
        return 0.0
    return total_revenue(orders) / len(orders)
