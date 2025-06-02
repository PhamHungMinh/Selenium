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
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()


def wait_for_element(driver, by, value):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))


def login_to_atlassian(driver, email, password):
    Login_Page = LoginPage(driver)
    driver.get("https://id.atlassian.com/login")

    wait_for_element(driver, By.ID, "username")
    Login_Page.enter_email(email)
    Login_Page.click_continue()

    wait_for_element(driver, By.ID, "password")
    Login_Page.enter_password(password)
    Login_Page.click_login()


def navigate_to_trello(driver):
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)

    AtlassianPage.Menu_click()
    AtlassianPage.Trello_click()
    driver.get("https://trello.com/u/ngotrongnghia8424/boards")

    # Lưu ID của cửa sổ gốc
    original_window = driver.current_window_handle

    # Kiểm tra và đóng các cửa sổ khác nếu có
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            driver.close()  # Đóng cửa sổ mới
            driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc

    # Đảm bảo chỉ có một cửa sổ mở
    assert len(driver.window_handles) == 1
    HomePage.click_trello_login_button()

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
