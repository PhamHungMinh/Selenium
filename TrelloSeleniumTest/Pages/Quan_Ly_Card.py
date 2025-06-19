import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Base.base_page import BasePage

class QuanLyCard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi hàm khởi tạo của lớp cha
        self.Name_Card = "card test 1"
        self.Name_Link = "https://docs.google.com/"
        self.Create_Card_Area = (By.XPATH, "//li[@data-testid='list-wrapper'][.//h2/button[contains(text(), 'List_Test_1')]]//div[@data-testid='list-footer']//button[@data-testid='list-add-card-button']")
        self.Input_Name_Card = (By.XPATH, "//textarea[@data-testid='list-card-composer-textarea']")
        self.Create_Card_Button = (By.XPATH, "//button[@data-testid='list-card-composer-add-card-button']")
        self.First_List_Cards = (By.XPATH, "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][1]//ol[@data-testid='list-cards']/li[@data-testid='list-card']")
        self.Second_List_Cards_With_Deadline = (By.XPATH, "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][1]//ol[@data-testid='list-cards']/li[@data-testid='list-card' and .//div[@data-testid='card-done-state']]")
        self.FirstCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[1]/li[1]")
        self.SecondCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[1]/li[2]")
        self.ThirdCard = (By.XPATH, "(//ol[@data-testid='list-cards'])[1]/li[3]")
        self.Edit_DeadLine = (By.XPATH, "//button//span[@data-testid='ClockIcon']/ancestor::button")
        self.Input_Date = (By.XPATH, "//input[@data-testid='due-date-field']")
        self.Input_Hour = (By.XPATH, "/html/body/div[5]/div/section/div[2]/div/div/form/div[2]/div[2]/div/div[2]/input")
        self.Button_Save_Deadline = (By.XPATH, "//button[@data-testid='save-date-button']")
        self.Close_Set_Deadline_Button = (By.XPATH, "//span[@data-testid='CloseIcon']")
        self.Date_Deadline = "6/8/2025"
        self.Near_Date = "6/9/2025"
        self.Date_Away = "6/10/2025"
        # Test case 26
        self.Comment_Card = "Complete comment card"
        self.Input_Comment_Card = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/section[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]")
        self.Click_Button_Input = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/section[2]/div[2]/div/div[2]/button")
        self.Button_Save = (By.XPATH, "//button[@data-testid='card-back-comment-save-button' and text()='Save']")
        # Test case 27
        self.Tag_User = "@"
        self.Comment_User = "Bạn làm bài tới đâu rồi hửm"
        self.Input_Tag_User = (By.XPATH, "//div[@id='ak-editor-textarea' and @contenteditable='true']")
        self.Choose_User = (By.XPATH, "//div[@data-mention-item='true' and @data-mention-id='682b65bbd4dcd7cbb7f769d6']")

    def Click_Create_Card_Area(self):
        self.Wait_And_Click(self.Create_Card_Area)

    def Fill_Card_Name_Input(self, card_name):
        text_area = self.Wait_For_Element(self.Input_Name_Card)
        text_area.send_keys(card_name)

    def Click_Create_Card_Button(self):
        self.Wait_And_Click(self.Create_Card_Button)

    def Create_Card(self, card_type='short'):
        if card_type == 'nommar':
            card_name = self.Name_Card
        elif card_type == 'link':
            card_name = self.Name_Link
        elif card_type == 'limit':
            card_name = "limit"
        else:
            raise ValueError("Invalid card type. Use 'short' or 'link'.")

        self.Click_Create_Card_Area()
        self.Fill_Card_Name_Input(card_name)
        self.Click_Create_Card_Button()

    def Count_Cards_With_Deadline(self):
        # Chờ cho các thẻ có deadline xuất hiện
        cards = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.Second_List_Cards_With_Deadline)
        )
        return len(cards)

    def Set_Deadline(self):
        self.Set_Single_Deadline(self.FirstCard, self.Date_Deadline)
        self.Set_Single_Deadline(self.SecondCard, self.Near_Date)
        self.Set_Single_Deadline(self.ThirdCard, self.Date_Away)

    def Set_Single_Deadline(self, card_xpath, date):
        self.Wait_And_Click(card_xpath)
        self.Wait_And_Click(self.Edit_DeadLine)
        deadline = self.Wait_For_Element(self.Input_Date)
        deadline.clear()
        deadline.send_keys(date)
        self.Wait_And_Click(self.Button_Save_Deadline)
        self.Wait_And_Click(self.Close_Set_Deadline_Button)

    # Test case 26
    def Fill_Input_Comment_Card(self):
        self.Wait_For_Element(self.Input_Comment_Card).send_keys(self.Comment_Card)

    def Click_Button_Comment_Card(self):
        self.Wait_And_Click(self.Click_Button_Input)

    def Click_Button_Save(self):
        self.Wait_And_Click(self.Button_Save)

    # Test case 27
    def Fill_Tag_User(self):
        self.Wait_For_Element(self.Input_Tag_User).send_keys(self.Tag_User)

    def Click_Choose_User(self):
        self.Wait_And_Click(self.Choose_User)

    def Comment_User_Enter(self):
        self.Wait_For_Element(self.Input_Tag_User).send_keys(self.Comment_User)
