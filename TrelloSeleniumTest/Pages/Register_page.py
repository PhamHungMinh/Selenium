from selenium.webdriver.common.by import By

#Test Case 2
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.ID, "email")
        self.continue_button = (By.ID, "signup-submit")


    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
