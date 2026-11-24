"""In-memory data the API serves (stands in for a database)."""

from dataclasses import dataclass

from .models import Item, Order, Product, slugify


@dataclass
class Invoice:
    number: str
    order_id: int
    amount: float


ORDERS: dict[int, Order] = {
    o.id: o
    for o in [
        Order(1, [Item("mug", 12.0, 2)], customer_id=7),
        Order(2, [Item("coffee-mug", 15.0)], coupon="WELCOME10", customer_id=7),
        Order(3, [Item("tee", 20.0, 3)], customer_id=9),
    ]
}

INVOICES: dict[int, Invoice] = {o.id: Invoice(f"INV-{o.id:04d}", o.id, o.total) for o in ORDERS.values()}

PRODUCTS: dict[str, Product] = {
    slugify(p.name): p for p in [Product("Mug", 12.0), Product("Coffee Mug", 15.0), Product("Tee", 20.0)]
}


def get_order(order_id: int) -> Order:
    return ORDERS[order_id]


def get_invoice(order: Order) -> Invoice:
    """Invoice issued for an order."""
    return INVOICES[order.id]


def find_product(slug: str) -> Product:
    """Product by its URL slug, e.g. 'coffee-mug'."""
    return PRODUCTS[_normalize_slug(slug)]


def _normalize_slug(slug: str) -> str:
    # Accept links like 'Coffee-Mug' and legacy ones like 'coffee_mug'.
    return slug.strip().lower().replace("-", "_")
