import logging
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
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

# Test case 07
def test_Create_Board_With_Valid_Name(driver):
  login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
  navigate_to_trello(driver)
  home_page = HomeTrelloPage(driver)
  # Mở URL để tạo board mới
  driver.get(Trello_Url)




  # Lưu ID của cửa sổ gốc
  original_window = driver.current_window_handle




  # Kiểm tra và đóng các cửa sổ khác nếu có
  for window_handle in driver.window_handles:
      if window_handle != original_window:
          driver.switch_to.window(window_handle)
          driver.close()  # Đóng cửa sổ mới
          driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc




  # Đảm bảo chỉ có một cửa sổ mở
  assert len(driver.window_handles) == 1
  # Đợi cho nút tạo board hiển thị và nhấp vào
  home_page.Click_Login_Button()




  wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")  # XPath cho nút tạo board
  home_page.Click_Create_Board()
  home_page.Click_Create_New_Board_Button()
  home_page.Fill_Board_Name_Input()
  time.sleep(3)
  home_page.Click_Create_New_Board()
  time.sleep(3)
  home_page.Click_Return_Home()
  logging.info("Test case passed: Board đã được tạo thành công.")




# Test case 09
def test_Change_BackGround_Board(driver):
  login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
  navigate_to_trello(driver)
  home_page = HomeTrelloPage(driver)


  # Mở URL để tạo board mới
  driver.get(Trello_Url)


  # Lưu ID của cửa sổ gốc
  original_window = driver.current_window_handle




  # Kiểm tra và đóng các cửa sổ khác nếu có
  for window_handle in driver.window_handles:
      if window_handle != original_window:
          driver.switch_to.window(window_handle)
          driver.close()  # Đóng cửa sổ mới
          driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc




  # Đảm bảo chỉ có một cửa sổ mở
  assert len(driver.window_handles) == 1
  # Đợi cho nút tạo board hiển thị và nhấp vào
  home_page.Click_Login_Button()
  home_page.Click_Select_Board()
  home_page.Click_Open_Board_Menu()
  home_page.Click_Change_Board()
  home_page.Click_Change_Color()
  home_page.Click_Select_Color()
  home_page.Click_Cancel()
  logging.info("Test case passed: Đã thay đổi nền board thành công.")




# Test case 10
def test_Load_BackGround_Large_Size(driver):
  login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
  navigate_to_trello(driver)
  home_page = HomeTrelloPage(driver)
  # Mở URL để tạo board mới
  driver.get(Trello_Url)




  # Lưu ID của cửa sổ gốc
  original_window = driver.current_window_handle




  # Kiểm tra và đóng các cửa sổ khác nếu có
  for window_handle in driver.window_handles:
      if window_handle != original_window:
          driver.switch_to.window(window_handle)
          driver.close()  # Đóng cửa sổ mới
          driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc




  # Đảm bảo chỉ có một cửa sổ mở
  assert len(driver.window_handles) == 1
  # Đợi cho nút tạo board hiển thị và nhấp vào
  home_page.Click_Login_Button()
  home_page.Click_Select_Board()
  home_page.Click_Open_Board_Menu()
  home_page.Click_Change_Board()
  time.sleep(5)
  home_page.Upload_Background(r"D:\Anh\Anh.jpg")




  # Kiểm tra sự xuất hiện của thông báo lỗi
  error_present = WebDriverWait(driver, 5).until(
      EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'File too large')]"))
  )




  # Sử dụng assert để xác nhận kết quả
  assert error_present, "Upload thất bại: File quá lớn!"
  logging.info("Test case passed: Upload thành công: Không có lỗi!")
  time.sleep(3)




# Test case 11
def test_Archive_Board(driver):
  login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
  navigate_to_trello(driver)
  home_page = HomeTrelloPage(driver)
  # Mở URL để tạo board mới
  driver.get(Trello_Url)




  # Lưu ID của cửa sổ gốc
  original_window = driver.current_window_handle




  # Kiểm tra và đóng các cửa sổ khác nếu có
  for window_handle in driver.window_handles:
      if window_handle != original_window:
          driver.switch_to.window(window_handle)
          driver.close()  # Đóng cửa sổ mới
          driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc




  # Đảm bảo chỉ có một cửa sổ mở
  assert len(driver.window_handles) == 1
  # Đợi cho nút tạo board hiển thị và nhấp vào
  home_page.Click_Login_Button()
  home_page.Click_Select_Board()
  home_page.Click_Open_Board_Menu()
  home_page.Click_Close_Board()
  home_page.Click_Confirm_Close_Board()
  home_page.Click_Return_Home()
  driver.refresh()
  logging.info("Test case passed: Board đã được lưu trữ thành công.")




# Test case 12
def test_Reopen_Board(driver):
  login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
  navigate_to_trello(driver)
  home_page = HomeTrelloPage(driver)
  # Mở URL để tạo board mới
  driver.get(Trello_Url)




  # Lưu ID của cửa sổ gốc
  original_window = driver.current_window_handle




  # Kiểm tra và đóng các cửa sổ khác nếu có
  for window_handle in driver.window_handles:
      if window_handle != original_window:
          driver.switch_to.window(window_handle)
          driver.close()  # Đóng cửa sổ mới
          driver.switch_to.window(original_window)  # Quay lại cửa sổ gốc




  # Đảm bảo chỉ có một cửa sổ mở
  assert len(driver.window_handles) == 1
  # Đợi cho nút tạo board hiển thị và nhấp vào
  home_page.Click_Login_Button()
  home_page.Click_View_Closed_Board()
  home_page.Click_Open_Board_Again()
  home_page.Click_Reopen_Board()
  home_page.Click_Confirm_Reopen()
  home_page.Click_Return_Home()
  driver.refresh()
  logging.info("Test case passed: Board đã được mở lại thành công.")











