from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi constructor của BasePage
        self.Email_Textbox = (By.XPATH, "//input[@id='username-uid1' and @name='username' and @type='email']")
        self.Email_Textbox_Again = (By.XPATH, "//input[@data-testid='username' and @name='username' and @type='email']")
        self.Continue_Button = (By.ID, "login-submit")
        self.Password_Textbox = (By.ID, "password")
        self.Login_Button = (By.ID, "login-submit")
        self.Edit_Email = (By.XPATH, "(//span[@data-vc='icon-undefined' and contains(@class, 'css-snhnyn')])[1]")

    def Open_Page(self, url):
        """Mở trang đăng nhập."""
        self.driver.get(url)

    def Fill_Email(self, email):
        """Nhập địa chỉ email vào trường email."""
        self.Wait_And_Send_Keys(self.Email_Textbox, email)

    def Fill_Email_Again(self, email):
        """Nhập địa chỉ email vào trường email."""
        self.Wait_And_Send_Keys(self.Email_Textbox_Again, email)

    def Continue_Button_Click(self):
        """Nhấn nút tiếp tục."""
        self.Wait_And_Click(self.Continue_Button)

    def Fill_Password(self, password):
        """Nhập mật khẩu vào trường mật khẩu."""
        self.Wait_And_Send_Keys(self.Password_Textbox, password)

    def Login_Button_Click(self):
        """Nhấn nút đăng nhập."""
        self.Wait_And_Click(self.Login_Button)
    def Edit_Email_Click(self):
        self.Wait_And_Click(self.Edit_Email)

    def clear_email_field(self):
        email_field = self.driver.find_element(*self.Email_Textbox)
        email_field.clear()