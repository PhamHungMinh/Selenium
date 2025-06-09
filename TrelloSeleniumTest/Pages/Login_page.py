from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage  # Cập nhật đúng đường dẫn base_page nếu cần

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi constructor của BasePage
        self.Email_Textbox = (By.ID, "username")
        self.Continue_Button = (By.ID, "login-submit")
        self.Password_Textbox = (By.ID, "password")
        self.Login_Button = (By.ID, "login-submit")

    def Open_Page(self, url):
        """Mở trang đăng nhập."""
        self.Driver.get(url)

    def Enter_Email(self, email):
        """Nhập địa chỉ email vào trường email."""
        self.Wait_And_Send_Keys(self.Email_Textbox, email)

    def Click_Continue(self):
        """Nhấn nút tiếp tục."""
        self.Wait_And_Click(self.Continue_Button)

    def Enter_Password(self, password):
        """Nhập mật khẩu vào trường mật khẩu."""
        self.Wait_And_Send_Keys(self.Password_Textbox, password)

    def Click_Login(self):
        """Nhấn nút đăng nhập."""
        self.Wait_And_Click(self.Login_Button)
