import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Pages.Quan_ly_List import QuanLyList
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.utils import *

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
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
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()


    ql_list_page = QuanLyList(driver)
    ql_list_page.Create_List_Click()
    ql_list_page.Fill_List_Name_Input()
    ql_list_page.Button_Create_List_WithName_Click()


    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)
    try:
        list_element = driver.find_element(By.XPATH, "//button[text()='List_Test_1']")
        assert list_element.is_displayed(), "Danh sách 'List_Test_1' không được tìm thấy."
        logging.info("Danh sách 'List_Test_1' đã được tạo và tìm thấy.")
    except Exception as e:
        pytest.fail("Không thể tìm thấy danh sách 'List_Test_1': " + str(e))


# Test case 14
def test_Create_List_With_Same_Name(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")


    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()


    ql_list_page = QuanLyList(driver)
    ql_list_page.Create_List_Click()
    ql_list_page.Fill_Same_Name_List_Input()
    ql_list_page.Button_Create_List_WithName_Click()


    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)
    # Tìm tất cả các danh sách có tên "List_Test_1"
    list_elements = driver.find_elements(By.XPATH, "//button[text()='List_Test_1']")
    count = len(list_elements)


    # Assert xem có đúng 2 danh sách không
    assert count == 2, f"Số lượng danh sách 'List_Test_1' không phải là 2, mà là {count}."
    logging.info("Có 2 danh sách 'List_Test_1' được tìm thấy.")


# Test case 15
def test_Create_List_With_Long_Name(driver):
    # Đăng nhập vào Atlassian
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")


    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()


    ql_list_page = QuanLyList(driver)
    ql_list_page.Create_List_Click()
    ql_list_page.Fill_Long_Name_List()  # Giả định rằng tên dài đã được điền
    ql_list_page.Button_Create_List_WithName_Click()


    # Kiểm tra độ dài tên danh sách bằng cách sử dụng phương thức từ lớp Quan_Ly_List
    textarea = driver.find_element(By.XPATH,
                                   "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][4]//textarea[@data-testid='list-name-textarea']")
    length = len(textarea.get_attribute("value"))


    # Kiểm tra độ dài tên danh sách
    expected_length = 512
    assert length == expected_length, f"Test case FAIL: Độ dài tên danh sách là {length}, khác 512."
    logging.info("Test case PASS: Đã tạo thành công danh sách với tên dài.")


# Test case 17
def test_Archive_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")


    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()


    ql_list_page = QuanLyList(driver)
    ql_list_page.Click_Menu_List()
    ql_list_page.Archive_List_Button_Click()


    # Kiểm tra xem thông báo có hiển thị không
    alert_visible = ql_list_page.Check_Alert_Message()


    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)


    # Đếm số lượng danh sách có tên "List_Test_1"
    list_elements = driver.find_elements(By.XPATH, "//button[text()='List_Test_1']")
    list_count = len(list_elements)


    # Assert điều kiện: thông báo hiển thị và số lượng danh sách là 1
    assert alert_visible, "Test case FAIL: Thông báo không xuất hiện sau khi lưu trữ danh sách."
    assert list_count == 1, f"Test case FAIL: Số lượng danh sách 'List_Test_1' là {list_count}, nhưng mong đợi là 1."


    logging.info("Test case PASS: Thông báo đã xuất hiện và chỉ có 1 danh sách 'List_Test_1'.")





