import time
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Base.config import Login_Url, Email, Password, Signup_Url, Home_Url
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from Selenium.TrelloSeleniumTest.Until.utils import wait_for_element

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    driver = get_chrome_driver()  # Đã cấu hình để chạy qua Grid trong Chrome_Driver.py
    yield driver
    driver.quit()

# Test case 1 - Đăng nhập với tài khoản chưa đăng ký
def test_Login_With_Unregistered_Account(driver):
    login_page = LoginPage(driver)
    login_page.Open_Page(Login_Url)

    email = "phamhungminh1805@gmail.com"
    login_page.Fill_Email(email)
    login_page.Continue_Button_Click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://id.atlassian.com/signup?email=phamhungminh1805%40gmail.com&redirectedFrom=login")
    )
    current_url = driver.current_url
    expected_url = "https://id.atlassian.com/signup?email=phamhungminh1805%40gmail.com&redirectedFrom=login"

    if current_url.startswith(expected_url):
        print("✅ Test case PASS: Đã chuyển hướng đến trang đăng ký")
    else:
        print(f"❌ Test case FAIL: Expected URL to start with: {expected_url}, but got: {current_url}")

    time.sleep(3)

# Test case 4 - Đăng nhập với mật khẩu sai
def test_Login_With_Incorrect_Password(driver):
    login_page = LoginPage(driver)
    login_page.Open_Page(Login_Url)
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()

    login_page.Fill_Password("TestPassWord")
    login_page.Login_Button_Click()

    error_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div"
    wait_for_element(driver, By.XPATH, error_xpath)

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, error_xpath))
        )
        assert error_message.is_displayed(), "Thông báo lỗi không hiển thị."
        print("✅ Test case PASS: Thông báo lỗi đã hiển thị.")
    except Exception as e:
        print("❌ Test case FAIL: Thông báo lỗi không hiển thị.")
        assert False, "Test case FAIL: Thông báo lỗi không hiển thị."

# Test case 6 - Đăng nhập thành công
def test_Login_Success(driver):
    login_page = LoginPage(driver)
    login_page.Open_Page(Login_Url)
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    WebDriverWait(driver, 10).until(EC.url_contains(Home_Url))

    current_url = driver.current_url
    expected_url = Home_Url

    if current_url.startswith(expected_url):
        print("✅ Test case PASS: Đăng nhập thành công và chuyển hướng đến trang chủ")
    else:
        print(f"❌ Test case FAIL: Expected URL to start with: {expected_url}, but got: {current_url}")
