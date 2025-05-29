import time
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from TrelloSeleniumTest.Pages.Register_page import RegisterPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

#Test Case 2 - Đăng ký với tên không hợp lệ
def test_register_voi_ten_khong_hop_le(driver):
    register_Page = RegisterPage(driver)
    time.sleep(10)
    register_Page.open_page("https://id.atlassian.com/signup")
    time.sleep(5)
    register_Page.enter_email("minhpham")
    register_Page.click_continue()
    time.sleep(5)

#Test case 3 - Đăng ký với email đã đăng ký trước đó
def test_register_voi_email_da_DangKy(driver):
    register_Page = RegisterPage(driver)
    time.sleep(10)
    register_Page.open_page("https://id.atlassian.com/signup")
    time.sleep(5)
    register_Page.enter_email("ngotrongnghia8424@gmail.com")
    register_Page.click_continue()
    time.sleep(5)
