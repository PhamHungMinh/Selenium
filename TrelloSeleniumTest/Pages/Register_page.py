from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.ID, "email")
        self.continue_button = (By.ID, "signup-submit")

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        # Chờ cho ô nhập email có thể tương tác
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_textbox)
        )
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        # Chờ cho nút tiếp tục có thể tương tác
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        self.driver.find_element(*self.continue_button).click()

    def get_error_message(self):
        # Chờ cho ô nhập email có thể tương tác
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_textbox)
        )
        return self.driver.execute_script("return arguments[0].validationMessage;", email_input)

    def get_error_message2(self):
        # Cập nhật selector để lấy thông báo lỗi
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/span"  # Cập nhật selector cho thông báo lỗi
            ))
        )
        return element.text
