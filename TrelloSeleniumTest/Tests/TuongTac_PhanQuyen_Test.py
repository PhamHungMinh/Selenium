import time
import logging
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Quan_Ly_Board import QuanLyBoard
from TrelloSeleniumTest.Pages.Quan_Ly_Card import QuanLyCard
from TrelloSeleniumTest.Until.untils import wait_for_element, login_to_atlassian, navigate_to_trello, \
    wait_for_element_visible
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Email, Password, EmailUser, PasswordUser

Find_User = "@nghiangotrng3"


@pytest.fixture
def driver():
    driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
    yield driver
    driver.quit()


def run_all_test_cases(driver):
    # Test case 21: Invite Member To Board
    login_to_atlassian(driver, Email, Password)
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    QLBoard = QuanLyBoard(driver)
    QLBoard.Share_Button_Click()
    QLBoard.Fill_Email_Input("0306221443@caothang.edu.vn,")
    QLBoard.Invite_Button_Click()
    QLBoard.Invite_Button_Click()
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    member_count = len(member_elements)
    email_found = any(
        Find_User in member.find_element(By.XPATH, ".//div[@class='Nb2wVffRyPwsUc']//div").text for member in
        member_elements)

    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@name='username']")
    login_page.Fill_Email_Again("0306221443@caothang.edu.vn")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password("Nghia842004@")
    login_page.Login_Button_Click()
    wait_for_element(driver, By.XPATH, "//a[@href='/b/6jkUMfhu/test']")

    # Assert kết quả
    assert member_count == 2, "Test case 21 FAIL: Số lượng thành viên không đúng."
    assert email_found, "Test case 21 FAIL: Không tìm thấy email mời."
    assert driver.find_element(By.XPATH, "//a[@href='/b/6jkUMfhu/test']"), "Test case 21 FAIL: Phần tử không xuất hiện."
    print("Test case 21 PASS: Số lượng thành viên là 2, tìm thấy email mời và phần tử đã xuất hiện.")

    # Test case 22:  Thành viên tham gia bảng qua link mời
    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@name='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest1@gmail.com")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    new_url = "https://trello.com/invite/b/683728efeaab183d8b373c79/ATTIa4b2533b9eda91cff5b218e40978919eF170FF1B/test"
    driver.execute_script(f"window.location.href = '{new_url}';")
    driver.refresh()
    QLBoard.Join_Board_Button_Click()
    QLBoard.Share_Button_Click()

    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO")))
    child_divs = parent_div.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")
    user_member_count = len(child_divs)
    user_name_found = any(
        "Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text for
        member in child_divs)

    QLBoard.Close_Share_Button_Click2()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()

    member_elements_admin = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div_admin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO")))
    child_divs_admin = parent_div_admin.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")
    admin_member_count = len(child_divs_admin)
    admin_name_found = any(
        "Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text for
        member in child_divs_admin)

    # Assert kết quả
    assert user_member_count == 3, "Test case 22 FAIL: User member count không đúng."
    assert user_name_found, "Test case 22 FAIL: Tên user không tìm thấy."
    assert admin_member_count == 3, "Test case 22 FAIL: Admin member count không đúng."
    assert admin_name_found, "Test case 22 FAIL: Tên user không tìm thấy."
    print("Test case 22 PASS: User và Admin member counts đều chính xác và tên đã được tìm thấy.")

    # Test case 23 - Kiểm tra khả năng xem bảng private của thành viên Work Space
    QLBoard.Close_Share_Button_Click2()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    home_page.Click_Enter_Board()

    QLBoard.Visibility_Click()
    QLBoard.Visibility_Private_Click()
    QLBoard.Menu_Trello_Click()
    QLBoard.Trello_Home_Click()
    driver.get(Trello_Url)

    # Lưu ID của cửa sổ gốc
    original_window = driver.current_window_handle

    # Kiểm tra và đóng các cửa sổ khác nếu có
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            driver.close()  # Đóng cửa sổ mới
            driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc

    # Đảm bảo chỉ có một cửa sổ mở
    assert len(driver.window_handles) == 1, "Test case 23 FAIL: Có nhiều cửa sổ mở."

    home_page.Click_View_Members_23()
    home_page.Click_Add_Member_23()
    home_page.Fill_Email_Member_Input_Click_23()
    home_page.Click_Send_Invite_Button_23()
    driver.refresh()
    home_page.Click_Close_Member_WS_Button()
    home_page.Click_Close_MN_PS_Button()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest2@gmail.com")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    home_page.Click_Work_Space_23()
    home_page.Click_Boards_23()

    # Kiểm tra xem có bảng "Test" trong work space hay không
    board_items = driver.find_elements(By.CSS_SELECTOR, "li.boards-page-board-section-list-item")
    test_board_exists = False

    # Duyệt qua từng bảng để kiểm tra tên
    for item in board_items:
        board_name_element = item.find_element(By.CSS_SELECTOR, "div.board-tile-details-name div")
        board_name = board_name_element.text
        # Kiểm tra tên bảng chính xác là "Test" (không phân biệt hoa thường)
        if board_name.lower() == "test":
            test_board_exists = True
            print(f"Tìm thấy bảng không mong muốn: {board_name}")
            break

    # Assert: Test case PASS nếu không tìm thấy bảng "Test"
    if not test_board_exists:
        print("Test case 23 PASSED: Không tìm thấy bảng 'Test' trong danh sách")
    else:
        print("Test case 23 FAILED: Tìm thấy bảng 'Test' trong danh sách")

    # Test case 24 - Thành viên yêu cầu tham gia bảng private:
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    home_page.Click_Enter_Board()

    cur_url = driver.current_url
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest3@gmail.com")
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    driver.execute_script(f"window.location.href = '{cur_url}';")
    driver.execute_script("document.body.style.zoom='90%'")
    QLBoard.Accept_Into_Private_Board_Click()
    driver.execute_script("document.body.style.zoom='100%'")

    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")

    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()
    QLBoard.Request_Into_Board_Click()
    QLBoard.Select_Visibility_Click()
    QLBoard.Select_Member_Click()

    result_message = False
    try:
        # Chờ cho thông báo xuất hiện
        notification = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.YEctMXs9uZbttS"))
        )

        # Nếu thông báo xuất hiện, gán result_message là True
        result_message = True

    except Exception as e:
        print(f"Lỗi khi kiểm tra thông báo: {str(e)}")

    QLBoard.Close_Share_Button_Click2()
    # Đăng xuất và đăng nhập lại
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest3@gmail.com")
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    # Chờ cho phần tử với XPath cụ thể xuất hiện
    wait_for_element_visible(driver, By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")

    # Kiểm tra sự tồn tại của phần tử
    test_board_exists = False
    try:
        test_board_element = driver.find_element(By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        test_board_exists = True if test_board_element else False
    except NoSuchElementException:
        test_board_exists = False

    # Assert: Test case PASS nếu tìm thấy bảng "Test" và thông báo đúng
    assert result_message, "Test case 24 FAILED: Thông báo không hiển thị đúng."
    assert test_board_exists, "Test case 24 FAILED: Không tìm thấy bảng 'Test' trong danh sách."

    print("Test case PASSED: Thông báo hiển thị đúng và tìm thấy bảng 'Test' trong danh sách.")

    # Test case 25
    home_page.Click_Enter_Board()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")

    home_page.Click_Enter_Board()

    cur_url = driver.current_url

    QLBoard = QuanLyBoard(driver)
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest4@gmail.com")
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    driver.execute_script(f"window.location.href = '{cur_url}';")
    driver.execute_script("document.body.style.zoom='90%'")
    QLBoard.Accept_Into_Private_Board_Click()
    driver.execute_script("document.body.style.zoom='100%'")

    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")

    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()
    QLBoard.Request_Into_Board_Click()
    QLBoard.Deny_Request_Into_Board_Click()

    notification_exists = False
    try:
        # Chờ cho thông báo xuất hiện
        notification = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.YEctMXs9uZbttS"))
        )

        # Nếu thông báo xuất hiện, gán result_message là True
        notification_exists = True

    except Exception as e:
        print(f"Lỗi khi kiểm tra thông báo: {str(e)}")

    QLBoard.Close_Share_Button_Click2()
    # Đăng xuất và đăng nhập lại
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again("minhnghiaseleniumtest4@gmail.com")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()

    wait_for_element_visible(driver, By.XPATH, "//button[p[text()='Tạo mới']]")

    # Kiểm tra sự tồn tại của phần tử
    test_board_exists = False
    try:
        test_board_element = driver.find_element(By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        test_board_exists = True if test_board_element else False
    except NoSuchElementException:
        test_board_exists = False

    # Kiểm tra điều kiện để xác định kết quả của test case
    if notification_exists and not test_board_exists:
        print("Test case 25 PASS: Notification exists and 'Test' board is not found.")
    else:
        print("Test case 25 FAIL: Either notification is missing or 'Test' board exists.")
        return False

    # Test case 26: Member Comment Success
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(EmailUser)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(PasswordUser)
    login_page.Login_Button_Click()

    home_page = HomeTrelloPage(driver)
    QLBoard = QuanLyBoard(driver)
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    QL_Card = QuanLyCard(driver)
    QL_Card.Click_Button_Comment_Card()
    QL_Card.Fill_Input_Comment_Card()
    QL_Card.Click_Button_Save()
    QLBoard.Click_Close_Card()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    time.sleep(3)
    comments_xpath = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"
    comments = driver.find_elements(By.XPATH, comments_xpath)

    if comments:
        first_comment = comments[0].find_element(By.XPATH, ".//div[contains(@class, 'ak-renderer-wrapper')]//p").text
        print(f"Test case 26 PASS: Có {len(comments)} bình luận mới. Bình luận mới nhất: {first_comment}")
    else:
        print("Test case 26 FAIL: Không có bình luận mới.")

    # Test case 27: Member Comment Tag User
    QLBoard.Click_Close_Comment()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(EmailUser)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(PasswordUser)
    login_page.Login_Button_Click()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    QL_Card = QuanLyCard(driver)
    QL_Card.Click_Button_Comment_Card()
    QL_Card.Fill_Tag_User()
    QL_Card.Click_Choose_User()
    time.sleep(1)
    QL_Card.Comment_User_Enter()
    QL_Card.Click_Button_Save()
    time.sleep(1)
    QLBoard.Click_Close_Comment()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element_visible(driver, By.XPATH, "//input[@data-testid='username']")
    login_page.Fill_Email_Again(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    comments_xpath2 = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"
    comments = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, comments_xpath2)))

    if comments:
        latest_comment = comments[0].find_element(By.XPATH, ".//div[@class='TTb5N2DgAn9VHs']//p").text
        print(f"Test case 27 PASS: Có {len(comments)} bình luận mới. Bình luận mới nhất: {latest_comment}")
    else:
        print("Test case 27 FAIL: Không có bình luận mới.")


# Chạy tất cả các test case
def test_all_cases(driver):
    run_all_test_cases(driver)
