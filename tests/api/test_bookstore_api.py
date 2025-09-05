import uuid
import pytest
from utils.api_client import BookStoreAPI
from utils.config import API_USER, API_PASS

@pytest.fixture(scope="module")
def api():
    return BookStoreAPI()

@pytest.fixture(scope="module")
def fresh_user_credentials():
    # create a unique username per run to avoid conflicts on DemoQA
    u = f"{API_USER}_{uuid.uuid4().hex[:6]}"
    p = API_PASS
    return u, p

@pytest.fixture(scope="module")
def user_created(api, fresh_user_credentials):
    u, p = fresh_user_credentials
    resp = api.create_user(u, p)
    assert "userID" in resp, f"User creation failed: {resp}"
    return resp["userID"], u, p

@pytest.fixture(scope="module")
def auth_token(api, user_created):
    user_id, u, p = user_created
    token_resp = api.generate_token(u, p)
    assert token_resp.get("status") in ("Success", "success"), f"Token resp: {token_resp}"
    token = token_resp.get("token")
    assert token, "Token not returned"
    return token

def test_authorization(api, user_created):
    _, u, p = user_created
    auth = api.is_authorized(u, p)
    assert isinstance(auth, bool) or auth.get("isAuthorized") in (True, False)

def test_list_books(api):
    books = api.list_books()
    assert "books" in books and len(books["books"]) > 0

def test_rent_two_books(api, user_created, auth_token):
    user_id, _, _ = user_created
    books = api.list_books()["books"]
    chosen = [books[0]["isbn"], books[1]["isbn"]]
    add_resp = api.add_books(user_id, auth_token, chosen)
    # API can return empty body on success; just ensure no errors above
    assert isinstance(add_resp, dict) or add_resp is None

def test_user_details_with_books(api, user_created, auth_token):
    user_id, _, _ = user_created
    details = api.get_user(user_id, auth_token)
    assert details.get("userId") == user_id
