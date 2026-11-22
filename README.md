# shopcart (demo target)

A tiny package with three seeded bugs for the Bug Investigator demo:

| Command | Bug |
|---|---|
| `PYTHONPATH=src python -m shopcart.app aov` | `ZeroDivisionError` in `average_order_value([])` |
| `PYTHONPATH=src python -m shopcart.app coupon` | `KeyError` — coupons are documented as case-insensitive, unknown codes should give 0 |
| `PYTHONPATH=src python -m shopcart.app page` | `IndexError` — off-by-one: last page is rejected |

Existing tests pass: `PYTHONPATH=src pytest -q`.
