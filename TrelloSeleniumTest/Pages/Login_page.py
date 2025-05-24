from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.ID, "username")
        self.continue_button = (By.ID, "login-submit")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.ID, "login-submit")

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
