import os
import requests
from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.Create_Board_Button = (By.XPATH, "//button[@data-testid='header-create-menu-button']")
        self.Login_Button = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/p/a')
        self.Create_New_Board_Button = (By.XPATH, "//button[@data-testid='header-create-board-button' and contains(., 'Create board')]")
        self.Board_Name = "Test3"
        self.Board_Name_Input = (By.XPATH, "//input[@data-testid='create-board-title-input']")
        self.Create_Board_Submit_Button = (By.XPATH, "//button[@data-testid='create-board-submit-button']")
        self.Enter_Board_Button = (By.XPATH, "//a[@title='Test']")
        # Test case 09
        self.Select_Board = (By.XPATH, "//a[@href='/b/wrJPJ1YC/test1']")
        self.Open_Board_Menu = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[1]/div/span[2]/button[2]")
        self.Change_Board_Button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/ul/li[7]/button/div")
        self.Change_Color_Button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/div[1]/button[2]/div")
        self.Select_Color_Button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/ul[1]/li[1]/button")
        self.Cancel_Button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/header/button[2]/span")
        self.Return_Home_Button = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div[1]/a/div")
        # Test case 10
        self.Background_Input = (By.CSS_SELECTOR, "input[type='file']")
        # Test case 11
        self.Close_Board_Button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/ul/li[20]/button")
        self.Confirm_Close_Board_Button = (By.XPATH, "/html/body/div[3]/div[4]/section/div[2]/div/button")
        # Test case 12
        self.View_Closed_Board_Button = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/button")
        self.Open_Board_Again_Button = (By.XPATH, "//a[@href='/b/wrJPJ1YC']")
        self.Reopen_Board_Button = (By.XPATH, "//button[@data-testid='workspace-chooser-trigger-button']")
        self.Confirm_Reopen_Button = (By.XPATH, "//button[@data-testid='workspace-chooser-reopen-button']")
        self.Exit_Button = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div/header/button/span/span")
        # Broken Link Test - Open link in new tab test
        self.Base_URL = "https://trello.com"
        self.Footer_Links = (By.CSS_SELECTOR, "ul.IiYlBscoXISxa9 a.Tsjb04K8H5mEwj")
        self.Info_Button = (By.XPATH, "//button[@data-testid='header-info-button']")
        self.More_Info_Button = (By.XPATH, "//button[text()='More…']")
        self.Link_Mapping = {
            "Biểu phí": (By.XPATH, "//a[@href='/pricing']"),
            "Ứng dụng": (By.XPATH, "//a[@href='/platforms']"),
            "Blog": (By.XPATH, "//a[@href='https://blog.trello.com']"),
            "Chính sách Bảo mật": (By.XPATH, "//a[@href='/privacy']"),
            "Thông báo thu thập thông tin": (By.XPATH, "//a[@href='https://www.atlassian.com/legal/privacy-policy#additional-disclosures-for-ca-residents']"),
            "Trợ giúp": (By.XPATH, "//a[@href='http://help.trello.com']"),
            "Nhà phát triển": (By.XPATH, "//a[@href='https://developers.trello.com']"),
            "Pháp lý": (By.XPATH, "//a[@href='/legal']"),
            "Thuộc tính": (By.XPATH, "//a[@href='/attributions']")
        }
        # Test Limit Work Space
        self.Member_Button = (By.XPATH, "//a[@href='/w/userkhonggianlamvic33097947/members']")
        self.Add_Member_Button = (By.XPATH, "//button[text()='Invite Workspace members']")
        self.Email_Input_Members = (By.XPATH, "//input[@data-testid='add-members-input']")
        self.Submit_Add_Button = (By.XPATH, "//button[@type='button' and contains(@class, 'bxgKMAm3lq5BpA')]")
        self.Email_List = [
            "minhnghiaseleniumtest1@gmail.com",
            "minhnghiaseleniumtest2@gmail.com",
            "minhnghiaseleniumtest3@gmail.com",
            "minhnghiaseleniumtest4@gmail.com",
            "minhnghiaseleniumtest5@gmail.com",
            "minhnghiaseleniumtest6@gmail.com",
            "minhnghiaseleniumtest7@gmail.com",
            "minhnghiaseleniumtest8@gmail.com",
            "minhnghiaseleniumtest9@gmail.com",
            "minhnghiaseleniumtest10@gmail.com",
            ""
        ]
        self.Email_String = ','.join(self.Email_List)
        # Test case 23
        self.Members_Button_23 = (By.XPATH, "//a[@href='/w/userkhonggianlamvic65690210/members']")
        self.Add_Member_23_Button = (By.XPATH, "//button[.//span[@data-testid='AddMemberIcon']]")
        self.Member_Input_23 = (By.XPATH, "//input[@data-testid='add-members-input']")
        self.Send_Invite_Button_23 = (By.XPATH, "//button[span[text()='Gửi lời mời']]")
        self.Close_Add_Member_Button_23 = (By.XPATH, "//button[@data-testid='ws-invite-modal-close-button']")
        self.Close_Member_WS_Button_23 = (By.XPATH, "//span[@data-testid='CloseIcon']/ancestor::button")
        self.Work_Space_Button = (By.XPATH, "//span[text()='Work Space Test']")
        self.Boards_Button = (By.XPATH, "//span[text()='Boards']")
        self.Close_Personal_Manager_Button = (By.XPATH, "//span[@data-testid='CloseIcon']")
        # Test case 24
        self.Menu_Button = (By.XPATH, "//span[contains(@class, 'DweEFaF5owOe02') and contains(@class, 'S7RWiPL9Qgl9P9')]")


    # Test case 07
    def Click_Create_Board(self):
        self.Wait_And_Click(self.Create_Board_Button)

    def Click_Login_Button(self):
        self.Wait_And_Click(self.Login_Button)

    def Click_Create_New_Board_Button(self):
        self.Wait_And_Click(self.Create_New_Board_Button)

    def Fill_Board_Name_Input(self,board_name):
        self.Wait_And_Send_Keys(self.Board_Name_Input,board_name)

    def Click_Create_New_Board(self):
        self.Wait_And_Click(self.Create_Board_Submit_Button)

    def Click_Enter_Board(self):
        self.Wait_And_Click(self.Enter_Board_Button)

    # Test case 08
    def Click_Select_Board(self):
        self.Wait_And_Click(self.Select_Board)

    def Click_Open_Board_Menu(self):
        self.Wait_And_Click(self.Open_Board_Menu)

    def Click_Change_Board(self):
        self.Wait_And_Click(self.Change_Board_Button)

    def Click_Change_Color(self):
        self.Wait_And_Click(self.Change_Color_Button)

    def Click_Select_Color(self):
        self.Wait_And_Click(self.Select_Color_Button)

    def Click_Cancel(self):
        self.Wait_And_Click(self.Cancel_Button)

    def Click_Return_Home(self):
        self.Wait_And_Click(self.Return_Home_Button)

    # Test case 10
    def Upload_Background(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Không tìm thấy file: {file_path}")
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Background_Input)
        )
        self.driver.execute_script("arguments[0].style.display = 'block';", upload_input)
        upload_input.send_keys(file_path)

    def Click_Close_Board(self):
        self.Wait_And_Click(self.Close_Board_Button)

    def Click_Confirm_Close_Board(self):
        self.Wait_And_Click(self.Confirm_Close_Board_Button)

    # Test case 10-12
    def Click_View_Closed_Board(self):
        self.Wait_And_Click(self.View_Closed_Board_Button)

    def Click_Reopen_Board(self):
        self.Wait_And_Click(self.Reopen_Board_Button)

    def Click_Open_Board_Again(self):
        self.Wait_And_Click(self.Open_Board_Again_Button)

    def Click_Confirm_Reopen(self):
        self.Wait_And_Click(self.Confirm_Reopen_Button)

    def Click_Info_Button(self):
        self.Wait_And_Click(self.Info_Button)

    # Broken Link Test - Open link in new tab test
    def Click_More_Info(self):
        self.Wait_And_Click(self.More_Info_Button)

    def Get_All_Footer_Links(self):
        """Lấy tất cả các link trong footer"""
        return self.driver.find_elements(*self.Footer_Links)

    def Get_Link_URL(self, link_text):
        """Lấy URL của link dựa trên text hiển thị"""
        link = self.driver.find_element(*self.Link_Mapping[link_text])
        return link.get_attribute("href")

    def Get_Link_Status(self, url):
        """Lấy HTTP status code của URL (sử dụng requests)"""
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            return response.status_code
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    # Test Limit Work Space
    def Click_Member_Button(self):
        self.Wait_And_Click(self.Member_Button)

    def Click_Add_Member_Button(self):
        self.Wait_And_Click(self.Add_Member_Button)

    def Fill_Email_Input_Members(self):
        self.Wait_And_Send_Keys(self.Email_Input_Members, self.Email_String)

    def Click_Submit_Add_Button(self):
        self.Wait_And_Click(self.Submit_Add_Button)

    #Test case 23
    def Click_View_Members_23(self):
        self.Wait_And_Click(self.Members_Button_23)

    def Click_Add_Member_23(self):
        self.Wait_And_Click(self.Add_Member_23_Button)

    def Fill_Email_Member_Input_Click_23(self):
        self.Wait_And_Send_Keys(self.Member_Input_23, "minhnghiaseleniumtest2@gmail.com,")

    def Click_Send_Invite_Button_23(self):
        self.Wait_And_Click(self.Send_Invite_Button_23)

    def Click_Close_Add_Member_Button_23(self):
        self.Wait_And_Click(self.Close_Add_Member_Button_23)

    def Click_Close_Member_WS_Button(self):
        self.Wait_And_Click(self.Close_Member_WS_Button_23)

    def Click_Work_Space_23(self):
        self.Wait_And_Click(self.Work_Space_Button)

    def Click_Boards_23(self):
        self.Wait_And_Click(self.Boards_Button)

    def Click_Close_MN_PS_Button(self):
        self.Wait_And_Click(self.Close_Personal_Manager_Button)

    #Test case 24
    def Click_Menu_Account_Button(self):
        self.Wait_And_Click(self.Menu_Button)