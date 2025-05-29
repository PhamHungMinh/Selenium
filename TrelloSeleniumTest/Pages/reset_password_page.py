from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PasswordResetPage:
    # Locators
    EMAIL_FIELD = (By.ID, "email")
    SUBMIT_BUTTON = (By.ID, "reset-password-email-submit")

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def open_reset_page(self):
        self.driver.get("https://id.atlassian.com/login/resetpassword?application=trello")
        return self

    def enter_email(self, email):
        email_field = self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)
        return self

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        return self