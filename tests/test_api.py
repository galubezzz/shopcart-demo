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


def test_invoice_endpoint_returns_correct_data():
    status, body = handle("GET", "/orders/1/invoice")
    assert status == 200
    # Verify invoice fields match the stored invoice for order 1
    assert body["number"] == "INV-0001"
    assert body["order_id"] == 1
    # Amount should equal the total of order 1 (12.0 * 2 = 24.0)
    assert body["amount"] == 24.0
