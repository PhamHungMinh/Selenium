import pytest
import pymsgbox
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Home_Atlassian_page import HomeAtlassianPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Email, Password
from TrelloSeleniumTest.Until.utils import *
from TrelloSeleniumTest.Until.utils import wait_for_element

@pytest.fixture
def driver():
   # Khởi tạo trình duyệt
   driver = get_chrome_driver()  # Sử dụng hàm từ chrome_driver.py
   yield driver
   driver.quit()


#Test case 07
def test_Create_Board_With_Valid_Name(driver):
   Login_Page = LoginPage(driver)
   AtlassianPage = HomeAtlassianPage(driver)
   HomePage = HomeTrelloPage(driver)


   # Mở trang đăng nhập
   Login_Page.Open_Page(Login_Url)


   # Đợi cho phần tử email hiển thị và nhập email
   wait_for_element(driver, By.ID, "username")  # ID cho trường email
   Login_Page.Fill_Email(Email)
   Login_Page.Continue_Button_Click()


   # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
   wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
   Login_Page.Fill_Password(Password)
   Login_Page.Login_Button_Click()


   AtlassianPage.Menu_Click()
   AtlassianPage.Trello_Click()


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
   HomePage.Click_Login_Button()


   wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")  # XPath cho nút tạo board
   HomePage.Click_Create_Board()
   HomePage.Click_Create_New_Board_Button()
   HomePage.Fill_Board_Name_Input()
   time.sleep(5)
   HomePage.Click_Create_New_Board()
   time.sleep(5)
   HomePage.Click_Return_Home()
   time.sleep(10)


#Test case 09
def test_Change_BackGround_Board(driver):
   Login_Page = LoginPage(driver)
   AtlassianPage = HomeAtlassianPage(driver)
   HomePage = HomeTrelloPage(driver)


   # Mở trang đăng nhập
   Login_Page.Open_Page(Login_Url)
   # Đợi cho phần tử email hiển thị và nhập email
   wait_for_element(driver, By.ID, "username")  # ID cho trường email
   Login_Page.Fill_Email(Email)
   Login_Page.Continue_Button_Click()


   # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
   wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
   Login_Page.Fill_Password(Password)
   Login_Page.Login_Button_Click()


   AtlassianPage.Menu_Click()
   AtlassianPage.Trello_Click()


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
   HomePage.Click_Login_Button()
   HomePage.Click_Select_Board()
   HomePage.Click_Open_Board_Menu()
   HomePage.Click_Change_Board()
   HomePage.Click_Change_Color()
   HomePage.Click_Select_Color()
   HomePage.Click_Cancel()




# Test case 10
def test_Load_BackGround_Large_Size(driver):
   Login_Page = LoginPage(driver)
   AtlassianPage = HomeAtlassianPage(driver)
   HomePage = HomeTrelloPage(driver)


   # Mở trang đăng nhập
   Login_Page.Open_Page(Login_Url)


   # Đợi cho phần tử email hiển thị và nhập email
   wait_for_element(driver, By.ID, "username")  # ID cho trường email
   Login_Page.Fill_Email(Email)
   Login_Page.Continue_Button_Click()


   # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
   wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
   Login_Page.Fill_Password(Password)
   Login_Page.Login_Button_Click()


   AtlassianPage.Menu_Click()
   AtlassianPage.Trello_Click()
   # time.sleep(500)


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
   HomePage.Click_Login_Button()
   HomePage.Click_Select_Board()
   HomePage.Click_Open_Board_Menu()
   HomePage.Click_Change_Board()
   time.sleep(5)
   HomePage.Upload_Background(r"D:\Anh\Anh.jpg")
   # Kiểm tra sự xuất hiện của thông báo lỗi
   error_present = WebDriverWait(driver, 5).until(
       EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'File too large')]"))
   )

   # Sử dụng assert để xác nhận kết quả
   assert error_present, "Upload thất bại: File quá lớn!"

   # Nếu không có lỗi, xác nhận upload thành công
   assert True, "Upload thành công: Không có lỗi!"


#Test case 11
def test_Archive_Board(driver):
   Login_Page = LoginPage(driver)
   AtlassianPage = HomeAtlassianPage(driver)
   HomePage = HomeTrelloPage(driver)
   Login_Page.Open_Page(Login_Url)
   wait_for_element(driver, By.ID, "username")
   Login_Page.Fill_Email(Email)
   Login_Page.Continue_Button_Click()


   # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
   wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
   Login_Page.Fill_Password(Password)
   Login_Page.Login_Button_Click()


   AtlassianPage.Menu_Click()
   AtlassianPage.Trello_Click()
   # time.sleep(500)


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
   HomePage.Click_Login_Button()
   HomePage.Click_Select_Board()
   HomePage.Click_Open_Board_Menu()
   HomePage.Click_Close_Board()
   HomePage.Click_Confirm_Close_Board()
   HomePage.Click_Return_Home()
   driver.refresh()


#Test case 12
def test_Reopen_Board(driver):
   Login_Page = LoginPage(driver)
   AtlassianPage = HomeAtlassianPage(driver)
   HomePage = HomeTrelloPage(driver)
   Login_Page.Open_Page(Login_Url)
   wait_for_element(driver, By.ID, "username")
   Login_Page.Fill_Email(Email)
   Login_Page.Continue_Button_Click()


   # Đợi cho phần tử mật khẩu hiển thị và nhập mật khẩu
   wait_for_element(driver, By.ID, "password")  # ID cho trường mật khẩu
   Login_Page.Fill_Password(Password)
   Login_Page.Login_Button_Click()


   AtlassianPage.Menu_Click()
   AtlassianPage.Trello_Click()


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
   HomePage.Click_Login_Button()
   HomePage.Click_View_Closed_Board()
   HomePage.Click_Open_Board_Again()
   HomePage.Click_Reopen_Board()
   HomePage.Click_Confirm_Reopen()
   HomePage.Click_Return_Home()
   driver.refresh()

