from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi hàm khởi tạo của lớp cha
        self.driver = driver
        self.Email_Textbox_Input = (By.ID, "email")
        self.Continue_Button = (By.ID, "signup-submit")

    def Open_Page(self, url):
        self.driver.get(url)

    def Fill_Email_Input(self, email):
        self.Wait_For_Element(self.Email_Textbox_Input).send_keys(email)

    def Continue_Button_Click(self):
        self.Wait_And_Click(self.Continue_Button)

    def Get_Error_Message(self):
        # Chờ cho ô nhập email có thể tương tác
        email_input = self.Wait_For_Element(self.Email_Textbox_Input)
        return self.driver.execute_script("return arguments[0].validationMessage;", email_input)

    # Test case 3 - Đăng ký với email đã đăng ký trước đó
    def Get_Error_Message_TC3(self):
        # Cập nhật selector để lấy thông báo lỗi
        element = self.Wait_For_Element((
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/span"
        ))
        return element.text
    def clear_email_field(self):
        email_field = self.driver.find_element(*self.Email_Textbox_Input)
        email_field.clear()