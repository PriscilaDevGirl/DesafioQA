from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.demoqa_form_page import TextBoxPage

def before_all(context):
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=opts)

def after_all(context):
    context.driver.quit()

@given("que estou na página de Text Box")
def step_impl(context):
    context.page = TextBoxPage(context.driver)
    context.page.open()

@when("eu preencho o formulário corretamente")
def step_impl(context):
    context.page.fill_form("Maria BDD", "maria@example.com", "Rua C, 123", "Rua D, 456")

@then("vejo meu nome no resultado")
def step_impl(context):
    assert "Maria BDD" in context.page.output_name()
