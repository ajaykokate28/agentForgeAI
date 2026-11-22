# Sample customer data for testing purposes
CUSTOMERS = {
    101: {
        "customer_id": 101,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "membership": "Gold"
    },
    102: {
        "customer_id": 102, 
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "membership": "Silver"
    }
}

ORDER = {
    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer_id": 101,
        "product": "Laptop",
        "quantity": 1,
        "amount": 1200.00,
        "order_status": "Shipped",
        "days_since_purchase": 5
    },
    "ORD-1002": {
        "order_id": "ORD-1002",
        "customer_id": 102,
        "product": "Smartphone",
        "quantity": 2,  
        "amount": 1600.00,
        "order_status": "Processing"
    },
    "ORD-1003": {
        "order_id": "ORD-1003",
        "customer_id": 101,
        "product": "Tablet",
        "quantity": 1,  
        "amount": 600.00,
        "order_status": "Delivered"
    }
}

PAYMENT = {
    "PAY-2001": {
        "payment_id": "PAY-2001",
        "order_id": "ORD-1001",
        "customer_id": 101,
        "amount": 1200.00,
        "status": "Completed"
    },
    "PAY-2002": {
        "payment_id": "PAY-2002",
        "order_id": "ORD-1002",
        "customer_id": 102,
        "amount": 1600.00,
        "status": "Pending"
    },
}

def get_customer_details(customer_id: int) -> dict | None:
    customer = CUSTOMERS.get(customer_id)
    if customer is None:
        return {
            "found": False,
            "message": f"No customer found with ID {customer_id}"
        }
    return{
        "found": True,
        "customer": customer
    }

def get_order_details(order_id: str)-> dict | None:
    order = ORDER.get(order_id)
    if order is None:
        return {
            "found": False,
            "message": f"No order found with ID {order_id}"
        }
    return {
        "found": True,
        "order": order
    }

def check_payment_status(order_id: str):
    """Check the status of a payment based on its ID."""
    payment = PAYMENT.get(order_id)
    if payment is None:
        return {
            "found": False,
            "message": f"No payment found for order ID {order_id}"
        }
    return {
        "found": True,
        "payment": payment
    }

def check_refund_eligibility(order_id: str) -> dict:
    """Check if a refund is eligible for a given order ID."""
    order = ORDER.get(order_id)

    if order is None:
        return {
            "eligible": False,
            "message": f"Order not found with ID {order_id}"
        }
    
    payment = PAYMENT.get(order_id)

    if payment is None:
        return {
            "eligible": False,
            "message": f"Payment record not found for order ID {order_id}"
        }
    
    if payment["payment_status"] != "Successful":
        return {
            "eligible": False,
            "message": f"Payment was not successful for order ID {order_id}"
        }
    if order["order_status"] != "Delivered":
        return {
            "eligible": False,
            "message": f"Order ID {order_id} has not been delivered yet"
        }
    if order["days_since_purchase"] > 30:
        return {
            "eligible": False,
            "message": f"Refund period has expired for order ID {order_id}"
        }
    return {
        "eligible": True,
        "reason": "Order is eligible for a refund",
        "refund_amount": order["amount"]
    }

if __name__ == "__main__":
    # Example usage
    print(check_refund_eligibility("ORD-1001"))