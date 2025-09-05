import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.demoqa_form_page import TextBoxPage

@pytest.fixture(scope="module")
def driver():
    options = Options()
    # Headless for CI
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_fill_textbox_success(driver):
    page = TextBoxPage(driver)
    page.open()
    page.fill_form("Maria Teste", "maria@example.com", "Rua A, 123", "Rua B, 456")
    assert "Maria Teste" in page.output_name()

