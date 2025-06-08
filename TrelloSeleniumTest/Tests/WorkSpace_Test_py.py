import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Pages.Quan_ly_List import Quan_Ly_List
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from utils import wait_for_element, login_to_atlassian, navigate_to_trello

from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()


# Test case 29
def test_Gioi_Han_WorkSpace(driver):
    login_to_atlassian(driver, "0306221443@caothang.edu.vn", "Nghia842004@")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)

    HomePage.ThanhVien_Button_Click()
    HomePage.Add_Email_Button_Click()
    HomePage.Fill_Email_Input_Click()

    # Kiểm tra trạng thái của nút "Gửi lời mời"
    add_button = driver.find_element(By.XPATH,
                                     "//button[contains(@class, 'DXtVhm7hhVXHuw') and contains(span/text(), 'Send invites')]")
    is_add_button_disabled = add_button.get_attribute("disabled") is not None

    # Kiểm tra sự hiện diện của email thừa với class 'disabled'
    email_elements = driver.find_elements(By.CSS_SELECTOR, "div.autocomplete-option.disabled")
    has_disabled_email = len(email_elements) > 0

    # Điều kiện để test case pass
    if is_add_button_disabled and has_disabled_email:
        assert True, "Test case passed: Nút 'Gửi lời mời' bị chặn và có email thừa."
    else:
        assert False, "Test case failed: Điều kiện không thỏa mãn."
