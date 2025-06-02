# URL: https://trello.com/b/emheCK27/test
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Quan_Ly_List:
    def __init__(self, driver):
        self.driver = driver
        self.Create_List_Button = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div/button")
        self.Name_List = "List_Test_1"
        self.Name_Same = "List_Test_1"
        self.Name_Long = "Kế hoạch phát triển bản thân cho năm 2025 sẽ tập trung vào việc nâng cao kỹ năng và kiến thức thông qua các khóa học trực tuyến và tham gia hội thảo chuyên môn. Tôi sẽ duy trì sức khỏe bằng cách tập thể dục đều đặn và ăn uống lành mạnh. Ngoài ra, tôi cũng sẽ tham gia các hoạt động tình nguyện để giúp đỡ cộng đồng, xây dựng mối quan hệ tốt đẹp với bạn bè và đồng nghiệp. Cuối cùng, tôi sẽ lên kế hoạch tài chính cá nhân để tiết kiệm cho tương lai và đầu tư vào những cơ hội phát triển nghề nghiệp bản thân về sau"
        self.TextArea_Name_List = (By.XPATH,
                                   "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div[1]/form/textarea")
        self.Button_CreateList_WithName = (By.XPATH,
                                           "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/ol/div[1]/form/div/button[1]")
        self.List_edit_menu_button = (By.XPATH, "//button[@data-testid='list-edit-menu-button' and @type='button']")
        self.Archive_List_Button = (By.XPATH, "//button[@data-testid='list-actions-archive-list-button']")
        self.alert_xpath = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div")
        self.textarea_xpath = "//ol[@id='board']/li[4]//h2[@data-testid='list-name']"
        self.Cho_Bang_Hien_Thi ="//ol[@id='board']/li[1]"
        self.List_Test_1_XPATH = "//ol[@id='board']/li[1]"
        self.Drop_XPATH = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div/button"
        #Test case 30
        self.Set_Limit_card_button = (By.XPATH, "//span[text()='Set list limit']")
        self.Input_Limit = (By.XPATH, "//input[@id='listLimit' and @type='number']")
        self.Save_Button = (By.XPATH, "//button[@type='submit' and @class='bxgKMAm3lq5BpA SdamsUKjxSBwGb u0Qu04nzhYsVX_ SEj5vUdI3VvxDc']")
        self.Close_Button = (By.XPATH, "//button[@aria-label='Close popover' and @class='q7bda2GIwjst4f zKzcyhLUVG0jDw']")


    def Create_List_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_List_Button)
        ).click()

    def fill_list_name_input(self):
        # Chờ cho textarea có thể nhìn thấy và nhập tên danh sách
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TextArea_Name_List)
        )
        text_area.send_keys(self.Name_List)  # N

    def Button_CreateList_WithName_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Button_CreateList_WithName)
        ).click()

    def fill_list_ten_trung_input(self):
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TextArea_Name_List)
        )
        text_area.send_keys(self.Name_Same)

    def fill_list_ten_dai(self):
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TextArea_Name_List)
        )
        text_area.send_keys(self.Name_Long)

    def click_menu_list(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.List_edit_menu_button)
        ).click()

    def click_archive_list(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Archive_List_Button)
        ).click()

    def check_alert_message(self):
        try:
            alert_xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div"
            # Chờ cho đến khi thông báo xuất hiện
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.alert_xpath))
            return True  # Thông báo đã xuất hiện
        except:
            return False

    #Test case 30
    def click_add_limit_card_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Set_Limit_card_button)
        ).click()
    def fill_input_limit(self):
        # Chờ cho textarea có thể nhìn thấy và nhập tên danh sách
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Input_Limit)
        )
        text_area.send_keys("2")
    def click_save_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Save_Button)
        ).click()
    def click_close_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Close_Button)
        ).click()