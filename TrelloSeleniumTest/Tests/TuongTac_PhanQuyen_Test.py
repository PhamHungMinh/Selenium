import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Pages.Login_page import LoginPage
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Pages.Quan_Ly_Board import QuanLyBoard
from TrelloSeleniumTest.Pages.Quan_Ly_Card import QuanLyCard
from TrelloSeleniumTest.Until.utils import wait_for_element, login_to_atlassian, navigate_to_trello
from TrelloSeleniumTest.Base.config import Login_Url, Trello_Url, Email, Password, EmailUser, PasswordUser

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
Find_User = "@nghiangotrng3"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def run_all_test_cases(driver):
    # Test case 21: Invite Member To Board
    login_to_atlassian(driver, Email, Password)
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    home_page.Click_Enter_Board()
    QLBoard = QuanLyBoard(driver)
    QLBoard.Share_Button_Click()
    QLBoard.Fill_Email_Input("0306221443@caothang.edu.vn,")
    QLBoard.Invite_Button_Click()
    time.sleep(2)
    QLBoard.Invite_Button_Click()
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    member_count = len(member_elements)
    email_found = any(Find_User in member.find_element(By.XPATH, ".//div[@class='Nb2wVffRyPwsUc']//div").text for member in member_elements)
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email("0306221443@caothang.edu.vn")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password("Nghia842004@")
    login_page.Login_Button_Click()
    wait_for_element(driver, By.XPATH, "//a[@href='/b/6jkUMfhu/test']")

    # Assert kết quả
    if member_count == 2 and email_found and driver.find_element(By.XPATH, "//a[@href='/b/6jkUMfhu/test']"):
        print("Test case 21 PASS: Số lượng thành viên là 2, tìm thấy email mời và phần tử đã xuất hiện.")
    else:
        print("Test case 21 FAIL: Không đáp ứng điều kiện.")

    # Test case 22: Member Request To Join Board
    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()
    QLBoard.Close_Share_Button_Click()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email("minhnghiaseleniumtest1@gmail.com")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    wait_for_element(driver, By.XPATH, "//button[@data-testid='header-create-menu-button']")
    new_url = "https://trello.com/invite/b/683728efeaab183d8b373c79/ATTIa4b2533b9eda91cff5b218e40978919eF170FF1B/test"
    driver.execute_script(f"window.location.href = '{new_url}';")
    driver.refresh()
    QLBoard.Join_Board_Button_Click()
    QLBoard.Share_Button_Click()
    member_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO")))
    child_divs = parent_div.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")
    user_member_count = len(child_divs)
    user_name_found = any("Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text for member in child_divs)
    QLBoard.Close_Share_Button_Click2()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email("minhnghiaseleniumtest1@gmail.com")
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    home_page.Click_Enter_Board()
    QLBoard.Share_Button_Click()
    member_elements_admin = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='member-item']")
    parent_div_admin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.avIXKTMFqNSYgO")))
    child_divs_admin = parent_div_admin.find_elements(By.CSS_SELECTOR, "div.wFehm16heN83eQ")
    admin_member_count = len(child_divs_admin)
    admin_name_found = any("Tester001" in member.find_element(By.CSS_SELECTOR, "span[data-testid='member-list-item-full-name']").text for member in child_divs_admin)

    # Assert kết quả
    if user_member_count == 3 and user_name_found and admin_member_count == 3 and admin_name_found:
        print("Test case 22 PASS: User và Admin member counts đều chính xác và tên đã được tìm thấy.")
    else:
        print("Test case 22 FAIL: Không đáp ứng điều kiện.")

    # Test case 26: Member Comment Success
    QLBoard.Close_Share_Button_Click2()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email( EmailUser)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(PasswordUser)
    login_page.Login_Button_Click()

    home_page = HomeTrelloPage(driver)
    QLBoard = QuanLyBoard(driver)
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    QL_Card = QuanLyCard(driver)
    QL_Card.Click_Button_Comment_Card()
    QL_Card.Fill_Input_Comment_Card()
    QL_Card.Click_Button_Save()
    QLBoard.Click_Close_Card()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    home_page.Click_Enter_Board()
    QLBoard.Click_To_Card()
    time.sleep(10)
    comments_xpath = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"
    comments = driver.find_elements(By.XPATH, comments_xpath)

    if comments:
        first_comment = comments[0].find_element(By.XPATH, ".//div[contains(@class, 'ak-renderer-wrapper')]//p").text
        print(f"Test case 26 PASS: Có {len(comments)} bình luận mới. Bình luận mới nhất: {first_comment}")
    else:
        print("Test case 26 FAIL: Không có bình luận mới.")

    # Test case 27: Member Comment Tag User
    login_to_atlassian(driver, EmailUser, PasswordUser)
    navigate_to_trello(driver)
    home_page = HomeTrelloPage(driver)
    QLBoard = QuanLyBoard(driver)
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    QL_Card = QuanLyCard(driver)
    QL_Card.Click_Button_Comment_Card()
    QL_Card.Fill_Tag_User()
    QL_Card.Click_Choose_User()
    time.sleep(1)
    QL_Card.Comment_User_Enter()
    QL_Card.Click_Button_Save()
    QLBoard.Click_Close_Card()
    QLBoard.Member_Menu_Click()
    QLBoard.Log_Out_Click()
    QLBoard.Login_Another_Click()
    QLBoard.Add_Another_Account_Click()
    login_page = LoginPage(driver)
    wait_for_element(driver, By.ID, "username")
    login_page.Fill_Email(Email)
    login_page.Continue_Button_Click()
    wait_for_element(driver, By.ID, "password")
    login_page.Fill_Password(Password)
    login_page.Login_Button_Click()
    QLBoard.Into_Board_Click()
    QLBoard.Click_To_Card()
    comments_xpath2 = "//ul[@class='FZdsp70kDqEsB8']/li[@data-testid='card-back-action']"
    comments = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, comments_xpath2)))

    if comments:
        latest_comment = comments[0].find_element(By.XPATH, ".//div[@class='TTb5N2DgAn9VHs']//p").text
        print(f"Test case 27 PASS: Có {len(comments)} bình luận mới. Bình luận mới nhất: {latest_comment}")
    else:
        print("Test case 27 FAIL: Không có bình luận mới.")

# Chạy tất cả các test case
def test_all_cases(driver):
    run_all_test_cases(driver)
