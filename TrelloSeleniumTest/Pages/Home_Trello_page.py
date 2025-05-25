from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = ("div.rCD_pjrvLRI_B_ > button[data-testid='header-create-menu-button']")

    def Create_Board_Click(self):
        self.driver.find_element_by_css_selector(*self.Create_Board).click()