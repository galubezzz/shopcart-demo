from shopcart.api import handle
from shopcart.store import INVOICES


def test_health():
    assert handle("GET", "/health") == (200, {"status": "ok"})


def test_unknown_order_is_404():
    assert handle("GET", "/orders/999")[0] == 404


def test_single_word_product():
    status, body = handle("GET", "/products/mug")
    assert status == 200 and body["name"] == "Mug"


def test_unknown_route_and_method():
    assert handle("GET", "/nope")[0] == 404
    assert handle("POST", "/health")[0] == 405


def test_invoice_numbers():
    assert INVOICES[1].number == "INV-0001"


def test_get_order_returns_correct_data():
    status, body = handle("GET", "/orders/1")
    assert status == 200
    assert body == {"id": 1, "customer_id": 7, "total": 24.0}
