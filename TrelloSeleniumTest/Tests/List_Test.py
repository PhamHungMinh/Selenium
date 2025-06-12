import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Pages.Quan_ly_List import QuanLyList
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from selenium.webdriver.common.action_chains import ActionChains
from TrelloSeleniumTest.Until.utils import *

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()

# Hàm để đếm số lượng danh sách hiện có
def count_lists(driver):
    lists_xpath = "//ol[@data-testid='lists']/li"
    lists = driver.find_elements(By.XPATH, lists_xpath)
    return len(lists)


# Test case 13
def test_Create_List_With_Valid_Name(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Click_Enter_Board()

    QLListPage = QuanLyList(driver)
    QLListPage.Create_List_Click()
    QLListPage.Fill_List_Name_Input()
    QLListPage.Button_Create_List_WithName_Click()

    wait_for_element(driver, By.XPATH, QLListPage.Wait_For_Board_To_Display)
    try:
        list_element = driver.find_element(By.XPATH, "//button[text()='List_Test_1']")
        assert list_element.is_displayed(), "Danh sách 'List_Test_1' không được tìm thấy."
        print("Danh sách 'List_Test_1' đã được tạo và tìm thấy.")
    except Exception as e:
        driver.fail("Không thể tìm thấy danh sách 'List_Test_1': " + str(e))


# Test case 14
def test_Create_List_With_Same_Name(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Click_Enter_Board()

    QLListPage = QuanLyList(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.Fill_Same_Name_List_Input()
    QLListPage.Button_Create_List_WithName_Click()

    wait_for_element(driver, By.XPATH, QLListPage.Wait_For_Board_To_Display)
    # Tìm tất cả các danh sách có tên "List_Test_1"
    list_elements = driver.find_elements(By.XPATH, "//button[text()='List_Test_1']")
    count = len(list_elements)

    # Assert xem có đúng 2 danh sách không
    assert count == 2, f"Số lượng danh sách 'List_Test_1' không phải là 2, mà là {count}."

    # In ra thông báo nếu có 2 danh sách
    print("Có 2 danh sách 'List_Test_1' được tìm thấy.")


# Test case 15
def test_Create_List_With_Long_Name(driver):
    # Đăng nhập vào Atlassian
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Click_Enter_Board()

    QLListPage = QuanLyList(driver)  # Đã thay đổi tên
    QLListPage.Create_List_Click()
    QLListPage.Fill_Long_Name_List()  # Giả định rằng tên dài đã được điền
    QLListPage.Button_Create_List_WithName_Click()
    # Kiểm tra độ dài tên danh sách bằng cách sử dụng phương thức từ lớp Quan_Ly_List
    textarea = driver.find_element(By.XPATH,
                                   "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][2]//textarea[@data-testid='list-name-textarea']")
    length = len(textarea.get_attribute("value"))

    # Kiểm tra độ dài tên danh sách
    expected_length = 512
    assert length == expected_length, f"Test case FAIL: Độ dài tên danh sách là {length}, khác 512."
    print("Test case PASS: Đã tạo thành công danh sách với tên dài.")

# Test case 17
def test_Archive_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Click_Enter_Board()

    QLListPage = QuanLyList(driver)
    QLListPage.Click_Menu_List()
    QLListPage.Archive_List_Button_Click()

    # Kiểm tra xem thông báo có hiển thị không
    alert_visible = QLListPage.Check_Alert_Message()

    wait_for_element(driver, By.XPATH, QLListPage.Wait_For_Board_To_Display)

    # Đếm số lượng danh sách có tên "List_Test_1"
    list_elements = driver.find_elements(By.XPATH, "//button[text()='List_Test_1']")
    list_count = len(list_elements)

    # Assert điều kiện: thông báo hiển thị và số lượng danh sách là 1
    assert alert_visible, "Test case FAIL: Thông báo không xuất hiện sau khi lưu trữ danh sách."
    assert list_count == 1, f"Test case FAIL: Số lượng danh sách 'List_Test_1' là {list_count}, nhưng mong đợi là 1."

    print("Test case PASS: Thông báo đã xuất hiện và chỉ có 1 danh sách 'List_Test_1'.")

def test_xpath(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    alassian = HomeAtlassianPage(driver)
    alassian.Menu_Click()
    alassian.Trello_Click()

