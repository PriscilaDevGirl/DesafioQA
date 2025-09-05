import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://demoqa.com"
API_USER = os.getenv("DEMOQA_USERNAME", "test_user_demoqa")
API_PASS = os.getenv("DEMOQA_PASSWORD", "Test@12345")
