from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage

class QuanLyList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi hàm khởi tạo của lớp cha
        self.Create_List_Button = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div/button")
        self.Name_List = "List_Test_1"
        self.Name_Same = "List_Test_1"
        self.Name_Long = "Kế hoạch phát triển bản thân cho năm 2025 sẽ tập trung vào việc nâng cao kỹ năng và kiến thức thông qua các khóa học trực tuyến và tham gia hội thảo chuyên môn. Tôi sẽ duy trì sức khỏe bằng cách tập thể dục đều đặn và ăn uống lành mạnh. Ngoài ra, tôi cũng sẽ tham gia các hoạt động tình nguyện để giúp đỡ cộng đồng, xây dựng mối quan hệ tốt đẹp với bạn bè và đồng nghiệp. Cuối cùng, tôi sẽ lên kế hoạch tài chính cá nhân để tiết kiệm cho tương lai và đầu tư vào những cơ hội phát triển nghề nghiệp bản thân về sau"
        self.Text_Area_Name_List = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div[1]/form/textarea")
        self.Button_Create_List_With_Name = (By.XPATH, "//button[text()='Add list']")
        self.Text_Area_Xpath = "//ol[@data-testid='lists']//li[@data-testid='list-wrapper'][2]//textarea[@data-testid='list-name-textarea']"
        self.List_Edit_Menu_Button = (By.XPATH, "//li[@data-testid='list-wrapper'][2]//button[@data-testid='list-edit-menu-button']")
        self.Archive_List_Button = (By.XPATH, "//button[@data-testid='list-actions-archive-list-button']")
        self.Alert_Xpath = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div")
        self.Wait_For_Board_To_Display = "//ol[@id='board']/li[1]"
        self.List_Test_1_XPATH = "//ol[@id='board']/li[1]"
        self.Drop_XPATH = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div/button"
        # Test case 30
        self.Set_Limit_Card_Button = (By.XPATH, "//span[text()='Set list limit']")
        self.Input_Limit = (By.XPATH, "//input[@id='listLimit' and @type='number']")
        self.Save_Button = (By.XPATH, "//button[@type='submit' and @class='bxgKMAm3lq5BpA SdamsUKjxSBwGb u0Qu04nzhYsVX_ SEj5vUdI3VvxDc']")
        self.Close_Button = (By.XPATH, "//button[@aria-label='Close popover' and @class='q7bda2GIwjst4f zKzcyhLUVG0jDw']")

    def Create_List_Click(self):
        self.Wait_And_Click(self.Create_List_Button)

    def Fill_List_Name_Input(self):
        text_area = self.Wait_For_Element(self.Text_Area_Name_List)
        text_area.send_keys(self.Name_List)

    def Button_Create_List_WithName_Click(self):
        self.Wait_And_Click(self.Button_Create_List_With_Name)

    def Fill_Same_Name_List_Input(self):
        text_area = self.Wait_For_Element(self.Text_Area_Name_List)
        text_area.send_keys(self.Name_Same)

    def Fill_Long_Name_List(self):
        text_area = self.Wait_For_Element(self.Text_Area_Name_List)
        text_area.send_keys(self.Name_Long)

    def Click_Menu_List(self):
        self.Wait_And_Click(self.List_Edit_Menu_Button)

    def Archive_List_Button_Click(self):
        self.Wait_And_Click(self.Archive_List_Button)

    def Check_Alert_Message(self):
        try:
            self.Wait_For_Element(self.Alert_Xpath)
            return True  # Thông báo đã xuất hiện
        except:
            return False

    # Test case 30
    def Add_Limit_Card_Button_Click(self):
        self.Wait_And_Click(self.Set_Limit_Card_Button)

    def Fill_Input_Limit(self):
        text_area = self.Wait_For_Element(self.Input_Limit)
        text_area.send_keys("2")

    def Save_Button_Click(self):
        self.Wait_And_Click(self.Save_Button)

    def Click_Close_Button(self):
        self.Wait_And_Click(self.Close_Button)
