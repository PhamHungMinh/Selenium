import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeTrelloPage:
    def __init__(self, driver):
        self.driver = driver
        self.Create_Board = (By.XPATH, "//button[@data-testid='header-create-menu-button']")
        self.Login = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/p/a')
        self.Create_New_Board = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/ul/li[1]")
        self.name_board = "Test2"
        self.Board_Name_Input = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/form/div[1]/label/input")
        self.create_board_button = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/form/button")
        self.Button_Into_Board = (By.XPATH,"//div[@class='EAVRQ0SLBlQrwI']/a[@title='Test']")
        self.Click_Board = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/ul/li[3]/a/div")
        self.Click_Menu_Board = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div/div[1]/div/span[2]/button[2]")
        self.Click_Change = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/ul/li[7]/button/div")
        self.Click_Change_Color = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/div[1]/button[2]/div")
        self.Click_Color = (By.XPATH, "/html/body/div[3]/div/section/div[2]/div/div/section/div/div[1]/button[1]")
        self.Click_Cancel = (By.XPATH, "/html/body/div[3]/div/section/div[2]/header/button[2]/span")
        self.Return = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div[1]/a/div")
        #self.Click_Background = (By.XPATH, "/html/body/div[4]/div/section/div[2]/div/div/section/div/div[2]/div/div[1]")
        self.input_background = (By.CSS_SELECTOR, "input[type='file'][data-testid='custom-background-uploader']")
        #Broken_Link_Test
        self.BASE_URL = "https://trello.com"
        self.FOOTER_LINKS = (By.CSS_SELECTOR, "ul.IiYlBscoXISxa9 a.Tsjb04K8H5mEwj")
        self.Thong_Tin_Button = (By.XPATH, "//button[@data-testid='header-info-button']")
        self.More_Button = (By.XPATH, "//button[contains(@class, 'FCtIkW7rM2tRmZ') and contains(@class, 'Tsjb04K8H5mEwj')]")

        self.LINK_MAPPING = {
            "Biểu phí": (By.XPATH, "//a[@href='/pricing']"),
            "Ứng dụng": (By.XPATH, "//a[@href='/platforms']"),
            "Blog": (By.XPATH, "//a[@href='https://blog.trello.com']"),
            "Chính sách Bảo mật": (By.XPATH, "//a[@href='/privacy']"),
            "Thông báo thu thập thông tin": (By.XPATH,
                                             "//a[@href='https://www.atlassian.com/legal/privacy-policy#additional-disclosures-for-ca-residents']"),
            "Trợ giúp": (By.XPATH, "//a[@href='http://help.trello.com']"),
            "Nhà phát triển": (By.XPATH, "//a[@href='https://developers.trello.com']"),
            "Pháp lý": (By.XPATH, "//a[@href='/legal']"),
            "Thuộc tính": (By.XPATH, "//a[@href='/attributions']")
        }
        #Test Work Space
        self.ThanhVien_Button = (By.XPATH, "//a[@href='/w/userkhonggianlamvic33097947/members']")
        self.Moi_Thanh_Vien_Button = (By.XPATH, "//button[contains(@class, 'bxgKMAm3lq5BpA') and contains(@class, 'SdamsUKjxSBwGb')]")
        self.Input_Email_Memmbers = (By.XPATH, "//input[@data-testid='add-members-input']")
        self.Add_Button = (By.XPATH, "//button[@type='button' and contains(@class, 'bxgKMAm3lq5BpA')]")
        self.email_list = [
            "ngotrongnghia8424@gmail.com"
            "minhnghiaseleniumtest1@gmail.com",
            "minhnghiaseleniumtest2@gmail.com",
            "minhnghiaseleniumtest3@gmail.com",
            "minhnghiaseleniumtest4@gmail.com",
            "minhnghiaseleniumtest5@gmail.com",
            "minhnghiaseleniumtest6@gmail.com",
            "minhnghiaseleniumtest7@gmail.com",
            "minhnghiaseleniumtest8@gmail.com",
            "minhnghiaseleniumtest9@gmail.com",
            "minhnghiaseleniumtest10@gmail.com"
        ]
        self.email_string =','.join(self.email_list)
    def Create_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_Board)
        ).click()

    def click_trello_login_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Login)
        ).click()

    def click_trello_create_board_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Create_New_Board)
        ).click()

    def fill_board_name_input(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Board_Name_Input)
        ).send_keys(self.name_board)

    def create_board_with_name(self):
        # Nhấp vào nút tạo board với tên đã nhập
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.create_board_button)
        ).click()

    def Into_Board_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Button_Into_Board)
        ).click()

    def click_board(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Click_Board)
        ).click()

    def click_menu_board(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Menu_Board)
        ).click()

    def click_change(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Change)
        ).click()
    def click_change_color(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Change_Color)
        ).click()
    def click_color(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Color)
        ).click()

    def click_cancel(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Click_Cancel)
        ).click()
    def click_return(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Return)
        ).click()

    def upload_background(self, file_path):
        # Kiểm tra file tồn tại
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Không tìm thấy file: {file_path}")

        # Chờ input file có mặt trên DOM
        upload_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.input_background)
        )

        # Gửi đường dẫn ảnh vào input
        upload_input.send_keys(file_path)

    #Brokne_Link_Test
    def Thong_Tin_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Thong_Tin_Button)
        ).click()
    def More_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.More_Button)
        ).click()
    def get_all_footer_links(self):
        """Lấy tất cả các link trong footer"""
        return self.driver.find_elements(*self.FOOTER_LINKS)

    def get_link_url(self, link_text):
        """Lấy URL của link dựa trên text hiển thị"""
        link = self.driver.find_element(*self.LINK_MAPPING[link_text])
        return link.get_attribute("href")

    def get_link_status(self, url):
        """Lấy HTTP status code của URL (sử dụng requests)"""
        import requests
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            return response.status_code
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    #Work space test
    def ThanhVien_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ThanhVien_Button)
        ).click()
    def Add_Email_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Moi_Thanh_Vien_Button)
        ).click()
    def Fill_Email_Input_Click(self):
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.Input_Email_Memmbers)
            ).send_keys(self.email_string)

    def Add_Button_Click(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.Add_Button)
        ).click()
