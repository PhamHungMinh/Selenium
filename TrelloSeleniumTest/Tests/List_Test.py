import logging
import time

import pytest
from TrelloSeleniumTest.Pages.Quan_ly_List import QuanLyList
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.untils import *

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

# Gom tất cả test case vào một hàm duy nhất
def test_Trello_List_Functionality(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_list_page = QuanLyList(driver)

    # Test case 13: Tạo danh sách với tên hợp lệ
    ql_list_page.Create_List_Click()
    ql_list_page.Fill_List_Name_Input()
    ql_list_page.Button_Create_List_WithName_Click()

    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)
    list_element = driver.find_element(By.XPATH, "(//li[@data-testid='list-wrapper'])[2]//h2[@data-testid='list-name']"
                                                 "/button/span[text()='List_Test_1']")
    assert list_element.is_displayed(), "Danh sách 'List_Test_1' không được tìm thấy."
    print("Test case 13 passed: Danh sách 'List_Test_1' đã được tạo và tìm thấy.")
    logging.info("Test case 13 passed.")

    # Test case 14: Tạo danh sách với tên trùng lặp
    ql_list_page.Fill_Same_Name_List_Input()
    ql_list_page.Button_Create_List_WithName_Click()

    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)
    list_elements = driver.find_elements(By.XPATH, "//li[@data-testid='list-wrapper']"
                                                   "//h2[@data-testid='list-name']"
                                                   "/button/span[text()='List_Test_1']")
    count = len(list_elements)

    assert count == 2, f"Số lượng danh sách 'List_Test_1' không phải là 2, mà là {count}."
    print("Test case 14 passed: Có 2 danh sách 'List_Test_1' được tìm thấy.")
    logging.info("Test case 14 passed.")

    # Test case 15: Tạo danh sách với tên dài
    ql_list_page.Fill_Long_Name_List()
    ql_list_page.Button_Create_List_WithName_Click()

    textarea = driver.find_element(By.XPATH,
                                   "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][4]"
                                   "//textarea[@data-testid='list-name-textarea']")
    length = len(textarea.get_attribute("value"))

    expected_length = 512
    assert length == expected_length, f"Test case FAIL: Độ dài tên danh sách là {length}, khác 512."
    print("Test case 15 passed: Đã tạo thành công danh sách với tên dài.")
    logging.info("Test case 15 passed.")

    # Test case 17: Lưu trữ danh sách
    ql_list_page.Click_Menu_List()
    ql_list_page.Archive_List_Button_Click()

    alert_visible = ql_list_page.Check_Alert_Message()
    wait_for_element(driver, By.XPATH, ql_list_page.Wait_For_Board_To_Display)
    driver.refresh()
    Wait_List = wait_for_element(driver,By.XPATH,"//li[@data-testid='list-wrapper']"
                                                 "//h2[@data-testid='list-name']"
                                                 "/button/span[text()='List_Test_1']")

    list_elements = driver.find_elements(By.XPATH, "//li[@data-testid='list-wrapper']"
                                                   "//h2[@data-testid='list-name']"
                                                   "/button/span[text()='List_Test_1']")
    list_count = len(list_elements)

    assert alert_visible, "Test case FAIL: Thông báo không xuất hiện sau khi lưu trữ danh sách."
    assert list_count == 1, f"Test case FAIL: Số lượng danh sách 'List_Test_1' là {list_count}, nhưng mong đợi là 1."

    print("Test case 17 passed: Thông báo đã xuất hiện và chỉ có 1 danh sách 'List_Test_1'.")
    logging.info("Test case 17 passed.")