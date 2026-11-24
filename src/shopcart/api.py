"""Minimal JSON HTTP API for the shop (standard library WSGI, no dependencies).

Run the server:   PYTHONPATH=src python -m shopcart.api              # http://localhost:8080
Replay one call:  PYTHONPATH=src python -m shopcart.api GET /orders/1

Missing records are answered with 404, and the traceback goes to the server log.
"""

import json
import logging
import re
import sys
from wsgiref.simple_server import make_server

from . import store
from .models import slugify

log = logging.getLogger("shopcart.api")


def health() -> dict:
    return {"status": "ok"}


def get_order(order_id: str) -> dict:
    # Convert the path parameter to int because the store expects an integer ID.
    order = store.get_order(int(order_id))
    return {"id": order.id, "customer_id": order.customer_id, "total": order.total}


def get_invoice(order_id: str) -> dict:
    order = store.get_order(int(order_id))
    invoice = store.get_invoice(order)
    return {"number": invoice.number, "order_id": invoice.order_id, "amount": invoice.amount}


def get_product(slug: str) -> dict:
    product = store.find_product(slug)
    return {"slug": slugify(product.name), "name": product.name, "price": product.price}


ROUTES = [
    (re.compile(r"^/health$"), health),
    (re.compile(r"^/orders/(?P<order_id>[^/]+)$"), get_order),
    (re.compile(r"^/orders/(?P<order_id>[^/]+)/invoice$"), get_invoice),
    (re.compile(r"^/products/(?P<slug>[^/]+)$"), get_product),
]


def handle(method: str, path: str) -> tuple[int, dict]:
    """Route one request. Returns (HTTP status, JSON body)."""
    if method != "GET":
        return 405, {"error": "method not allowed"}
    for pattern, view in ROUTES:
        if m := pattern.match(path):
            try:
                return 200, view(**m.groupdict())
            except LookupError:
                # A missing record is a normal 404 for the client; keep the traceback in the logs.
                log.warning("404 %s %s", method, path, exc_info=True)
                return 404, {"error": "not found"}
    return 404, {"error": "no such route"}


def app(environ, start_response):
    status, body = handle(environ["REQUEST_METHOD"], environ.get("PATH_INFO") or "/")
    reason = {200: "OK", 404: "Not Found", 405: "Method Not Allowed"}[status]
    data = json.dumps(body).encode()
    start_response(f"{status} {reason}", [("Content-Type", "application/json"), ("Content-Length", str(len(data)))])
    return [data]


def main(argv: list[str]) -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    if len(argv) == 2:
        status, body = handle(argv[0], argv[1])
        print(status, json.dumps(body))
        return
    with make_server("", 8080, app) as server:
        log.info("serving on http://localhost:8080")
        server.serve_forever()


if __name__ == "__main__":
    main(sys.argv[1:])
