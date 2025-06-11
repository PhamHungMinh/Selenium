import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Email, Password, Signup_Url, Home_Url

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()

def wait_for_element(driver, by, value):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))

#Test case 1 - Đăng nhập với tài khoản chưa đăng ký
def test_login_voi_TaiKhoan_chua_dang_ky(driver):
    Login_Page = LoginPage(driver)
    # Mở trang đăng nhập
    Login_Page.Open_Page(Login_Url)

    # Nhập email chưa đăng ký và nhấn tiếp tục
    email = "nghiatrong4114@gmail.com"
    Login_Page.Fill_Email(email)
    Login_Page.Continue_Button_Click()

    # Đợi cho trang chuyển hướng
    WebDriverWait(driver, 10).until(
        EC.url_to_be(Signup_Url)
    )

    # Kiểm tra URL hiện tại
    current_url = driver.current_url
    expected_url = Signup_Url

    if current_url.startswith(expected_url):
        print("Test case PASS: Đã chuyển hướng đến trang đăng ký")
    else:
        print(f"Test case FAIL: Expected URL to start with: {expected_url}, but got: {current_url}")

# Test case 4 - Đăng nhập với mật khẩu sai
def test_login_voi_mat_khau_sai(driver):
    Login_Page = LoginPage(driver)
    # Mở trang đăng nhập
    Login_Page.Open_Page(Login_Url)
    # Nhập email và nhấn tiếp tục
    Login_Page.Fill_Email(Email)
    Login_Page.Continue_Button_Click()
    # Nhập mật khẩu sai và nhấn đăng nhập
    Login_Page.Fill_Password("TestPassWord")
    Login_Page.Login_Button_Click()

    # Kiểm tra xem thông báo lỗi có hiển thị không
    error_xpath = "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div"
    wait_for_element(driver, By.XPATH, error_xpath)
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, error_xpath))
        )
        assert error_message.is_displayed(), "Thông báo lỗi không hiển thị."
        print("Test case passed: Thông báo lỗi đã hiển thị.")
    except Exception as e:
        print("Test case failed: Thông báo lỗi không hiển thị.")
        assert False, "Test case failed: Thông báo lỗi không hiển thị."

#Test case 6 - Đăng nhập thành công
def test_login_success(driver):
    Login_Page = LoginPage(driver)
    Login_Page.Open_Page(Login_Url)
    Login_Page.Fill_Email(Email)
    Login_Page.Continue_Button_Click()
    Login_Page.Fill_Password(Password)
    Login_Page.Login_Button_Click()

    # Kiểm tra URL sau khi đăng nhập
    WebDriverWait(driver, 10).until(EC.url_contains(Home_Url))

    current_url = driver.current_url
    expected_url = Home_Url

    if current_url.startswith(expected_url):
        print("Test case PASS: Đăng nhập thành công và chuyển hướng đến trang chủ")
    else:
        print(f"Test case FAIL: Expected URL to start with: {expected_url}, but got: {current_url}")
