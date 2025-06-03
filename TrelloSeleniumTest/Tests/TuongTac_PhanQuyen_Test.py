import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import TrelloSeleniumTest
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Quan_Ly_Board import Quan_Ly_Board

Email_Invite = "0306221443@caothang.edu.vn"

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
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

#Test case 22
def test_Them_Thanh_Vien_Vao_Bang(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Share_Button_Click()
    QLBoard.fill_email_input(Email_Invite)
    QLBoard.Invite_Button_Click()

    member_elements = driver.find_elements(By.CSS_SELECTOR,
        "div[data-testid='member-item']")  # Cập nhật phương thức tìm kiếm
    member_count = len(member_elements)  # Đếm số lượng thành viên

    # Kiểm tra xem email đã được thêm vào danh sách thành viên hay chưa
    email_found = any(
        Email_Invite in member.text for member in member_elements)  # Kiểm tra nếu email có trong phần tử thành viên

    # Assert kết quả
    if member_count == 2 and email_found:
        print("Test case PASS: Số lượng thành viên là 2 và tìm thấy email mời.")
    else:
        print("Test case FAIL: Điều kiện không thỏa mãn.")

#Test case 23
def test_Thanh_Vien_Yeu_Cau_Vao_Bang(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    URL_SHARE = ""
    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Share_Button_Click()
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    #time.sleep(1000)
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest1@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()

    wait_for_element(driver, By.XPATH,"//button[@data-testid='header-create-menu-button']")
    # Thay thế dòng driver.get bằng mã để thay đổi URL
    new_url = "https://trello.com/invite/b/683728efeaab183d8b373c79/ATTIa4b2533b9eda91cff5b218e40978919eF170FF1B/test"
    driver.execute_script(f"window.location.href = '{new_url}';")

    # Đảm bảo trang được tải lại
    driver.refresh()

    QLBoard.Join_Board_Button_Click()
    QLBoard.Share_Button_Click()

    # Tìm tất cả các phần tử thành viên
    # Tìm tất cả các phần tử thành viên
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO"))
    )

    # Tìm tất cả các div con có class "wFehm16heN83eQ" bên trong div cha
    child_divs = parent_div.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")

    # Đếm số lượng thẻ div
    member_count = len(child_divs)

    # Kiểm tra xem tên "Tester001 (tester0015)" đã được thêm vào danh sách thành viên hay chưa
    name_found = any(
        "Tester001" in member.text for member in member_elements
    )

    # Hoặc bạn có thể tìm kiếm bằng cách lấy tên từ span cụ thể
    name_found = any(
        "Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text
        for member in child_divs  # Sử dụng child_divs thay vì member_elements
    )

    # Assert kết quả
    if member_count == 3 and name_found:
        print("Test case PASS: Số lượng thành viên là 3 và tìm thấy tên Tester001 (tester0015).")
    else:
        if member_count != 3:
            print(f"Test case FAIL: Số lượng thành viên không đúng. Hiện tại có {member_count} thành viên.")
        if not name_found:
            print("Test case FAIL: Tên 'Tester001 (tester0015)' không được tìm thấy trong danh sách thành viên.")
