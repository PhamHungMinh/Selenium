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

    wait_for_element(driver, By.XPATH, QLListPage.Cho_Bang_Hien_Thi)

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
    HomePage.Into_Board_Click()

    QLListPage = Quan_Ly_List(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.fill_list_ten_trung_input()
    QLListPage.Button_CreateList_WithName_Click()

    wait_for_element(driver, By.XPATH, QLListPage.Cho_Bang_Hien_Thi)

    # Đếm số lượng danh sách hiện có
    list_count = count_lists(driver)
    expected_count = 3  # 1 danh sách mặc định + 2 danh sách mới

    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."
    print("Test case PASS: Đã tạo thành công danh sách với tên trùng.")


# Test case 16
def test_Tao_List_Voi_Dai(driver):
    # Đăng nhập vào Atlassian
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Into_Board_Click()

    QLListPage = Quan_Ly_List(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.fill_list_ten_dai()  # Giả định rằng tên dài đã được điền
    QLListPage.Button_CreateList_WithName_Click()

    #wait_for_element(driver, By.XPATH, QLListPage.textarea_xpath)
    # Đếm số lượng danh sách hiện có
    list_count = count_lists(driver)
    expected_count = 4  # 1 danh sách mặc định + 3 danh sách mới

    # Kiểm tra số lượng danh sách
    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."

    # Kiểm tra độ dài tên danh sách bằng cách sử dụng phương thức từ lớp Quan_Ly_List
    textarea = driver.find_element(By.XPATH, QLListPage.textarea_xpath)
    length = len(textarea.text)

    # Kiểm tra độ dài tên danh sách
    expected_length = 512

    if length < expected_length:
        assert False, f"Test case FAIL: Độ dài tên danh sách là {length}, nhỏ hơn 512."
    elif length > expected_length:
        assert False, f"Test case FAIL: Độ dài tên danh sách là {length}, lớn hơn 512."
    else:
        print("Tên danh sách có độ dài chính xác là 512 ký tự.")

    print("Test case PASS: Đã tạo thành công danh sách với tên dài.")

# Test case 18
def test_Archive_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Into_Board_Click()

    QLListPage = Quan_Ly_List(driver)
    QLListPage.click_menu_list()
    QLListPage.click_archive_list()

    #wait_for_element(driver, By.XPATH, QLListPage.alert_xpath)
    alert_visible = QLListPage.check_alert_message()

    # Reload lại trang
    driver.refresh()  # Reload trang hiện tại
    wait_for_element(driver, By.XPATH, QLListPage.Cho_Bang_Hien_Thi)

    # Đếm số lượng danh sách hiện có sau khi reload
    list_count = count_lists(driver)
    expected_count = 3  # Giả định rằng có 3 danh sách còn lại sau khi lưu trữ

    # Kiểm tra cả hai điều kiện
    assert list_count == expected_count, f"Test case FAIL: Số lượng danh sách hiện có là {list_count}, nhưng mong đợi {expected_count}."
    assert alert_visible, "Test case FAIL: Thông báo không xuất hiện sau khi lưu trữ danh sách."

    print("Test case PASS: Đã lưu trữ danh sách thành công, thông báo đã xuất hiện và số lượng danh sách đúng.")

#Test case 17
def test_Drag_List_ViTri_HopLe(driver):
    # Đăng nhập vào Atlassian
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Into_Board_Click()

    QLListPage = Quan_Ly_List(driver)
    wait_for_element(driver, By.XPATH, QLListPage.Cho_Bang_Hien_Thi)

    actions = ActionChains(driver)
    list_1 = driver.find_element(By.XPATH, QLListPage.List_Test_1_XPATH)
    list_3 = driver.find_element(By.XPATH, QLListPage.Drop_XPATH)
    actions.drag_and_drop(list_1, list_3).perform()

    wait_for_element(driver, By.XPATH, QLListPage.Cho_Bang_Hien_Thi)

    time.sleep(10)
