import time

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

#Test case 20
def test_Tao_Card_Voi_Ten_Hop_Le(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()

    ql_card = QuanLyCard(driver)
    ql_card.create_card('short')

    number_of_cards = ql_card.count_cards_in_list()

    # Thay đổi assertEqual thành assert để tương thích với pytest
    assert number_of_cards == 1, f"Số lượng thẻ trong danh sách không đúng: {number_of_cards}. Kỳ vọng là 1."

#Test case 21
def test_Tao_Card_Voi_Ten_Link(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()

    ql_card = QuanLyCard(driver)
    ql_card.create_card('link')

    number_of_cards = ql_card.count_cards_in_list()

    # Thay đổi assertEqual thành assert để tương thích với pytest
    assert number_of_cards == 2, f"Số lượng thẻ trong danh sách không đúng: {number_of_cards}. Kỳ vọng là 2."

#Test case 23
def test_Set_DeadLine(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Into_Board_Click()

    ql_card = QuanLyCard(driver)
    ql_card.set_deadline()

    number_of_deadline_cards = ql_card.count_cards_with_deadline()

    # So sánh với số lượng mong muốn (3)
    assert number_of_deadline_cards == 3, f"Số lượng thẻ có deadline không đúng: {number_of_deadline_cards}. Kỳ vọng là 3."

#Test case 30 - Đặt giới hạn card cho list
def test_limit_cards_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Into_Board_Click()

    QLListPage = Quan_Ly_List(driver)
    QLListPage.click_menu_list()
    time.sleep(1)
    QLListPage.click_add_limit_card_button()
    QLListPage.fill_input_limit()
    QLListPage.click_save_button()
    QLListPage.click_close_button()

    ql_card = QuanLyCard(driver)
    ql_card.create_card('short')
    number_of_cards = ql_card.count_cards_in_list()

    # Kiểm tra màu nền của thẻ danh sách
    list_element = driver.find_element(By.CSS_SELECTOR,
                                       "div[data-testid='list'][style*='--accent-background: var(--ds-background-warning)']")

    # Assert để kiểm tra số lượng thẻ và màu nền
    assert number_of_cards == 3, f"Số lượng thẻ trong danh sách không đúng: {number_of_cards}. Kỳ vọng là 3."
    assert list_element is not None, "Thẻ danh sách không chuyển nền thành màu vàng khi vượt quá giới hạn."