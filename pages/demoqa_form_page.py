from selenium.webdriver.common.by import By

class TextBoxPage:
    URL = "https://demoqa.com/text-box"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    @property
    def full_name(self):
        return self.driver.find_element(By.ID, "userName")

    @property
    def email(self):
        return self.driver.find_element(By.ID, "userEmail")

    @property
    def current_address(self):
        return self.driver.find_element(By.ID, "currentAddress")

    @property
    def permanent_address(self):
        return self.driver.find_element(By.ID, "permanentAddress")

    @property
    def submit(self):
        return self.driver.find_element(By.ID, "submit")

    def fill_form(self, name, email, curr_addr, perm_addr):
        self.full_name.clear(); self.full_name.send_keys(name)
        self.email.clear(); self.email.send_keys(email)
        self.current_address.clear(); self.current_address.send_keys(curr_addr)
        self.permanent_address.clear(); self.permanent_address.send_keys(perm_addr)
        self.submit.click()

    def output_name(self):
        return self.driver.find_element(By.ID, "name").text
