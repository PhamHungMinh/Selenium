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
    login_page.Fill_Email(email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(password)
    login_page.Continue_Button_Click()

def navigate_to_trello(driver):
    atlassian_page = HomeAtlassianPage(driver)
    home_page = HomeTrelloPage(driver)

    atlassian_page.Menu_Click()
    atlassian_page.Trello_Click()
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

# Hàm đếm card trong list_test_1
def count_cards_in_list(driver):
    try:
        # Chờ cho danh sách "List_Test_1" xuất hiện
        list_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
        )

        # Tìm tất cả các card trong danh sách này
        cards_xpath = "//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//ol[@data-testid='list-cards']//li[@data-testid='list-card']"
        cards = driver.find_elements(By.XPATH, cards_xpath)

        # Đếm số lượng card
        card_count = len(cards)
        return card_count

    except Exception as e:
        print(f"Đã xảy ra lỗi khi đếm thẻ: {e}")
        return 0

#Test case 18
def test_Tao_Card_Voi_Ten_Hop_Le(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()

    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('short')

    try:
        # Chờ cho danh sách "List_Test_1" xuất hiện
        list_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
        )

        # Tìm kiếm card "card test 1" trong danh sách này
        card_xpath = "//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//ol[@data-testid='list-cards']//a[contains(text(), 'card test 1')]"
        card_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, card_xpath))
        )

        # Assert rằng card đã được tìm thấy
        assert card_element is not None, "Card 'card test 1' không tồn tại trong danh sách 'List_Test_1'."
        print("Test case passed: Card 'card test 1' đã được tìm thấy trong danh sách 'List_Test_1'.")

    except Exception as e:
        print(f"Test case failed: {e}")

#Test case 19
def test_Tao_Card_Voi_Ten_Link(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()

    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('link')

    try:
        # Chờ cho danh sách "List_Test_1" xuất hiện
        list_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
        )

        # Tìm kiếm card "card test 1" trong danh sách này
        card_xpath = "//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//ol[@data-testid='list-cards']//a[contains(text(), 'https://docs.google.com/')]"
        card_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, card_xpath))
        )

        # Assert rằng card đã được tìm thấy
        assert card_element is not None, "https://docs.google.com/' không tồn tại trong danh sách 'List_Test_1'."
        print("Test case passed: Card 'https://docs.google.com/' đã được tìm thấy trong danh sách 'List_Test_1  '.")

    except Exception as e:
        print(f"Test case failed: {e}")

#Test case 20
def test_Set_DeadLine(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_card = QuanLyCard(driver)
    ql_card.Set_Deadline()

    number_of_deadline_cards = ql_card.Count_Cards_With_Deadline()

    # So sánh với số lượng mong muốn (3)
    assert number_of_deadline_cards == 3, f"Số lượng thẻ có deadline không đúng: {number_of_deadline_cards}. Kỳ vọng là 3."
    print("Tìm thấy 3 card có deadline trong list 'Mặc định'.")

#Test case 29 - Đặt giới hạn card cho list
def test_limit_cards_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")

    navigate_to_trello(driver)
    HomePage = HomeTrelloPage(driver)
    HomePage.Click_Enter_Board()
    QLListPage = QuanLyList(driver)
    QLListPage.Click_Menu_List()
    time.sleep(1)
    QLListPage.Add_Limit_Card_Button_Click()
    QLListPage.Fill_Input_Limit()
    QLListPage.Save_Button_Click()
    QLListPage.Click_Close_Button()

    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('limit')

    card_count = count_cards_in_list(driver)
    print(f"Số lượng thẻ hiện tại trong danh sách 'List_Test_1': {card_count}")

    # Kiểm tra màu nền của thẻ danh sách
    list_element = driver.find_element(By.CSS_SELECTOR,
                                       "div[data-testid='list'][style*='--accent-background: var(--ds-background-warning)']")

    # Assert để kiểm tra số lượng thẻ và màu nền
    assert card_count == 3, f"Số lượng thẻ trong danh sách không đúng: {card_count}. Kỳ vọng là 3."
    assert list_element is not None, "Thẻ danh sách không chuyển nền thành màu vàng khi vượt quá giới hạn."
    print(f"Danh sách chuyển sang màu ấm khi số lượng thẻ lớn hơn giới hạn {card_count} > 2.")