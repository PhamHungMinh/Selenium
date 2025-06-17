import time
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TrelloSeleniumTest.Pages.Register_page import RegisterPage
from TrelloSeleniumTest.Base.config import Signup_Url
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    driver = get_chrome_driver()  # Đã cấu hình để chạy qua Grid trong Chrome_Driver.py
    yield driver
    driver.quit()

# Test Case 2 - Đăng ký với tên không hợp lệ
def test_RegisterWithInvalidName(driver):
    register_page = RegisterPage(driver)
    register_page.Open_Page(Signup_Url)
    register_page.Fill_Email_Input("minhpham")
    register_page.Continue_Button_Click()
    error_message = register_page.Get_Error_Message()
    print(f"Thông báo lỗi: {error_message}")

    if "@" in error_message or "email" in error_message.lower():
        print("✅ Test case PASS: Hiển thị lỗi đúng khi nhập tên không hợp lệ")
        return True
    else:
        print("❌ Test case FAIL: Không hiển thị lỗi đúng khi nhập tên không hợp lệ")
        return False

# Test case 3 - Đăng ký với email đã đăng ký trước đó
def test_RegisterWithRegisteredEmail(driver):
    register_page = RegisterPage(driver)
    register_page.Open_Page(Signup_Url)
    register_page.Fill_Email_Input("0306221442@caothang.edu.vn")
    register_page.Continue_Button_Click()

    # Đợi cho đến khi URL thay đổi
    WebDriverWait(driver, 10).until(EC.url_contains("https://id.atlassian.com/login"))

    # Kiểm tra URL sau khi nhấn nút tiếp tục
    current_url = driver.current_url
    expected_domain = "https://id.atlassian.com/login"

    if expected_domain in current_url:
        print("✅ Test case PASS: Chuyển hướng đến trang đăng nhập khi email đã đăng ký")
        return True
    else:
        print("❌ Test case FAIL: Không chuyển hướng đến trang đăng nhập đúng khi email đã đăng ký")
        print("URL hiện tại:", current_url)  # In ra URL hiện tại để kiểm tra
        return False
