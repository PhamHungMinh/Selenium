import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.reset_password_page import PasswordResetPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver  # Nhập hàm get_chrome_driver

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def setup():
    driver = get_chrome_driver()  # Sử dụng hàm get_chrome_driver để khởi tạo driver
    password_page = PasswordResetPage(driver)
    yield driver, password_page
    driver.quit()
# Test case 5 - Gửi yêu cầu quên mật khẩu
def test_Request_Password_Reset(setup):
    driver, password_page = setup
    logging.info("Bắt đầu kiểm tra: Khôi phục mật khẩu thành công")

    # Mở trang khôi phục mật khẩu và nhập email
    password_page.Open_Reset_Page() \
        .Enter_Email_Input("0306221443@caothang.edu.vn") \
        .Submit_Button_Click()

    # Chờ thông báo hiển thị và kiểm tra kết quả
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div[2]"))
    )
    actual_result = message_element.text.strip()
    expected_result = "We sent a recovery link to you at"

    logging.info(f"Actual result: '{actual_result}'")
    logging.info(f"Expected result: '{expected_result}'")

    # Kiểm tra kết quả
    assert actual_result == expected_result, f"❌ Expected: '{expected_result}' but got: '{actual_result}'"
    logging.info("✅ Test case PASS: Khôi phục mật khẩu thành công.")
