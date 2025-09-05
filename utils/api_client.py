import requests
from utils.config import BASE_URL

class BookStoreAPI:
    def __init__(self):
        self.base = BASE_URL
        self.session = requests.Session()
        self.headers = {"Content-Type": "application/json"}

    def create_user(self, username, password):
        url = f"{self.base}/Account/v1/User"
        payload = {"userName": username, "password": password}
        r = self.session.post(url, json=payload, headers=self.headers, timeout=30)
        r.raise_for_status()
        return r.json()

    def generate_token(self, username, password):
        url = f"{self.base}/Account/v1/GenerateToken"
        payload = {"userName": username, "password": password}
        r = self.session.post(url, json=payload, headers=self.headers, timeout=30)
        r.raise_for_status()
        return r.json()

    def is_authorized(self, username, password):
        url = f"{self.base}/Account/v1/Authorized"
        payload = {"userName": username, "password": password}
        r = self.session.post(url, json=payload, headers=self.headers, timeout=30)
        r.raise_for_status()
        return r.json()

    def list_books(self):
        url = f"{self.base}/BookStore/v1/Books"
        r = self.session.get(url, timeout=30)
        r.raise_for_status()
        return r.json()

    def add_books(self, user_id, token, isbns):
        url = f"{self.base}/BookStore/v1/Books"
        payload = {"userId": user_id, "collectionOfIsbns": [{"isbn": i} for i in isbns]}
        headers = {**self.headers, "Authorization": f"Bearer {token}"}
        r = self.session.post(url, json=payload, headers=headers, timeout=30)
        # this endpoint may return 201 or 200 depending on API behavior
        if r.status_code not in (200, 201):
            r.raise_for_status()
        return r.json()

    def get_user(self, user_id, token):
        url = f"{self.base}/Account/v1/User/{user_id}"
        headers = {**self.headers, "Authorization": f"Bearer {token}"}
        r = self.session.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        return r.json()
