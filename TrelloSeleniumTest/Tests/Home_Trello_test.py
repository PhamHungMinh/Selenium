import logging
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Email, Password
from TrelloSeleniumTest.Until.utils import wait_for_element, login_to_atlassian, navigate_to_trello

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
   driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
   yield driver
   driver.quit()

@pytest.fixture
def login_and_navigate(driver):
   """Fixture để đăng nhập và điều hướng đến trang Trello."""
   login_to_atlassian(driver, Email, Password)
   navigate_to_trello(driver)
   driver.get(Trello_Url)


   # Xử lý cửa sổ bật lên nếu có
   original_window = driver.current_window_handle
   for window_handle in driver.window_handles:
       if window_handle != original_window:
           driver.switch_to.window(window_handle)
           driver.close()
           driver.switch_to.window(original_window)


   assert len(driver.window_handles) == 1
   return driver


def test_trello_functionality(login_and_navigate):
   """Chạy tất cả các test case trong một hàm."""
   drivers = login_and_navigate
   home_page = HomeTrelloPage(drivers)


   # Test case 07 - Tạo board với tên hợp lệ
   home_page.Click_Login_Button()
   wait_for_element(drivers, By.XPATH, "//button[@data-testid='header-create-menu-button']")  # XPath cho nút tạo board
   home_page.Click_Create_Board()
   home_page.Click_Create_New_Board_Button()
   home_page.Fill_Board_Name_Input()
   time.sleep(3)
   home_page.Click_Create_New_Board()
   time.sleep(5)
   home_page.Click_Return_Home()
   logging.info("Test case 07 passed: Board đã được tạo thành công.")
   print("Test case 07 passed: Board đã được tạo thành công.")
   time.sleep(1)


   # Test case 08 - Thay đổi nền board
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Change_Board()
   home_page.Click_Change_Color()
   home_page.Click_Select_Color()
   home_page.Click_Cancel()
   home_page.Click_Return_Home()
   logging.info("Test case 08 passed: Đã thay đổi nền board thành công.")
   print("Test case 08 passed: Đã thay đổi nền board thành công.")
   time.sleep(5)


   # Test case 09 - Tải lên nền với kích thước lớn
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Change_Board()
   time.sleep(5)
   home_page.Upload_Background(r"D:\Anh\Anh.jpg")


   # Kiểm tra sự xuất hiện của thông báo lỗi
   error_present = WebDriverWait(drivers, 5).until(
       EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'File too large')]"))
   )
   # Sử dụng assert để xác nhận kết quả
   assert error_present, "Upload thất bại: File quá lớn!"
   print("Test case 9 Upload thất bại: File quá lớn!")
   home_page.Click_Return_Home()


   # Test case 10 - Đóng board
   home_page.Click_Select_Board()
   home_page.Click_Open_Board_Menu()
   home_page.Click_Close_Board()
   home_page.Click_Confirm_Close_Board()
   home_page.Click_Return_Home()
   drivers.refresh()
   print("Test case 10 passed: Board đã được đóng thành công.")
   # Test case 11 - Mở lại board
   home_page.Click_View_Closed_Board()
   home_page.Click_Open_Board_Again()
   home_page.Click_Reopen_Board()
   time.sleep(3)
   home_page.Click_Confirm_Reopen()
   home_page.Click_Return_Home()
   drivers.refresh()
   print("Test case 11 passed: Board đã được mở lại thành công.")

















