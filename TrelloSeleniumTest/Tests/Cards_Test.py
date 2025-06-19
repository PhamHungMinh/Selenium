import logging
import pytest
from TrelloSeleniumTest.Pages.Quan_ly_List import QuanLyList
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Quan_Ly_Card import QuanLyCard
from TrelloSeleniumTest.Until.utils import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
    yield driver
    driver.quit()

# Test case 18
def test_Create_Card_With_Valid_Name(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('nommar')
    list_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
    )
    card_xpath = ("//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//ol[@data-testid='list-cards']"
                  "//a[contains(text(), 'card test 1')]")
    card_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, card_xpath))
    )
    assert card_element is not None, "Card 'card test 1' không tồn tại trong danh sách 'List_Test_1'."
    logging.info("Test case passed: Card 'card test 1' đã được tìm thấy trong danh sách 'List_Test_1'.")

# Test case 19
def test_Create_Card_With_Link_Name(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('link')
    list_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
    )
    card_xpath = ("//li[@data-testid='list-wrapper'][.//h2/button[contains(text(),"
                  " 'List_Test_1')]]//ol[@data-testid='list-cards']//a[contains(text(), 'https://docs.google.com/')]")
    card_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, card_xpath))
    )
    assert card_element is not None, "Card 'https://docs.google.com/' không tồn tại trong danh sách 'List_Test_1'."
    logging.info("Test case passed: Card 'https://docs.google.com/' đã được tìm thấy trong danh sách 'List_Test_1'.")

# Test case 20
def test_Set_DeadLine_For_Card(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_card = QuanLyCard(driver)
    ql_card.Set_Deadline()
    number_of_deadline_cards = ql_card.Count_Cards_With_Deadline()
    assert number_of_deadline_cards == 3, f"Số lượng thẻ có deadline không đúng: {number_of_deadline_cards}. Kỳ vọng là 3."
    logging.info("Tìm thấy 3 card có deadline trong list 'Mặc định'.")

# Test case 29 - Đặt giới hạn card cho list
def test_Set_Card_Limit_For_List(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    ql_list_page = QuanLyList(driver)
    ql_list_page.Click_Menu_List()
    time.sleep(1) #Độ trễ
    ql_list_page.Add_Limit_Card_Button_Click()
    ql_list_page.Fill_Input_Limit()
    ql_list_page.Save_Button_Click()
    ql_list_page.Click_Close_Button()
    ql_card = QuanLyCard(driver)
    ql_card.Create_Card('limit')
    card_count = count_cards_in_list(driver)
    logging.info(f"Số lượng thẻ hiện tại trong danh sách 'List_Test_1': {card_count}")
    list_element = driver.find_element(By.CSS_SELECTOR, "div[data-testid='list'][style*='--accent-background: var(--ds-background-warning)']")
    assert card_count == 3, f"Số lượng thẻ trong danh sách không đúng: {card_count}. Kỳ vọng là 3."
    assert list_element is not None, "Thẻ danh sách không chuyển nền thành màu vàng khi vượt quá giới hạn."
    logging.info(f"Danh sách chuyển sang màu ấm khi số lượng thẻ lớn hơn giới hạn {card_count} > 2.")

def count_cards_in_list(driver):
    try:
        list_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-testid='list-wrapper']//h2/button[contains(text(), 'List_Test_1')]"))
        )
        cards_xpath = "//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//ol[@data-testid='list-cards']//li[@data-testid='list-card']"
        cards = driver.find_elements(By.XPATH, cards_xpath)
        return len(cards)
    except Exception as e:
        logging.error(f"Đã xảy ra lỗi khi đếm thẻ: {e}")
        return 0
