from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = (By.XPATH, "//button[@data-testid='header-create-menu-button']")

    def Create_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_Board)
        ).click()
