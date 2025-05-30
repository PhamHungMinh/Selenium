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

# Global variable for XPATHs
XPATH_CREATE_LIST = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/ul/li[2]/a/div"
XPATH_BUTTON_CREATE_BOARD = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/a/div"


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

# Hàm để đếm số lượng danh sách hiện có
def count_lists(driver):
    lists_xpath = "//ol[@data-testid='lists']/li"
    lists = driver.find_elements(By.XPATH, lists_xpath)
    return len(lists)


# Test case 14
def test_Tao_List_Voi_Ten_Hop_Le(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)

    HomePage.Into_Board_Click()
    QLListPage = Quan_Ly_List(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.fill_list_name_input()
    QLListPage.Button_CreateList_WithName_Click()

    time.sleep(5)  # Chờ cho danh sách hiển thị

    # Đếm số lượng danh sách hiện có
    list_count = count_lists(driver)
    expected_count = 2  # 1 danh sách mặc định + 1 danh sách mới

    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."
    print("Test case PASS: Đã tạo thành công danh sách với tên hợp lệ.")


# Test case 15
def test_Tao_List_Voi_Trung(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)

    time.sleep(2)
    HomePage.Into_Board_Click()
    QLListPage = Quan_Ly_List(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.fill_list_ten_trung_input()
    QLListPage.Button_CreateList_WithName_Click()

    time.sleep(5)  # Chờ cho danh sách hiển thị

    # Đếm số lượng danh sách hiện có
    list_count = count_lists(driver)
    expected_count = 3  # 1 danh sách mặc định + 2 danh sách mới

    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."
    print("Test case PASS: Đã tạo thành công danh sách với tên trùng.")


# Test case 16
def test_Tao_List_Voi_Dai(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)

    time.sleep(2)
    HomePage.Into_Board_Click()
    QLListPage = Quan_Ly_List(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.fill_list_ten_dai()
    QLListPage.Button_CreateList_WithName_Click()

    time.sleep(5)  # Chờ cho danh sách hiển thị

    # Đếm số lượng danh sách hiện có
    list_count = count_lists(driver)
    expected_count = 4  # 1 danh sách mặc định + 3 danh sách mới

    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."
    print("Test case PASS: Đã tạo thành công danh sách với tên dài.")


def test_Archive_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)

    time.sleep(2)
    HomePage.Into_Board_Click()
    QLListPage = Quan_Ly_List(driver)
    QLListPage.click_menu_list()
    QLListPage.click_archive_list()
    time.sleep(2)
    alert_visible = QLListPage.check_alert_message()
    time.sleep(1)
    # Reload lại trang
    driver.refresh()  # Reload trang hiện tại
    time.sleep(5)
    expected_count = 3
    # Đếm số lượng danh sách hiện có sau khi reload
    list_count = count_lists(driver)