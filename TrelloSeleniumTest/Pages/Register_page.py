from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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

    def get_error_message(self):
        email_input = self.driver.find_element(By.ID, "email")  # hoặc selector đúng với ô email
        return self.driver.execute_script("return arguments[0].validationMessage;", email_input)

    def get_error_message2(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/span/div"
            ))
        )
        return element.text