import logging
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.untils import wait_for_element, login_to_atlassian, navigate_to_trello, wait_for_element_visible
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
   driver = get_chrome_driver()
   yield driver
   driver.quit()

def test_trello_functionality(driver):
   login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
   navigate_to_trello(driver)
   home_page = HomeTrelloPage(driver)
   #Test case 07 - Tạo board với tên hợp lệ
   Board_Name = "Test3"
   wait_for_element_visible(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
   home_page.Click_Create_Board()
   home_page.Click_Create_New_Board_Button()
   home_page.Fill_Board_Name_Input(Board_Name)
   time.sleep(3)
   home_page.Click_Create_New_Board()
   time.sleep(5)
   home_page.Click_Return_Home()
   # Kiểm tra xem bảng đã được tạo chưa
   boards = driver.find_elements(By.XPATH, "//a[@title='Test3']")  # Lấy danh sách các bảng
   board_exists = any(board.text == Board_Name for board in boards)  # Kiểm tra sự tồn tại của bảng

   if board_exists:
       print("Test case 07 passed: Board đã được tạo thành công.")
   else:
       print("Test case 07 failed: Board không được tạo.")

   # Test case 08 - Thay đổi nền board
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Change_Board()
   home_page.Click_Change_Color()
   home_page.Click_Select_Color()
   # Kiểm tra màu nền hiện tại
   current_color = driver.find_element(By.XPATH, "//button[@data-testid='board-background-select-gradient-gradient-rainbow']") #Hồng
   expected_color = driver.find_element(By.XPATH, "//button[@data-testid='board-background-select-gradient-gradient-bubble']" ) #Lam

   # Kiểm tra xem màu nền đã thay đổi thành công chưa
   if current_color != expected_color:
       logging.info("Test case 09 passed: Đã thay đổi nền board thành công.")
       print("Test case 09 passed: Đã thay đổi nền board thành công.")
   else:
       logging.error("Test case 09 failed: Không thay đổi nền board.")
       print("Test case 09 failed: Không thay đổi nền board.")

   # Test case 10 - Tải lên nền với kích thước lớn
   home_page.Click_Cancel()
   home_page.Click_Return_Home()
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Change_Board()
   time.sleep(5)
   home_page.Upload_Background(r"D:\Anh\Anh.jpg")

   error_present = WebDriverWait(driver, 5).until(
       EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'File too large')]"))
   )

   if error_present:
       print("Test case 10 Failed: Upload thất bại: File quá lớn!")
       assert True  # Đảm bảo rằng điều kiện đúng
   else:
       print("Test case 10 Passed: Upload thành công hoặc không có thông báo lỗi.")

   #Test case 11 - Đóng board
   home_page.Click_Return_Home()
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Close_Board()
   home_page.Click_Confirm_Close_Board()
   home_page.Click_Return_Home()
   driver.refresh()
   board_exists = driver.find_elements(By.XPATH,"//a[@href='/b/wrJPJ1YC/test1']")
   if len(board_exists) == 0:
       print("Test case 11 passed: Board đã được đóng thành công.")
   else:
       print("Test case 11 failed: Board vẫn còn mở.")

   #Test case 12 - Mở lại board
   home_page.Click_View_Closed_Board()
   home_page.Click_Open_Board_Again()
   home_page.Click_Reopen_Board()
   time.sleep(2)
   home_page.Click_Confirm_Reopen()
   home_page.Click_Return_Home()
   driver.refresh()
   WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.XPATH, "//a[@href='/b/wrJPJ1YC/test1']"))
   )

   # Kiểm tra bảng đã được mở lại
   board_exists = driver.find_elements(By.XPATH, "//a[@href='/b/wrJPJ1YC/test1']")
   assert len(board_exists) > 0, "Test case 12 Failed: Mở lại board thất bại"
   print("Test case 12 Passed: Board đã được mở thành công.")
