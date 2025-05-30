import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Register_page import RegisterPage


@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()

#Test Case 2 - Đăng ký với tên không hợp lệ
def test_register_voi_ten_khong_hop_le(driver):
    register_page = RegisterPage(driver)
    register_page.open_page("https://id.atlassian.com/signup")
    time.sleep(2)
    register_page.enter_email("minhpham")
    register_page.click_continue()

    time.sleep(2)  # đợi native tooltip hiển thị (dù không bắt buộc)

    error_message = register_page.get_error_message()
    print(f"Lỗi hiển thị: {error_message}")

    assert "@" in error_message or "email" in error_message.lower()


#Test case 3 - Đăng ký với email đã đăng ký trước đó
def test_register_voi_email_da_dang_ky(driver):
        register_page = RegisterPage(driver)
        register_page.open_page("https://id.atlassian.com/signup")
        register_page.enter_email("ngotrongnghia8424@gmail.com")
        register_page.click_continue()
        time.sleep(10)

        error_message2 = register_page.get_error_message2()
        print("Thông báo lỗi thực tế:", error_message2)

        expected_vn = "bạn đã có một tài khoản"
        expected_en = "you've already got an account"

        print("Thông báo kỳ vọng (VN):", expected_vn)
        print("Thông báo kỳ vọng (EN):", expected_en)

        assert expected_vn in error_message2.lower() or expected_en in error_message2.lower(), \
            "Thông báo lỗi không khớp với kỳ vọng bằng tiếng Việt hoặc tiếng Anh."