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
        self.Member_Menu_Button = (By.XPATH, "//button[@data-testid='header-member-menu-button']")
        self.Log_Out_Button = (By.XPATH, "//button[@data-testid='account-menu-logout']")
        self.Login_Another_Button = (By.XPATH, "//a[text()='Log in to another account']")
        self.Add_Another_Account_Button = (By.XPATH, "//button[@id='navigate-to-login-prompt']")
        self.Join_Button = (By.XPATH, "//button[@data-testid='join-button']")

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