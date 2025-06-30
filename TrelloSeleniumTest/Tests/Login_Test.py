import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Base.config import Login_Url, Email, Password, Signup_Url, Home_Url
from TrelloSeleniumTest.Until.untils import wait_for_element

error_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div"

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
   driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
   yield driver
   driver.quit()

def run_tests(driver):
    # Test case 1 - Đăng nhập với tài khoản chưa đăng ký
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

    assert current_url.startswith(expected_url), f"Expected URL to start with: {expected_url}, but got: {current_url}"
    print("Test case 1 PASS: Đã chuyển hướng đến trang đăng ký")

    # Test case 4 - Đăng nhập với mật khẩu sai
    driver.get(Login_Url)  # Đảm bảo chỉ có 1 tab được mở và quay lại trang đăng nhập
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()

    login_page.Fill_Password("TestPassWord")
    login_page.Login_Button_Click()

    wait_for_element(driver, By.XPATH, error_xpath)

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, error_xpath))
    )

    assert error_message.is_displayed(), "Thông báo lỗi không hiển thị."
    print("Test case 4 PASS: Thông báo lỗi đã hiển thị.")

    # Test case 6 - Đăng nhập thành công
    login_page.Edit_Email_Click()
    email_field = login_page.Wait_For_Element(login_page.Email_Textbox)
    login_page.clear_email_field()
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    WebDriverWait(driver, 10).until(EC.url_contains(Home_Url))

    current_url = driver.current_url
    expected_url = Home_Url

    assert current_url.startswith(expected_url), f"Expected URL to start with: {expected_url}, but got: {current_url}"
    print("Test case 6 PASS: Chuyển sang trang chủ của Atlassian")

def test_all_cases(driver):
    run_tests(driver)
