import time
import pytest
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Quan_Ly_Board import QuanLyBoard
from TrelloSeleniumTest.Pages.Register_page import RegisterPage
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Signup_Url, Email, Password, EmailUser, PasswordUser
from TrelloSeleniumTest.Until.utils import login_to_atlassian, navigate_to_trello


@pytest.fixture
def driver():
    driver, session_id = get_chrome_driver()
    yield driver
    driver.quit()


#Test Case 2 - Đăng ký với tên không hợp lệ
def test_RegisterWithInvalidName(driver):
   register_page = RegisterPage(driver)
   register_page.Open_Page(Signup_Url)
   register_page.Fill_Email_Input("minhpham")
   register_page.Continue_Button_Click()
   error_message = register_page.Get_Error_Message()
   print(f"Lỗi hiển thị: {error_message}")
   assert "@" in error_message or "email" in error_message.lower()



def test_RegisterWithRegisteredEmail(driver):
    login_to_atlassian(driver, Email, Password)
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()

    cur_url = driver.current_url

    QLBoard = QuanLyBoard(driver)
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()

    register_page = RegisterPage(driver)
    register_page.Open_Page(Signup_Url)
    register_page.Fill_Email_Input(Email)
    register_page.Continue_Button_Click()


    error_message2 = register_page.Get_Error_Message_TC3()
    print("Thông báo lỗi thực tế:", error_message2)


    expected_vn = "bạn đã có một tài khoản"
    expected_en = "you've already got an account"


    print("Thông báo kỳ vọng (VN):", expected_vn)
    print("Thông báo kỳ vọng (EN):", expected_en)


    assert expected_vn in error_message2.lower() or expected_en in error_message2.lower(), \
       "Thông báo lỗi không khớp báo lỗi không khớp với kỳ vọng bằng tiếng Việt hoặc tiếng Anh."