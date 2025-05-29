#URL: https://trello.com/b/emheCK27/test

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Quan_ly_board:
    def __init__(self, driver):
        self.driver = driver
        self.Create_List_Button = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div/button")
        self.Name_List = "List_Test_1"
        self.Name_Link = "https://docs.google.com/"
        self.TextArea_Name_List = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div[1]/form/textarea")
        self.Button_CreateList_WithName = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div/div[5]/div/div/div/div/div[2]/ol/div[1]/form/div/button[1]")

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

    def fill_list_name_link_input(self):
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TextArea_Name_List)
        )
        text_area.send_keys(self.Name_Link)