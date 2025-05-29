import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.reset_password_page import PasswordResetPage


@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--lang=vi")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    password_page = PasswordResetPage(driver)
    yield driver, password_page
    driver.quit()


def test_successful_password_reset(setup):
    driver, password_page = setup

    password_page.open_reset_page()\
                 .enter_email("nghiatrong4554@gmail.com")\
                 .click_submit()

    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/section/div[2]/div[2]"))
    )
    actual_result = message_element.text.strip()
    expected_result = "Chúng tôi đã gửi liên kết khôi phục cho bạn theo địa chỉ"

    print(f"Actual result: '{actual_result}'")
    print(f"Expected result: '{expected_result}'")

    assert actual_result == expected_result, f"❌ Expected: '{expected_result}' but got: '{actual_result}'"