import time
from time import sleep

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import TrelloSeleniumTest
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Quan_Ly_Board import Quan_Ly_Board
from TrelloSeleniumTest.Pages.Quan_Ly_Card import QuanLyCard
from utils import wait_for_element, login_to_atlassian, navigate_to_trello

Email_Invite = "0306221443@caothang.edu.vn"
Find_User = "@nghiangotrng3"

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()
    yield driver
    driver.quit()

#Test case 21
def test_Moi_Thanh_Vien_Vao_Bang(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Share_Button_Click()
    QLBoard.Fill_Email_Input(Email_Invite)
    QLBoard.Invite_Button_Click()
    QLBoard.Invite_Button_Click()
    # Admin bảng
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")  # Tìm tất cả thành viên
    member_count = len(member_elements)  # Đếm số lượng thành viên

    # Kiểm tra nếu email có trong danh sách thành viên
    email_found = any(
        Find_User in member.find_element(By.XPATH, ".//div[@class='Nb2wVffRyPwsUc']//div").text for member in
        member_elements
    )
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("0306221443@caothang.edu.vn")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("Nghia842004@")
    login_page.click_login()

    # Assert kết quả
    wait_for_element(driver, By.XPATH, "//a[@href='/b/6jkUMfhu/test']")  # Đợi cho phần tử xuất hiện

    # Kiểm tra điều kiện
    if member_count == 2 and email_found and driver.find_element(By.XPATH, "//a[@href='/b/6jkUMfhu/test']"):
        print("Test case PASS: Số lượng thành viên là 2, tìm thấy email mời và phần tử đã xuất hiện.")
    else:
        if member_count != 2:
            print("Test case FAIL: Số lượng thành viên không đủ 2.")
        if not email_found:
            print("Test case FAIL: Không tìm thấy email trong danh sách thành viên.")
        if not driver.find_elements(By.XPATH, "//a[@href='/b/6jkUMfhu/test']"):
            print("Test case FAIL: Phần tử không tìm thấy.")


# Test case 22
def test_Thanh_Vien_Yeu_Cau_Vao_Bang(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Share_Button_Click()
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest1@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()

    wait_for_element(driver, By.XPATH,"//button[@data-testid='header-create-menu-button']")
    new_url = "https://trello.com/invite/b/683728efeaab183d8b373c79/ATTIa4b2533b9eda91cff5b218e40978919eF170FF1B/test"
    driver.execute_script(f"window.location.href = '{new_url}';")

    # Đảm bảo trang được tải lại
    driver.refresh()

    QLBoard.Join_Board_Button_Click()
    QLBoard.Share_Button_Click()

    # Tìm kết quả bên user
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO"))
    )

    # Tìm tất cả các div con có class "wFehm16heN83eQ" bên trong div cha
    child_divs = parent_div.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")

    # Đếm số lượng thẻ div
    user_member_count = len(child_divs)

    # Kiểm tra xem tên "Tester001 (tester0015)" đã được thêm vào danh sách thành viên hay chưa
    user_name_found = any(
        "Tester001" in member.text for member in member_elements
    )

    # Hoặc bạn có thể tìm kiếm bằng cách lấy tên từ span cụ thể
    user_name_found = any(
        "Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text
        for member in child_divs  # Sử dụng child_divs thay vì member_elements
    )

    QLBoard.Close_Share_Button_Click2()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest1@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard.Share_Button_Click()

    # Tìm kết quả bên admin
    member_elements_admin = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div_admin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO"))
    )

    # Tìm tất cả các div con có class "wFehm16heN83eQ" bên trong div cha
    child_divs_admin = parent_div_admin.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")

    # Đếm số lượng thẻ div
    admin_member_count = len(child_divs_admin)

    # Kiểm tra xem tên "Tester001 (tester0015)" đã được thêm vào danh sách thành viên hay chưa
    admin_name_found = any(
        "Tester001" in member.text for member in member_elements_admin
    )

    # Hoặc bạn có thể tìm kiếm bằng cách lấy tên từ span cụ thể
    admin_name_found = any(
        "Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text
        for member in child_divs_admin  # Sử dụng child_divs_admin thay vì member_elements_admin
    )

    # Assert kết quả
    assert user_member_count == 3 and user_name_found, "FAIL"
    assert admin_member_count == 3 and admin_name_found, "FAIL"

