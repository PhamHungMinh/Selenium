# untils.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage

def __init__(self, driver):
    self.Driver = driver

def wait_for_element(driver, by, value):
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((by, value)))
def wait_for_element_visible(driver, by, value, timeout=15):
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

def login_to_atlassian(driver, email, password):
    login_page = LoginPage(driver)
    driver.get("https://id.atlassian.com/login")
    wait_for_element(driver, By.XPATH, "//div[@role='presentation' and @data-testid='username-container']")
    login_page.Fill_Email(email)
    login_page.Continue_Button_Click()

    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(password)
    login_page.Continue_Button_Click()

def navigate_to_trello(driver):
    atlassian_page = HomeAtlassianPage(driver)
    home_page = HomeTrelloPage(driver)

    atlassian_page.Menu_Click()
    atlassian_page.Trello_Click()
    driver.get("https://trello.com/u/ngotrongnghia8424/boards")

    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            driver.close()  # Đóng cửa sổ mới
            driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc

    # Đảm bảo chỉ có một cửa sổ mở
    assert len(driver.window_handles) == 1
    home_page.Click_Login_Button()

def open_and_close_tabs(driver, urls):
   """
   Mở mỗi URL trong một tab mới, xử lý xong thì đóng, quay về tab chính.
   """
   if not urls:
       print("⚠️ Không có URL nào để mở.")
       return


   # Mở tab đầu tiên
   driver.get(urls[0])
   time.sleep(2)
   original_window = driver.current_window_handle


   for url in urls[1:]:
       # Mở tab mới
       driver.execute_script("window.open('');")
       time.sleep(1)

       # Lấy handle tab mới và chuyển sang
       new_tab = [wh for wh in driver.window_handles if wh != original_window][-1]
       driver.switch_to.window(new_tab)

       # Mở URL trong tab mới
       driver.get(url)
       time.sleep(2)

       # CHUYỂN LẠI VỀ TAB GỐC TRƯỚC khi đóng tab hiện tại
       driver.switch_to.window(original_window)

       # Bây giờ mới được đóng tab kia (sau khi đã chuyển đi)
       driver.execute_script(f"window.close('{new_tab}');")  # hoặc driver.switch_to.window(new_tab); driver.close()
       time.sleep(0.5)

   # Đảm bảo về lại tab gốc
   driver.switch_to.window(original_window)
   print("✅ Đã xử lý và đóng các tab phụ.")

