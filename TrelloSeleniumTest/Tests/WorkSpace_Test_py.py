import logging
import pytest
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.untils import login_to_atlassian, wait_for_element, navigate_to_trello

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
   driver = get_chrome_driver()
   yield driver
   driver.quit()

def wait_for_element1(driver, by, value, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

# Test case 29
def test_Limit_Member_WorkSpace(driver):
    login_to_atlassian(driver, "0306221443@caothang.edu.vn", "Nghia842004@")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Click_Member_Button()
    home_page.Click_Add_Member_Button()
    home_page.Fill_Email_Input_Members()

    # Chờ cho email thừa xuất hiện
    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.autocomplete-option.disabled")))
    except TimeoutException:
        logging.warning("Không tìm thấy email thừa trong thời gian chờ.")
        disabled_emails = []  # Nếu không tìm thấy email thừa, gán danh sách rỗng
    else:
        # Lấy tất cả các email bị thừa
        email_elements = driver.find_elements(By.CSS_SELECTOR, "div.autocomplete-option.disabled")
        disabled_emails = [email.get_attribute('title') for email in email_elements]  # Lấy title của email bị thừa

    # Chờ cho nút "Gửi lời mời" xuất hiện
    try:
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[span='Send invites']")))
    except TimeoutException:
        logging.error("Không tìm thấy nút 'Gửi lời mời' trong thời gian chờ.")
        assert False, "Test case failed: Nút 'Gửi lời mời' không xuất hiện."

    # Kiểm tra trạng thái của nút "Gửi lời mời"
    add_button = driver.find_element(By.XPATH,
                                     "//button[span='Send invites']")
    is_add_button_disabled = not add_button.is_enabled()  # Kiểm tra xem nút có bị vô hiệu hóa hay không

    logging.info(f"Nút 'Gửi lời mời' bị chặn: {is_add_button_disabled}, Email thừa: {disabled_emails}")

    # Điều kiện để test case pass
    if is_add_button_disabled and disabled_emails:
        logging.info("Nút 'Gửi lời mời' bị chặn và có email thừa: %s", disabled_emails)
        assert True, "Test case passed: Nút 'Gửi lời mời' bị chặn và có email thừa."
    else:
        if not is_add_button_disabled:
            logging.error("Nút 'Gửi lời mời' không bị chặn.")
            assert False, "Test case failed: Nút 'Gửi lời mời' không bị chặn."
        if not disabled_emails:
            logging.error("Không có email thừa.")
            assert False, "Test case failed: Không có email thừa."