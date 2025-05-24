from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Register_page import RegisterPage

#Test Case 2
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_register_voi_ten_khong_hop_le(driver):
    register_Page = RegisterPage(driver)
    time.sleep(10)
    register_Page.open_page("https://id.atlassian.com/signup")
    time.sleep(5)
    register_Page.enter_email("ngotrongnghia8424@gmail.com")
    register_Page.click_continue()
    time.sleep(5)