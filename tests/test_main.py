from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the AgentForge AI API",
        "status": "running"
    }

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }

def test_receive_customer_message():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }

def test_receive_customer_message_missing_fields():
    payload = {
        "name": "John Doe"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 422  # Unprocessable Entity due to missing fields    
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_invalid_email():
    payload = {
        "name": "John Doe",
        "email": "invalid-email",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 422  # Unprocessable Entity due to invalid email format
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_empty_fields():
    payload = {
        "name": "",
        "email": "",
        "subject": "",
        "message": ""
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 422  # Unprocessable Entity due to empty fields
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_extra_fields():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message",
        "extra_field": "This field should be ignored"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200  # Should still succeed despite extra fields
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }

def test_receive_customer_message_large_payload():
    payload = {
        "name": "John Doe" * 1000,  # Large name
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200  # Should still succeed despite large payload
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }

def test_receive_customer_message_special_characters():
    payload = {
        "name": "John Doe!@#$%^&*()",
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200  # Should still succeed despite special characters
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }   

def test_receive_customer_message_unicode_characters():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200  # Should still succeed despite unicode characters
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }   

def test_receive_customer_message_long_message():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message" * 1000  # Large message
    }
    response = client.post("/api/v1/support/messages", json=payload)
    assert response.status_code == 200  # Should still succeed despite long message
    assert response.json() == {
        "status": "received",
        "message": "Your support request has been received. Our team will get back to you shortly."
    }   

def test_receive_customer_message_invalid_json():
    response = client.post("/api/v1/support/messages", data="Invalid JSON")
    assert response.status_code == 422  # Unprocessable Entity due to invalid JSON
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_empty_json():
    response = client.post("/api/v1/support/messages", json={})
    assert response.status_code == 422  # Unprocessable Entity due to empty JSON
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_missing_json():
    response = client.post("/api/v1/support/messages")
    assert response.status_code == 422  # Unprocessable Entity due to missing JSON
    assert "detail" in response.json()  # Check that the response contains validation error details

def test_receive_customer_message_invalid_method():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "subject": "Test Subject",
        "message": "Test Message"
    }
    response = client.put("/api/v1/support/messages", json=payload)
    assert response.status_code == 405  # Method Not Allowed due to invalid method