# Test case 23
def test_ThanhVien_WS_Xem_Bang_Private(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Visibility_Click()
    QLBoard.Visibility_Private_Click()
    QLBoard.Menu_Trello_Click()
    QLBoard.Trello_Home_Click()
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

    home_page.Xem_Thanh_Vien_23()
    home_page.Moi_Thanh_Vien_23()
    home_page.Fill_Email_Member_Input_Click_23()
    home_page.Button_add_click_23()
    home_page.Close_Add_Member_Click_23()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest2@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    home_page.Work_Space_Click_23()
    home_page.Boards_Click_23()

    #Kiểm tra xem có bảng "Test" trong work space hay không
    try:
        # Tìm tất cả các phần tử bảng trong danh sách
        board_items = driver.find_elements(By.CSS_SELECTOR, "li.boards-page-board-section-list-item")

        # Biến kiểm tra sự tồn tại
        test_board_exists = False

        # Duyệt qua từng bảng để kiểm tra tên
        for item in board_items:
            try:
                board_name_element = item.find_element(By.CSS_SELECTOR, "div.board-tile-details-name div")
                board_name = board_name_element.text

                # Kiểm tra tên bảng chính xác là "Test" (không phân biệt hoa thường)
                if board_name.lower() == "Test":
                    test_board_exists = True
                    print(f"Tìm thấy bảng không mong muốn: {board_name}")
                    break
            except:
                # Bỏ qua các item không phải là bảng thực sự
                continue

        # Assert: Test case PASS nếu không tìm thấy bảng "Test"
        assert not test_board_exists, "Test case FAILED: Tìm thấy bảng 'Test' trong danh sách"
        print("Test case PASSED: Không tìm thấy bảng 'Test' trong danh sách")

    except Exception as e:
        print(f"Lỗi trong quá trình kiểm tra: {str(e)}")
        raise

#Test case 24:
def test_User_YeuCau_ThamGia_Bang_Private(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()

    cur_url = driver.current_url

    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest3@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()

    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    driver.execute_script(f"window.location.href = '{cur_url}';")
    driver.execute_script("document.body.style.zoom='90%'")
    QLBoard.Accept_Into_Private_Board_Click()
    driver.execute_script("document.body.style.zoom='100%'")

    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("ngotrongnghia8424@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")

    home_page.Into_Board_Click()
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
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest3@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()

    # Chờ cho phần tử với XPath cụ thể xuất hiện
    wait_for_element(driver, By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")

    # Kiểm tra sự tồn tại của phần tử
    test_board_exists = False
    try:
        test_board_element = driver.find_element(By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        test_board_exists = True if test_board_element else False
    except NoSuchElementException:
        test_board_exists = False

    # Assert: Test case PASS nếu tìm thấy bảng "Test" và thông báo đúng
    if not result_message:
        print("Test case FAILED: Thông báo không hiển thị đúng.")
    if not test_board_exists:
        print("Test case FAILED: Không tìm thấy bảng 'Test' trong danh sách.")
    print(result_message)
    print(test_board_exists)

    assert result_message and test_board_exists, "Test case FAILED: Không thỏa mãn điều kiện."

    print("Test case PASSED: Thông báo hiển thị đúng và tìm thấy bảng 'Test' trong danh sách.")

#Test case 25
def test_Huy_YeuCau_User_ThamGia_Bang_Private(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()

    cur_url = driver.current_url

    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest4@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    #time.sleep(2000000)

    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    driver.execute_script(f"window.location.href = '{cur_url}';")
    driver.execute_script("document.body.style.zoom='90%'")
    QLBoard.Accept_Into_Private_Board_Click()
    driver.execute_script("document.body.style.zoom='100%'")

    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("ngotrongnghia8424@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")

    home_page.Into_Board_Click()
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
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("minhnghiaseleniumtest4@gmail.com")
    login_page.click_continue()
    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    #time.sleep(5000)
    wait_for_element(driver, By.XPATH, "//button[p[text()='Tạo mới']]")

    # Kiểm tra sự tồn tại của phần tử
    test_board_exists = False
    try:
        test_board_element = driver.find_element(By.XPATH, "//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        test_board_exists = True if test_board_element else False
    except NoSuchElementException:
        test_board_exists = False

    # Kiểm tra điều kiện để xác định kết quả của test case
    if notification_exists and not test_board_exists:
        print("Test case pass: Notification exists and 'Test' board is not found.")
        return True
    else:
        print("Test case fail: Either notification is missing or 'Test' board exists.")
        return False

def test_Thanh_Vien_Binh_Luan_Thanh_Cong(driver):
    login_to_atlassian(driver, "0306221442@caothang.edu.vn", "082204016528A")
    navigate_to_trello(driver)

    URL_SHARE = ""
    home_page = HomeTrelloPage(driver)
    QLBoard = Quan_Ly_Board(driver)
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
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("ngotrongnghia8424@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    time.sleep(10)
    comments_xpath = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"
    # Lấy tất cả các bình luận
    comments = driver.find_elements(By.XPATH, comments_xpath)
    # Kiểm tra xem có bình luận mới không
    if comments:
        print(f"Có {len(comments)} bình luận mới.")
        # Lấy nội dung bình luận đầu tiên
        first_comment = comments[0].find_element(By.XPATH, ".//div[contains(@class, 'ak-renderer-wrapper')]//p").text
        print(f"Bình luận mới nhất: {first_comment}")
    else:
        print("Không có bình luận mới.")

    time.sleep(10)
#Test case 27
def test_ThanhVien_BinhLuanTagUser(driver):
    login_to_atlassian(driver, "0306221442@caothang.edu.vn", "082204016528A")
    navigate_to_trello(driver)

    URL_SHARE = ""
    home_page = HomeTrelloPage(driver)
    QLBoard = Quan_Ly_Board(driver)
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    QL_Card = QuanLyCard(driver)
    QL_Card.Click_Button_Comment_Card()
    QL_Card.fill_tag_user()
    QL_Card.Click_Choose_User()
    QL_Card.Comment_User()
    QL_Card.Click_Button_Save()
    QLBoard.Click_Close_Card()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.enter_email("ngotrongnghia8424@gmail.com")
    login_page.click_continue()

    wait_for_element(driver, By.ID, "password")
    login_page.enter_password("khongcomatkhau4654")
    login_page.click_login()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()

    comments_xpath2 = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"

    # Lấy tất cả các bình luận
    comments = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, comments_xpath2))
    )

    # Kiểm tra xem có bình luận mới không
    if comments:
        print(f"Có {len(comments)} bình luận mới.")

        # Lấy nội dung bình luận mới nhất (bình luận đầu tiên trong danh sách)
        latest_comment = comments[0].find_element(By.XPATH, ".//div[@class='TTb5N2DgAn9VHs']//p").text
        print(f"Bình luận mới nhất: {latest_comment}")
    else:
        print("Không có bình luận mới.")
    time.sleep(10)
