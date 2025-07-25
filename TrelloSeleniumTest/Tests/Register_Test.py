import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Register_page import RegisterPage
from TrelloSeleniumTest.Base.config import Signup_Url
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Setup WebDriver
@pytest.fixture
def driver():
   options = webdriver.ChromeOptions()
   options.add_argument("--start-maximized")
   driver = webdriver.Chrome(options=options)
   yield driver
   driver.quit()

def run_tests(driver):
    # Test Case 2 - Đăng ký với tên không hợp lệ
    register_page = RegisterPage(driver)
    register_page.Open_Page(Signup_Url)
    register_page.Fill_Email_Input("minhpham")
    register_page.Continue_Button_Click()
    error_message = register_page.Get_Error_Message()
    print(f"Thông báo lỗi: {error_message}")

    if "@" in error_message or "email" in error_message.lower():
        print("✅ Test case PASS: Hiển thị lỗi đúng khi nhập tên không hợp lệ")
    else:
        print("❌ Test case FAIL: Không hiển thị lỗi đúng khi nhập tên không hợp lệ")

    # Test case 3 - Đăng ký với email đã đăng ký trước đó
    register_page.clear_email_field()
    register_page.Fill_Email_Input("0306221443@caothang.edu.vn")
    register_page.Continue_Button_Click()
    time.sleep(15)
    # Đợi cho đến khi URL thay đổi
    WebDriverWait(driver, 10).until(EC.url_contains("https://id.atlassian.com/login"))

    # Kiểm tra URL sau khi nhấn nút tiếp tục
    current_url = driver.current_url
    expected_domain = "https://id.atlassian.com/login"

    if expected_domain in current_url:
        print("✅ Test case PASS: Chuyển hướng đến trang đăng nhập khi email đã đăng ký")
    else:
        print("❌ Test case FAIL: Không chuyển hướng đến trang đăng nhập đúng khi email đã đăng ký")
        print("URL hiện tại:", current_url)  # In ra URL hiện tại để kiểm tra

# Gọi hàm run_tests trong pytest
def test_all_cases(driver):
    run_tests(driver)
