import re
from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    price: float
    qty: int = 1


@dataclass
class Order:
    id: int
    items: list[Item] = field(default_factory=list)
    coupon: str | None = None
    customer_id: int | None = None

    @property
    def total(self) -> float:
        from .pricing import apply_coupon

        subtotal = sum(i.price * i.qty for i in self.items)
        return apply_coupon(subtotal, self.coupon)


@dataclass
class Product:
    name: str
    price: float


def slugify(name: str) -> str:
    """URL slug of a product name: 'Coffee Mug' -> 'coffee-mug'."""
    return re.sub(r"\s+", "-", name.strip().lower())
