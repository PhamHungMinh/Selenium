import time
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Pages.Quan_ly_List import Quan_Ly_List
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Quan_Ly_Card import QuanLyCard

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Danh sách các link cần kiểm tra
LINK_TEXTS = [
    "Biểu phí",
    "Ứng dụng",
    "Blog",
    "Chính sách Bảo mật",
    "Thông báo thu thập thông tin",
    "Trợ giúp",
    "Nhà phát triển",
    "Pháp lý",
    "Thuộc tính"
]

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.quit()

def wait_for_element(driver, by, value):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))

def login_to_atlassian(driver, email, password):
    login_page = LoginPage(driver)
    driver.get("https://id.atlassian.com/login")

    wait_for_element(driver, By.ID, "username")
    login_page.enter_email(email)
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password(password)
    login_page.click_login()

def navigate_to_trello(driver):
    atlassian_page = HomeAtlassianPage(driver)
    home_page = HomeTrelloPage(driver)

    atlassian_page.Menu_click()
    atlassian_page.Trello_click()
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
    home_page.click_trello_login_button()

#Broken Link Test - Test Case 30
@pytest.mark.brokenlink
def test_footer_links_broken(driver):
    broken_links = []
    link_statuses = []  # Danh sách để lưu trạng thái link

    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Thong_Tin_Click()
    home_page.More_Click()

    # Kiểm tra từng link trong footer
    for link_text in LINK_TEXTS:
        url = home_page.get_link_url(link_text)
        status = home_page.get_link_status(url)

        # Ghi lại trạng thái link
        link_statuses.append(f"{link_text}: {url} - Status: {status}")

        # Kiểm tra nếu status >= 400 hoặc có lỗi
        if isinstance(status, int) and status >= 400:
            broken_links.append(f"{link_text} ({url}): HTTP {status}")
            logging.error(f"Link broken: {link_text} ({url}): HTTP {status}")
        elif isinstance(status, str) and "Error" in status:
            broken_links.append(f"{link_text} ({url}): {status}")
            logging.error(f"Link broken: {link_text} ({url}): {status}")

    # Fail test nếu có link broken
    if broken_links:
        error_message = "\n".join([f"❌ {link}" for link in broken_links])
        logging.critical(f"Found {len(broken_links)} broken links:\n{error_message}")
        pytest.fail(f"Found {len(broken_links)} broken links:\n{error_message}")

    # In ra thông tin link và trạng thái khi test case pass
    print("\n✅ Tất cả link trong footer đều hoạt động tốt!")
    print("Thông tin các link:")
    for entry in link_statuses:
        print(entry)

#Test case 31
@pytest.mark.brokenlink
def test_open_links_in_new_tabs(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Thong_Tin_Click()
    home_page.More_Click()

    # Mở từng link trong một tab mới và kiểm tra trạng thái
    for link_text in LINK_TEXTS:
        url = home_page.get_link_url(link_text)
        driver.execute_script(f"window.open('{url}', '_blank');")  # Mở link trong tab mới

        # Chuyển đến tab mới
        driver.switch_to.window(driver.window_handles[-1])  # Chuyển đến tab mới
        time.sleep(2)  # Đợi một chút để trang tải

        status = home_page.get_link_status(url)  # Kiểm tra trạng thái của link
        print(f"{link_text}: {url} - Status: {status}")

        driver.close()  # Đóng tab mới
        driver.switch_to.window(driver.window_handles[0])  # Quay lại tab gốc