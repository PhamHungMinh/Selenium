import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage

#Test Case 1
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    Login_Page = LoginPage(driver)
    time.sleep(10)
    Login_Page.open_page("https://id.atlassian.com/login")
    time.sleep(5)
    Login_Page.enter_email("eoww749@gmail.com")
    Login_Page.click_continue()
    time.sleep(10)
    # Login_Page.enter_password("khongcomatkhau4654")
    # Login_Page.click_login()
     

