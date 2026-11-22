from app.tools.customer_tools import (
    get_customer_info,
    get_order_info,
    get_payment_info
)

def test_get_customer_info():
    # Test with a valid customer ID
    customer_info = get_customer_info(101)
    assert customer_info is not None
    assert customer_info["name"] == "Alice Smith"
    assert customer_info["email"] == "alice.smith@example.com"
    assert customer_info["phone"] == "555-1234"

    # Test with an invalid customer ID
    customer_info = get_customer_info(999)
    assert customer_info is None

def test_get_order_info():
    # Test with a valid order ID
    order_info = get_order_info("ORD-1001")
    assert order_info is not None
    assert order_info["Product"] == "Laptop"
    assert order_info["Quantity"] == 1
    assert order_info["Price"] == 1200.00
    assert order_info["Status"] == "Shipped"

    # Test with an invalid order ID
    order_info = get_order_info("ORD-9999")
    assert order_info is None

def test_get_payment_info():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-1001")
    assert payment_info is not None
    assert payment_info["Amount"] == 1200.00
    assert payment_info["Method"] == "Credit Card"
    assert payment_info["Status"] == "Completed"

    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"

def test_get_payment_info_invalid_id():
    # Test with an invalid payment ID
    payment_info = get_payment_info("PAY-9999")
    assert payment_info is None

def test_get_payment_info_valid_id():
    # Test with a valid payment ID
    payment_info = get_payment_info("PAY-2001")
    assert payment_info is not None
    assert payment_info["amount"] == 1200.00
    assert payment_info["status"] == "Completed"
