import pytest
import time
import pymsgbox
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt
    driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
    yield driver
    driver.quit()

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
    time.sleep(3)
    HomePage.click_trello_create_board_button()
    time.sleep(3)
    HomePage.fill_board_name_input()
    time.sleep(3)
    HomePage.create_board_with_name()
    time.sleep(3)
    HomePage.click_return()
    time.sleep(3)
    HomePage.click_board()
    time.sleep(3)
    HomePage.click_menu_board()
    time.sleep(3)
    HomePage.click_change()
    time.sleep(3)
    HomePage.click_change_color()
    time.sleep(3)
    HomePage.click_color()
    time.sleep(3)
    HomePage.click_cancel()
    time.sleep(3)

def test_TaoBoard_Background(driver):
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
    #time.sleep(500)

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
    HomePage.click_board()
    time.sleep(5)
    HomePage.click_menu_board()
    time.sleep(5)
    HomePage.click_change()
    time.sleep(5)
    HomePage.upload_background(r"D:\ui\Anh.jpg")
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'File too large')]"))
        )
        pymsgbox.alert("❌ Upload thất bại: File quá lớn!", "Kết quả")
    except TimeoutException:
        pymsgbox.alert("✅ Upload thành công: Không có lỗi!", "Kết quả")
    time.sleep(10)

def test_dong_Board(driver):
    Login_Page = LoginPage(driver)
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)
    Login_Page.open_page("https://id.atlassian.com/login")
    wait_for_element(driver, By.ID, "username")
    Login_Page.enter_email("ngotrongnghia8424@gmail.com")
    Login_Page.click_continue()

    # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
    wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
    Login_Page.enter_password("khongcomatkhau4654")
    Login_Page.click_login()

    AtlassianPage.Menu_click()
    AtlassianPage.Trello_click()
    # time.sleep(500)

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
    HomePage.click_board()
    time.sleep(5)
    HomePage.click_menu_board()
    time.sleep(5)
    HomePage.click_close_board()
    time.sleep(5)
    HomePage.click_confirm()
    time.sleep(5)
    HomePage.click_return()
    time.sleep(10)
    driver.refresh()

def test_mo_board_da_dong(driver):
    Login_Page = LoginPage(driver)
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)
    Login_Page.open_page("https://id.atlassian.com/login")
    wait_for_element(driver, By.ID, "username")
    Login_Page.enter_email("ngotrongnghia8424@gmail.com")
    Login_Page.click_continue()

    # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
    wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
    Login_Page.enter_password("khongcomatkhau4654")
    Login_Page.click_login()

    AtlassianPage.Menu_click()
    AtlassianPage.Trello_click()
    # time.sleep(500)

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
    HomePage.click_xem_board_da_dong()
    time.sleep(10)
    try:
        board = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/div/ul/li[3]/div[1]/a")
    except:
        print("Không tìm thấy board!")
    HomePage.click_open_again()
    time.sleep(5)
    button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='workspace-chooser-reopen-button']")
    button.click()
    time.sleep(5)
    HomePage.click_exit()
    driver.refresh()

def test_TaoBoard_TenDai(driver):
    Login_Page = LoginPage(driver)
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)
    Login_Page.open_page("https://id.atlassian.com/login")
    wait_for_element(driver, By.ID, "username")
    Login_Page.enter_email("ngotrongnghia8424@gmail.com")
    Login_Page.click_continue()

    # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
    wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
    Login_Page.enter_password("khongcomatkhau4654")
    Login_Page.click_login()

    AtlassianPage.Menu_click()
    AtlassianPage.Trello_click()
    # time.sleep(500)

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
    HomePage.Create_Board_Click()
    time.sleep(5)
    HomePage.click_trello_create_board_button()
    time.sleep(10)
    HomePage.fill_board_name_input_withnamelong()
    time.sleep(5)
    HomePage.create_board_with_name()
    time.sleep(10)
    HomePage.click_return()
    time.sleep(5)
    driver.refresh()



