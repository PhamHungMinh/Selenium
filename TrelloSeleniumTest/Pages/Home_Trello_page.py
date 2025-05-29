from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = (By.XPATH, "//button[@data-testid='header-create-menu-button']")
        self.Login = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/p/a')
        self.Create_New_Board = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/ul/li[1]")
        self.name_board = "Test2"
        self.Board_Name_Input = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/form/div[1]/label/input")
        self.create_board_button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/form/button")
        self.Button_Into_Board = (By.XPATH,"//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        self.Click_Board = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[3]/a/div")
        self.Click_Menu_Board = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[1]/div/span[2]/button[2]")
        self.Click_Change = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/ul/li[7]/button/div")
        self.Click_Change_Color = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/div[1]/button[2]/div")
        self.Click_Color = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/div[1]/button[1]")
        self.Click_Cancel = (By.XPATH, "/html/body/div[3]/div/section/div[2]/header/button[2]/span")
        self.Return = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div[1]/a/div")


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

    def click_board(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Click_Board)
        ).click()

    def click_menu_board(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Menu_Board)
        ).click()

    def click_change(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Change)
        ).click()
    def click_change_color(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Change_Color)
        ).click()
    def click_color(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Color)
        ).click()

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Cancel)
        ).click()
    def click_return(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Return)
        ).click()