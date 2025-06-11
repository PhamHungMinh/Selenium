from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage

class PasswordResetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi hàm khởi tạo của lớp cha
        self.driver = driver 
        self.Email_Input = (By.ID, "email")
        self.Submit_Button = (By.ID, "reset-password-email-submit")

    def Open_Reset_Page(self):
        self.driver.get("https://id.atlassian.com/login/resetpassword?application=trello")
        return self

    def Enter_Email_Input(self, email):
        email_field = self.Wait_For_Element(self.Email_Input)
        email_field.clear()
        email_field.send_keys(email)
        return self

    def Submit_Button_Click(self):
        self.Wait_And_Click(self.Submit_Button)
        return self
