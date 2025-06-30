import time
import logging
import pytest
from TrelloSeleniumTest.Pages.Home_Trello_page import HomeTrelloPage
from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.untils import login_to_atlassian, navigate_to_trello

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Danh sách các link cần kiểm tra
LINK_TEXTS = [
    "Biểu phí",
    "Ứng dụng",
    "Blog",
    "Chính sách Bảo mật",
    "Thông báo thu thập thông tin",
    "Trợ giúp",
    "Nhà phát triển",
    "Pháp lý",
    "Thuộc tính"
]

@pytest.fixture
def driver():
   driver = get_chrome_driver()  # Chỉ lấy driver mà không unpack
   yield driver
   driver.quit()

# Test Case 30 & 31 - Broken Link Test and Open link in new tab
@pytest.mark.brokenlink
def test_Footer_Links_Broken_And_Open_In_New_Tab(driver):
    broken_links = []
    link_statuses = []  # Danh sách để lưu trạng thái link
    opened_link_statuses = []  # Danh sách để lưu trạng thái link mở trong tab mới

    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    navigate_to_trello(driver)

    home_page = HomeTrelloPage(driver)
    home_page.Click_Info_Button()
    home_page.Click_More_Info()

    # Kiểm tra từng link trong footer
    for link_text in LINK_TEXTS:
        url = home_page.Get_Link_URL(link_text)
        status = home_page.Get_Link_Status(url)
        # Ghi lại trạng thái link
        link_statuses.append(f"{link_text}: {url} - Status: {status}")
        # Kiểm tra nếu status >= 400 hoặc có lỗi
        if isinstance(status, int) and status >= 400:
            broken_links.append(f"{link_text} ({url}): HTTP {status}")
            logging.error(f"Link broken: {link_text} ({url}): HTTP {status}")
        elif isinstance(status, str) and "Error" in status:
            broken_links.append(f"{link_text} ({url}): {status}")
            logging.error(f"Link broken: {link_text} ({url}): {status}")

    # Fail test nếu có link broken
    if broken_links:
        error_message = "\n".join([f"❌ {link}" for link in broken_links])
        logging.critical(f"Found {len(broken_links)} broken links:\n{error_message}")
        pytest.fail(f"Found {len(broken_links)} broken links:\n{error_message}")

    # In ra thông tin link và trạng thái khi test case pass
    print("\n✅ Tất cả link trong footer đều hoạt động tốt!")
    print("Thông tin các link:")
    for entry in link_statuses:
        print(entry)

    # Mở từng link trong một tab mới và kiểm tra trạng thái
    for link_text in LINK_TEXTS:
        url = home_page.Get_Link_URL(link_text)
        driver.execute_script(f"window.open('{url}', '_blank');")  # Mở link trong tab mới

        # Chuyển đến tab mới
        driver.switch_to.window(driver.window_handles[-1])  # Chuyển đến tab mới
        time.sleep(2)  # Đợi một chút để trang tải

        status = home_page.Get_Link_Status(url)  # Kiểm tra trạng thái của link
        opened_link_statuses.append(f"{link_text}: {url} - Status: {status}")  # Lưu trạng thái link mở

        # Assert kiểm tra trạng thái của link
        assert status == 200, f"Link '{link_text}' with URL '{url}' is broken, status: {status}"

        driver.close()  # Đóng tab mới
        driver.switch_to.window(driver.window_handles[0])  # Quay lại tab gốc

    # In ra thông tin các link mở trong tab mới
    print("\n🔗 Thông tin các link mở trong tab mới:")
    for entry in opened_link_statuses:
        print(entry)
