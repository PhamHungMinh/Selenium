from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class HomeAtlassianPage:
    def __init__(self, driver):
        self.driver = driver
        self.Menu = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/header/nav/div[1]/button/span/span")
        self.Trello_Button = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div/div/div/div/div/section/div/ul/li[2]/div/div/div/a/span")

#Chuyển từ trang chủ Atlassian sang Trello
    def Menu_click(self):
        self.driver.find_element(*self.Menu).click()
    def Trello_click(self):
        self.driver.find_element(*self.Trello_Button).click()
