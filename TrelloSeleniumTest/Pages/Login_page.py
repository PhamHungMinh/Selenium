from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # Chờ cho trường email hiển thị và sau đó nhập email
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_textbox))
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        # Chờ cho nút tiếp tục hiển thị và sau đó nhấn
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.continue_button))
        self.driver.find_element(*self.continue_button).click()

    def enter_password(self, password):
        # Chờ cho trường mật khẩu hiển thị và sau đó nhập mật khẩu
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_textbox))
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        # Chờ cho nút đăng nhập hiển thị và sau đó nhấn
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button))
        self.driver.find_element(*self.login_button).click()
