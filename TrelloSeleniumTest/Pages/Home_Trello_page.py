from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = (By.XPATH, "//button[@data-testid='header-create-menu-button']")
        self.Login = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/p/a')
        self.Create_New_Board = (By.XPATH, "/html/body/div[3]/div[3]/section/div[2]/div/div/ul/li[1]/button/span/span")
        self.name_board = "Test"
        self.Board_Name_Input = (By.XPATH, "/html/body/div[3]/div[3]/section/div[2]/div/form/div[1]/label/input")
        self.create_board_button = (By.XPATH, "/html/body/div[3]/div[3]/section/div[2]/div/form/button")
        self.Button_Into_Board = (By.XPATH,"//div[contains(@class, 'EAVRQ0SLBlQrwI')]//a[@href='/b/6jkUMfhu/test' and @title='Test']")


    def Create_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_Board)
        ).click()

    def click_trello_login_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Login)
        ).click()

    def click_trello_create_board_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_New_Board)
        ).click()

    def fill_board_name_input(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Board_Name_Input)
        ).send_keys(self.name_board)

    def create_board_with_name(self):
        # Nhấp vào nút tạo board với tên đã nhập
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.create_board_button)
        ).click()

    def Into_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Button_Into_Board)
        ).click()