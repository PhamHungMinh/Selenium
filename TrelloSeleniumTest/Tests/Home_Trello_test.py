import pytest
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()  # Đóng trình duyệt sau khi kiểm thử

def wait_for_element(driver, by, value):
    """Hàm đợi cho một phần tử trở nên hiển thị và có thể nhấp được trong tối đa 10 giây."""
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))

def test_Create_Board_voi_ten_hop_le(driver):
    Login_Page = LoginPage(driver)
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)

    # Mở trang đăng nhập
    Login_Page.open_page("https://id.atlassian.com/login")

    # Đợi cho phần tử email hiển thị và nhập email
    wait_for_element(driver, By.ID, "username")  # ID cho trường email
    Login_Page.enter_email("ngotrongnghia8424@gmail.com")
    Login_Page.click_continue()

    # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
    wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
    Login_Page.enter_password("khongcomatkhau4654")
    Login_Page.click_login()

    AtlassianPage.Menu_click()
    AtlassianPage.Trello_click()

    # Mở URL để tạo board mới
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
    # Đợi cho nút tạo board hiển thị và nhấp vào
    HomePage.click_trello_login_button()

    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")  # XPath cho nút tạo board
    HomePage.Create_Board_Click()
    HomePage.click_trello_create_board_button()
    HomePage.fill_board_name_input()
    time.sleep(2)
    HomePage.create_board_with_name()
    time.sleep(10)

