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

    @property
    def total(self) -> float:
        from .pricing import apply_coupon

        subtotal = sum(i.price * i.qty for i in self.items)
        return apply_coupon(subtotal, self.coupon)
