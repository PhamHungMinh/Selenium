import time
import pytest
import sys
import os
from TrelloSeleniumTest.Pages.reset_password_page import PasswordResetPage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from TrelloSeleniumTest.Pages.reset_password_page import PasswordResetPage


class TestPasswordReset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.password_page = PasswordResetPage(self.driver)
        self.driver.maximize_window()
        yield
        self.driver.quit()

#Test Case 5 - Gửi yêu cầu quên mật khẩu
    def test_successful_password_reset(self):
        (self.password_page.open_reset_page()
         .enter_email("nghiatrong4554@gmail.com")
         .click_submit())
        time.sleep(5)

