import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.reset_password_page import PasswordResetPage

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--lang=vi")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    password_page = PasswordResetPage(driver)
    yield driver, password_page
    driver.quit()

def test_Successful_Password_Reset(setup):
    driver, password_page = setup
    logging.info("Bắt đầu kiểm tra: Khôi phục mật khẩu thành công")

    # Mở trang khôi phục mật khẩu và nhập email
    password_page.Open_Reset_Page() \
        .Enter_Email_Input("nghiatrong4554@gmail.com") \
        .Submit_Button_Click()

    # Chờ thông báo hiển thị và kiểm tra kết quả
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div[2]"))
    )
    actual_result = message_element.text.strip()
    expected_result = "Chúng tôi đã gửi liên kết khôi phục cho bạn theo địa chỉ"

    logging.info(f"Actual result: '{actual_result}'")
    logging.info(f"Expected result: '{expected_result}'")

    # Kiểm tra kết quả
    assert actual_result == expected_result, f"❌ Expected: '{expected_result}' but got: '{actual_result}'"
    logging.info("✅ Test case PASS: Khôi phục mật khẩu thành công.")
