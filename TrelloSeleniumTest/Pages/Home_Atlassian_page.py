from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Base.base_page import BasePage
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By

class HomeAtlassianPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.Menu = (By.XPATH, "//button[@data-testid='app-switcher-button' and @type='button']")
        self.Trello_Button = (By.XPATH, "//span[@data-testid='switcher-item__TRELLOTrello--primitive--icon-before']")

    # Chuyển từ trang chủ Atlassian sang Trello
    def Menu_Click(self):
        self.Wait_And_Click(self.Menu)

    def Trello_Click(self):
        self.Wait_And_Click(self.Trello_Button)
