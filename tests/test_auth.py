import pytest
import utils.api_client as api_client
import test_data.payloads as payloads

class TestRegister:
    def test_valid_register_status_code(self):
        response= api_client.post("/register",payloads.VALID_REGISTER)
        assert response.status_code == 200

    def test_valid_reg_return_token(self):
        response= api_client.post("/register",payloads.VALID_REGISTER)
        body = response.json()

        assert "token" in body
        assert len(body["token"]) > 0

    def test_register_missing_password_status_code(self):
         response= api_client.post("/register",payloads.REGISTER_MISSING_PASSWORD)
         assert response.status_code == 400

    def test_register_missing_password_error_message(self):
        response = api_client.post("/register", payloads.REGISTER_MISSING_PASSWORD)
        body = response.json()

        assert "error" in body
        assert body["error"] == "Missing password"

class TestLogin:
    def test_valid_login_status_code(self):
        response=api_client.post("/login",payloads.VALID_LOGIN)
        assert response.status_code == 200

    def test_valid_login_returns_token(self):
        response = api_client.post("/login", payloads.VALID_LOGIN)
        body = response.json()

        assert "token" in body
        assert isinstance(body["token"], str)  # token must be a string
        assert len(body["token"]) > 0

    def test_invalid_login_status_code(self):
        response = api_client.post("/login", payloads.INVALID_LOGIN)
        assert response.status_code == 400

    def test_invalid_login_returns_error(self):
        response = api_client.post("/login", payloads.INVALID_LOGIN)
        body = response.json()

        assert "error" in body  # error key exists
        assert body["error"] != ""






