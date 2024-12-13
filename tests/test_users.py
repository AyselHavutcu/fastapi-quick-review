from app import schemas
import pytest
from jose import jwt
from app.config import settings


def test_create_user(client):
    res = client.post("/users/", json={"email": "test123@gmail.com", "password": "12345", "phone_number": "00"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test123@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password":test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=settings.algorithm)
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code",
                         [("wrong_email@gmail.com", "12345", 403),
                          ("test123@gmail.com", "wrongpass", 403),
                          (None, "wrongpass", 403)])
def test_incorrect_login(email,password,status_code, client):
    res = client.post("/login", data={"username": email, "password":password})

    assert status_code == 403
    assert res.json().get("detail") == "Invalid Credentials"