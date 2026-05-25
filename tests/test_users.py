import pytest
import utils.api_client as api_client
import test_data.payloads as payloads

class TestGetUsers:
    def test_get_all_users_with_status_code(self):
        response = api_client.get("/users?page=1")
        assert response.status_code == 200

    def test_all_users_return_data_array(self):
        response = api_client.get("/users?page=1")
        body=response.json()

        assert "data" in body
        assert isinstance(body["data"],list)
        assert len(body["data"]) > 0

    def test_get_all_users_response_time(self):
        response = api_client.get("/users?page=1")
        assert response.elapsed.total_seconds() < 3

class TestGetSingleUser:
    def test_get_single_user_status_code(self):
        response=api_client.get("/users/2")
        assert response.status_code == 200

    def test_get_single_user_correct_id(self):
        response = api_client.get("/users/2")
        body=response.json()

        assert body["data"]["id"]==2

    def test_get_single_user_has_required_fields(self):
        response = api_client.get("/users/2")
        body=response.json()
        user=body["data"]

        assert "id" in user
        assert"email" in user
        assert "first_name" in user
        assert "last_name" in user

    def test_single_user_email_format(self):

        response = api_client.get("/users/2")
        body= response.json()
        email = body["data"]["email"]
        assert "@" in email

class TestGetUserNotFound:
    def test_get_invalid_user_returns_404(self):
        response=api_client.get("/users/99")
        body = response.json()
        assert response.status_code == 404
        assert body == {}

class TestCreateUser:
    def test_create_user_status_code(self):
        response = api_client.post("/users",payloads.CREATE_USER)
        assert response.status_code == 201

    def test_create_user_returns_id(self):
        response = api_client.post("/users",payloads.CREATE_USER)
        body= response.json()

        assert "id" in body
        assert body["id"] is not None

    def test_create_user_returns_correct_data(self):
        response = api_client.post("/users", payloads.CREATE_USER)
        body = response.json()

        assert body["name"] == payloads.CREATE_USER["name"]
        assert body["job"] == payloads.CREATE_USER["job"]

    def test_create_user_returns_created_at(self):
        response = api_client.post("/users", payloads.CREATE_USER)
        body = response.json()

        assert "createdAt" in body

class TestUpdateUser:
    def test_update_user_status_code(self):
        response = api_client.put("/users/2",payloads.UPDATE_USER)
        assert response.status_code == 200

    def test_update_user_returns_updated_fields(self):
        response = api_client.put("/users/2",payloads.UPDATE_USER)
        body = response.json()

        assert body["name"] == payloads.UPDATE_USER["name"]
        assert body["job"] == payloads.UPDATE_USER["job"]

    def test_update_user_returns_updated_at(self):
        response = api_client.put("/users/2",payloads.UPDATE_USER)
        body = response.json()

        assert "updatedAt" in body

class TestDeleteUser:
    def test_delete_user_status_code(self):
        response = api_client.delete("/users/2")
        assert response.status_code == 204
    def test_delete_user_empty_response(self):
        response = api_client.delete("/users/2")
        assert response.text == ""




















