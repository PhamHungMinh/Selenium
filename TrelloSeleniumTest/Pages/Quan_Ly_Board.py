import os
from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage

class QuanLyBoard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Gọi hàm khởi tạo của lớp cha
        # Test case 21
        self.Share_Button = (By.XPATH, "//button[@data-testid='board-share-button']")
        self.Email_Input = (By.XPATH, "//input[@data-testid='add-members-input']")
        self.Invite_Button = (By.XPATH, "//button[@data-testid='team-invite-submit-button']")
        # Test case 22
        self.Copy_Link_Button = (By.XPATH, "//button[@data-testid='board-invite-link-copy-button']")
        self.Close_Share_Button = (By.XPATH, "//button[@aria-label='Close']")
        self.Close_Share_Button2 = (By.XPATH, "//button[@aria-label='Đóng']")
        self.Member_Menu_Button = (By.XPATH, "//button[@data-testid='header-member-menu-button']")
        self.Log_Out_Button = (By.XPATH, "//button[@data-testid='account-menu-logout']")
        self.Login_Another_Button = (By.XPATH, "//a[text()='Log in to another account']")
        self.Add_Another_Account_Button = (By.XPATH, "//button[@id='navigate-to-login-prompt']")
        self.Join_Button = (By.XPATH, "//button[@data-testid='join-button']")
        # Test case 23
        self.Visibility_Button = (By.XPATH, "//button[@type='button' and (contains(@data-testid, 'board-visibility-option'))]")
        self.Visibility_Private_Button = (By.XPATH, "//button[.//span[@data-testid='PrivateIcon']]")
        self.Menu_Trello = (By.XPATH, "//button[contains(@class, 'o7EAj6bxSlZptk') and @type='button']")
        self.Trello_Home = (By.XPATH, "//a[@data-testid='switcher-item__TRELLOTrello']")
        # Test case 24
        self.Accept_Into_Private_Board_Button = (By.XPATH, "//button[@data-testid='request-access-button']")
        self.Request_To_Board_Button = (By.XPATH, "//div[@id='boardInviteModalMembersAndRequests-1' and @aria-controls='boardInviteModalMembersAndRequests-1-tab' and @role='tab']")
        self.Select_Visibility_Button = (By.XPATH, "//span[contains(text(), 'Thêm vào bảng thông tin')]")
        self.Select_Memmber_Button = (By.XPATH, "//div[@class='css-c93nfn']//span[contains(text(), 'Thành viên')]")
        # Test case 25
        self.Deny_Request_Button = (By.XPATH, "//button[@data-testid='delete-request-item-button']")
        # Test case 26
        self.Board_Click = (By.XPATH, "//a[@href='/b/wrJPJ1YC/test1' and @title='Test1']")
        self.Click_Card = (By.XPATH, "//ol[@data-testid='list-cards']")
        self.Click_Button_Menu = (By.XPATH, "//button[@data-testid='header-member-menu-button']")
        self.Close_Card = (By.XPATH, "//button[@aria-label='Close dialog']")
        # Test case 27
        self.Notification_Button = (By.XPATH, "//button[@class='o7EAj6bxSlZptk JLWAF01l7Cb26C frrHNIWnTojsww bxgKMAm3lq5BpA HAVwIqCeMHpVKh SEj5vUdI3VvxDc' and @type='button' and @data-testid='header-notifications-button' and @aria-label='0 Notifications']")
        self.Close_Comment = (By.XPATH, "//button[.//span[@data-testid='CloseIcon']]")

    # Test case 21
    def Share_Button_Click(self):
        self.Wait_And_Click(self.Share_Button)

    def Fill_Email_Input(self, email):
        self.Wait_And_Send_Keys(self.Email_Input, email)

    def Invite_Button_Click(self):
        self.Wait_And_Click(self.Invite_Button)

    # Test case 22
    def Copy_Link_Button_Click(self):
        self.Wait_And_Click(self.Copy_Link_Button)

    def Close_Share_Button_Click(self):
        self.Wait_And_Click(self.Close_Share_Button)

    def Close_Share_Button_Click2(self):
        self.Wait_And_Click(self.Close_Share_Button2)

    def Member_Menu_Click(self):
        self.Wait_And_Click(self.Member_Menu_Button)

    def Log_Out_Click(self):
        self.Wait_And_Click(self.Log_Out_Button)

    def Login_Another_Click(self):
        self.Wait_And_Click(self.Login_Another_Button)

    def Add_Another_Account_Click(self):
        self.Wait_And_Click(self.Add_Another_Account_Button)

    def Join_Board_Button_Click(self):
        self.Wait_And_Click(self.Join_Button)

    # Test case 23
    def Visibility_Click(self):
        self.Wait_And_Click(self.Visibility_Button)

    def Visibility_Private_Click(self):
        self.Wait_And_Click(self.Visibility_Private_Button)

    def Menu_Trello_Click(self):
        self.Wait_And_Click(self.Menu_Trello)

    def Trello_Home_Click(self):
        self.Wait_And_Click(self.Trello_Home)

    # Test case 24
    def Accept_Into_Private_Board_Click(self):
        self.Wait_And_Click(self.Accept_Into_Private_Board_Button)

    def Request_Into_Board_Click(self):
        self.Wait_And_Click(self.Request_To_Board_Button)

    def Select_Visibility_Click(self):
        self.Wait_And_Click(self.Select_Visibility_Button)

    def Select_Member_Click(self):
        self.Wait_And_Click(self.Select_Memmber_Button)

    # Test case 25
    def Deny_Request_Into_Board_Click(self):
        self.Wait_And_Click(self.Deny_Request_Button)

    # Test case 26
    def Into_Board_Click(self):
        self.Wait_And_Click(self.Board_Click)

    def Click_To_Card(self):
        self.Wait_And_Click(self.Click_Card)

    def Click_Close_Card(self):
        self.Wait_And_Click(self.Close_Card)

    def Menu_Click(self):
        self.Wait_And_Click(self.Click_Button_Menu)

    # Test case 27
    def Check_Notification(self):
        self.Wait_And_Click(self.Notification_Button)
    def Click_Close_Comment(self):
        self.Wait_And_Click(self.Close_Comment)
