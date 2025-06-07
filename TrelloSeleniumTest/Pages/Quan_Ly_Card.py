import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuanLyCard:
    def __init__(self, driver):
        self.driver = driver
        self.Name_Card = "card test 1"
        self.Name_Link = "https://docs.google.com/"

        # XPath cho các phần tử cần thiết
        self.Create_Card_Area = (By.XPATH, "//button[@data-testid='list-add-card-button']")
        self.Input_Name_Card = (By.XPATH, "//textarea[@data-testid='list-card-composer-textarea']")
        self.Create_Card_Button = (By.XPATH, "//button[@data-testid='list-card-composer-add-card-button']")

        # XPath cho các thẻ trong danh sách thứ hai
        self.First_List_Cards = (By.XPATH, "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][1]//ol[@data-testid='list-cards']/li[@data-testid='list-card']")
        self.Second_List_Cards_With_Deadline = (By.XPATH,"//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][2]//ol[@data-testid='list-cards']/li[@data-testid='list-card' and .//div[@data-testid='card-done-state']]")
        self.FirstCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[2]/li[1]")
        self.SecondCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[2]/li[2]")
        self.ThirdCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[2]/li[3]")
        self.Edit_DeadLine = (By.XPATH, "//button//span[@data-testid='ClockIcon']/ancestor::button")
        self.Input_Date = (By.XPATH, "//input[@data-testid='due-date-field']")
        self.Input_Hour = (By.XPATH, "/html/body/div[5]/div/section/div[2]/div/div/form/div[2]/div[2]/div/div[2]/input")
        self.Button_Save_Deadline = (By.XPATH, "//button[@data-testid='save-date-button']")
        self.Close_Set_Deadline_Button = (By.XPATH, "//span[@data-testid='CloseIcon']")
        self.Ngay_Deadline = "6/1/2025"
        self.Ngay_Gan = "6/2/2025"
        self.Ngay_Xa = "10/6/2025"
        # test case 26
        self.Comment_Card = "Complete comment card"
        self.Input_Comment_Card = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/section[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]")
        self.Click_Button_Input = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/section[2]/div[2]/div/div[2]/button")
        self.Button_Save = (By.XPATH,
                            "/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/section[2]/div[2]/div/div[2]/div[2]/button")
        # test case 27
        self.Tag_User = "@"
        self.Comment_User = "Bạn làm bài tới đâu rồi hửm"
        self.Input_Tag_User = (By.XPATH, "//div[@id='ak-editor-textarea' and @contenteditable='true']")
        self.Choose_User = (By.XPATH,
                            "//div[@data-mention-item='true' and @data-mention-id='682b65bbd4dcd7cbb7f769d6']")

    def click_create_card_area(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Create_Card_Area)
        ).click()

    def fill_card_name_input(self, card_name):
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Name_Card)
        )
        text_area.send_keys(card_name)  # Nhập tên thẻ từ tham số

    def click_create_card_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Create_Card_Button)
        ).click()

    def create_card(self, card_type='short'):
        # Trình tự tạo thẻ với tên được xác định trước
        if card_type == 'short':
            card_name = self.Name_Card
        elif card_type == 'link':
            card_name = self.Name_Link
        else:
            raise ValueError("Invalid card type. Use 'short' or 'link'.")

        self.click_create_card_area()
        self.fill_card_name_input(card_name)
        self.click_create_card_button()

    def count_cards_in_list(self):
        # Đếm số lượng thẻ trong danh sách thứ hai
        cards = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.First_List_Cards)
        )
        return len(cards)

    def count_cards_with_deadline(self):
        # Đếm số lượng thẻ có deadline trong danh sách thứ hai
        cards = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.Second_List_Cards_With_Deadline)
        )
        return len(cards)

    def set_deadline(self):
        # Cận deadline
        self._set_single_deadline(self.FirstCard, self.Ngay_Deadline)
        self._set_single_deadline(self.SecondCard, self.Ngay_Gan)
        self._set_single_deadline(self.ThirdCard, self.Ngay_Xa)

    def _set_single_deadline(self, card_xpath, date):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(card_xpath)
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Edit_DeadLine)
        ).click()
        deadline = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Date)
        )
        deadline.clear()
        deadline.send_keys(date)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Button_Save_Deadline)
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Close_Set_Deadline_Button)
        ).click()

    # Test case 26
    def fill_Input_Comment_Card(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Comment_Card)
        ).send_keys(self.Comment_Card)

    def click_Button_Comment_Card(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Click_Button_Input)
        ).click()

    def Click_Button_Save(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Button_Save)
        ).click()

    # Test case 27
    def fill_tag_user(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Tag_User)
        ).send_keys(self.Tag_User)

    def click_choose_user(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Choose_User)
        ).click()

    def comment_user(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Tag_User)
        ).send_keys(self.Comment_User)
