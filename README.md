# shopcart (demo target)

A tiny shop package with seeded bugs for the Bug Investigator demo.

## Crashes

| Command | Bug |
|---|---|
| `PYTHONPATH=src python -m shopcart.app aov` | `ZeroDivisionError` in `average_order_value([])` |
| `PYTHONPATH=src python -m shopcart.app coupon` | `KeyError`: coupons are documented as case-insensitive, unknown codes should give 0 |
| `PYTHONPATH=src python -m shopcart.app page` | `IndexError`, off by one: the last page is rejected |

## Silent 404s in the HTTP API

The API (`shopcart/api.py`, standard library only) keeps running and answers `404 {"error": "not found"}`. The real cause is only visible in the server log's traceback.

```bash
PYTHONPATH=src python -m shopcart.api                    # server on http://localhost:8080
PYTHONPATH=src python -m shopcart.api GET /orders/1      # or replay a single request
```

| Request | What the client sees | What's actually wrong |
|---|---|---|
| `GET /orders/1` | 404 for every existing order | The ID from the URL is the string `"1"`, but orders are stored under the integer `1` |
| `GET /orders/1/invoice` | 404 | The invoice is looked up by the customer's ID instead of the order's ID |
| `GET /products/coffee-mug` | 404, while `/products/mug` works | Slug normalization replaces `-` with `_` (reversed), so multi-word products are never found |

Existing tests pass: `PYTHONPATH=src pytest -q`.
