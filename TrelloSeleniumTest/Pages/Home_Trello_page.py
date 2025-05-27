from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = (By.XPATH, "//button[@data-testid='header-create-menu-button']")
        self.Login = (By.XPATH, '//html/body/div[1]/div[2]/div[1]/div/main/div/div/div[2]/div/div/p/a')  # Đây là một locator
        self.Create_New_Board =(By.XPATH,"/html/body/div[23]/div/section/div[2]/div/div/ul/li[1]/button/div")


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
