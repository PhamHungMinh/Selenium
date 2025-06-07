import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Quan_Ly_Board:
    def __init__(self, driver):
        self.driver = driver
        #Test case 22
        self.Share_Button = (By.XPATH, "//button[@data-testid='board-share-button']")
        self.Email_Input = (By.XPATH, "//input[@data-testid='add-members-input']")
        self.Invite_Button = (By.XPATH, "//button[@data-testid='team-invite-submit-button']")
        #Test case 23
        self.Copy_Link_Button = (By.XPATH, "//button[@data-testid='board-invite-link-copy-button']")
        self.Close_Share_Button = (By.XPATH, "//button[@aria-label='Close']")
        self.Close_Share_Button2 = (By.XPATH, "//button[@aria-label='Đóng']")
        self.Member_Menu_Button = (By.XPATH, "//button[@data-testid='header-member-menu-button']")
        self.Log_Out_Button = (By.XPATH, "//button[@data-testid='account-menu-logout']")
        self.Login_Another_Button = (By.XPATH, "//a[text()='Log in to another account']")
        self.Add_Another_Account_Button = (By.XPATH, "//button[@id='navigate-to-login-prompt']")
        self.Join_Button = (By.XPATH, "//button[@data-testid='join-button']")
        #Test case 24
        self.Phan_Quyen_Button = (By.XPATH, "//button[@type='button' and (contains(@data-testid, 'board-visibility-option'))]")
        self.Phan_Quyen_Private_Button = (By.XPATH, "//button[.//span[contains(text(), 'Private')]]")
        self.Menu_Trello = (By.XPATH, "//button[contains(@class, 'o7EAj6bxSlZptk') and @type='button']")
        self.Trello_Home = (By.XPATH, "//a[@data-testid='switcher-item__TRELLOTrello']")
        #Test case 24
        self.Accept_Into_Private_Board_Button = (By.XPATH, "//button[@data-testid='request-access-button']")
        self.YeuCau_VaoBang_Button = (By.XPATH, "//div[@id='boardInviteModalMembersAndRequests-1' and @aria-controls='boardInviteModalMembersAndRequests-1-tab' and @role='tab']")
        self.Chon_PhanQuyen_Button = (By.XPATH, "//span[contains(text(), 'Thêm vào bảng thông tin')]")
        self.Chon_ThanhVien_Button = (By.XPATH, "//div[@class='css-c93nfn']//span[contains(text(), 'Thành viên')]")
        self.TuChoi_YeuCau_Button = (By.XPATH, "//button[@data-testid='delete-request-item-button']")
        # Test case 26
        self.Board_Click = (By.XPATH, "//a[@href='/b/wrJPJ1YC/test1' and @title='Test1']")
        self.Click_Card = (By.XPATH, "//ol[@data-testid='list-cards']")
        self.Click_Button_Menu = (By.XPATH, "//button[@data-testid='header-member-menu-button']")
        self.Close_Card = (By.XPATH, "//button[@aria-label='Close dialog']")
        # Test case 27
        self.Notification_Button = (By.XPATH, "//button[@class='o7EAj6bxSlZptk JLWAF01l7Cb26C frrHNIWnTojsww bxgKMAm3lq5BpA HAVwIqCeMHpVKh SEj5vUdI3VvxDc' and @type='button' and @data-testid='header-notifications-button' and @aria-label='0 Notifications']")

    # Test case 22
    def Share_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Share_Button)
        ).click()

    def fill_email_input(self, email):
        text_area = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Email_Input)
        )
        text_area.send_keys(email)

    def Invite_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Invite_Button)
        ).click()

    #Test case 23
    def Copy_Link_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Copy_Link_Button)
        ).click()

    def Close_Share_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Close_Share_Button)
        ).click()

    def Close_Share_Button_Click2(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Close_Share_Button2)
        ).click()

    def Member_Menu_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Member_Menu_Button)
        ).click()

    def Log_Out_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Log_Out_Button)
        ).click()

    def Login_Another_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Login_Another_Button)
        ).click()

    def Add_Another_Account_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Add_Another_Account_Button)
        ).click()

    def Join_Board_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Join_Button)
        ).click()

    #Test case 24
    def Phan_Quyen_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Phan_Quyen_Button)
        ).click()

    def Phan_Quyen_Private_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Phan_Quyen_Private_Button)
        ).click()

    def Menu_Trello_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Menu_Trello)
        ).click()

    def Trello_Home_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Trello_Home)
        ).click()

    #Test case 24
    def Accept_Into_Private_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Accept_Into_Private_Board_Button)
        ).click()

    def YeuCau_VaoBang_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.YeuCau_VaoBang_Button)
        ).click()

    def Chon_PhanQuyen_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Chon_PhanQuyen_Button)
        ).click()

    def Chon_ThanhVien_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Chon_ThanhVien_Button)
        ).click()

    #Test case 25
    def TuChoi_YeuCau_VaoBang_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TuChoi_YeuCau_Button)
        ).click()

    #Test case 26
    def Into_Board_Click(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.Board_Click)
        ).click()

    def Click_To_Card(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Click_Card)
        ).click()

    def Click_Close_Card(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Close_Card)
        ).click()

    def Menu_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Click_Button_Menu)
        ).click()

    # Test case 27
    def Check_Notification(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.Notification_Button)
        ).click()
