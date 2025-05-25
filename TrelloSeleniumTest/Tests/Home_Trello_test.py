import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_Create_Board_voi_ten_hop_le(driver):
    Login_Page = LoginPage(driver)
    AtlassianPage = HomeAtlassianPage(driver)
    HomePage = HomeTrelloPage(driver)

    time.sleep(5)
    Login_Page.open_page("https://id.atlassian.com/login")
    time.sleep(5)
    Login_Page.enter_email("ngotrongnghia8424@gmail.com")
    Login_Page.click_continue()
    time.sleep(2)
    Login_Page.enter_password("khongcomatkhau4654")
    Login_Page.click_login()
    time.sleep(5)

    time.sleep(5)
    AtlassianPage.Menu_click()
    time.sleep(3)
    AtlassianPage.Trello_click()
    time.sleep(5)
    HomePage.Create_Board_Click()
    time.sleep(5)