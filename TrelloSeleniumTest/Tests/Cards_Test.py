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

# Gom tất cả test case vào một hàm duy nhất
def test_Trello_Card_Functionality(driver):
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()

    ql_card = QuanLyCard(driver)

    # Hàm đếm số thẻ trong danh sách
    def count_cards_in_list(list_index):
        try:
            # Tìm phần tử danh sách theo chỉ số
            list_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"(//li[@data-testid='list-wrapper'])[{list_index}]")  # Lấy danh sách theo chỉ số
                )
            )

            # XPath để tìm tất cả các thẻ card trong danh sách
            cards_xpath = f"(//li[@data-testid='list-wrapper'])[ {list_index}]//ol[@data-testid='list-cards']//li[@data-testid='list-card']"

            # Tìm tất cả các thẻ card
            cards = driver.find_elements(By.XPATH, cards_xpath)

            return len(cards)  # Trả về số lượng thẻ card
        except Exception as e:
            logging.error(f"Đã xảy ra lỗi khi đếm thẻ: {e}")
            return 0

    # Test case 18: Tạo thẻ với tên hợp lệ
    ql_card.Create_Card('card test 1')
    card_xpath_18 = "//ol[@data-testid='list-cards']//li[@data-testid='list-card']//a[@data-testid='card-name' and text()='card test 1']"
    card_element_18 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, card_xpath_18)))
    assert card_element_18 is not None, "Card 'card test 1' không tồn tại trong danh sách 'List_Test_1'."
    print("Test case 18 passed: Card 'card test 1' đã được tìm thấy trong danh sách 'List_Test_1'.")
    logging.info("Test case 18 passed.")

    # Test case 19: Tạo thẻ với tên là link
    ql_card.Create_Card('link')
    card_xpath_19 = "//ol[@data-testid='list-cards']/li[div[@data-testid='link-card']//a[@href='https://docs.google.com/']]"
    card_element_19 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, card_xpath_19)))
    assert card_element_19 is not None, "Card 'https://docs.google.com/' không tồn tại trong danh sách 'List_Test_1'."
    print("Test case 19 passed: Card 'https://docs.google.com/' đã được tìm thấy trong danh sách 'List_Test_1'.")
    logging.info("Test case 19 passed.")

    # Test case 20: Đặt deadline cho thẻ
    ql_card.Set_Deadline()
    number_of_deadline_cards = ql_card.Count_Cards_With_Deadline()
    assert number_of_deadline_cards == 3, f"Số lượng thẻ có deadline không đúng: {number_of_deadline_cards}. Kỳ vọng là 3."
    print("Test case 20 passed: Tìm thấy 3 card có deadline trong list 'Mặc định'.")
    logging.info("Test case 20 passed.")

    # Test case 29: Đặt giới hạn cho thẻ trong danh sách
    ql_list_page = QuanLyList(driver)
    ql_list_page.Click_Menu_List()
    time.sleep(1)  # Độ trễ
    ql_list_page.Add_Limit_Card_Button_Click()
    ql_list_page.Fill_Input_Limit()
    ql_list_page.Save_Button_Click()
    ql_list_page.Click_Close_Button()

    ql_card.Create_Card('limit')
    card_count = count_cards_in_list(2)  # Đếm thẻ trong danh sách thứ hai

    print(f"Số lượng thẻ hiện tại trong danh sách 'List_Test_1': {card_count}")
    logging.info(f"Số lượng thẻ hiện tại trong danh sách 'List_Test_1': {card_count}")

    list_element = driver.find_element(By.CSS_SELECTOR,
                                       "div[data-testid='list'][style*='--accent-background: var(--ds-background-warning)']")

    assert card_count == 3, f"Số lượng thẻ trong danh sách không đúng: {card_count}. Kỳ vọng là 3."
    assert list_element is not None, "Thẻ danh sách không chuyển nền thành màu vàng khi vượt quá giới hạn."

    print(f"Test case 29 passed: Danh sách chuyển sang màu ấm khi số lượng thẻ lớn hơn giới hạn {card_count} > 2.")
    logging.info(f"Test case 29 passed.")
