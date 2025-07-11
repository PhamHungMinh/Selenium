# test_trello.py

# Import Required Libraries
import time
import logging
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from TrelloSeleniumTest.Until.untils import login_to_atlassian, navigate_to_trello
import requests

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Setup WebDriver
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Region: Các hàm kiểm tra SEO
def check_title(driver):
    try:
        title = driver.title
        title_length = len(title)
        print(f"📏 Độ dài tiêu đề: {title_length} ký tự")
        if 30 < title_length < 60:
            print("✅ Title Tag: Passed")
        else:
            print(f"❌ Tiêu đề nên từ 30-60 ký tự (Hiện tại: {title_length})")
    except Exception as e:
        print(f"❌ Không tìm thấy tiêu đề trang")


def check_meta_description(driver):
    try:
        meta_desc = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
        desc_length = len(meta_desc)
        print(f"📏 Độ dài meta description: {desc_length} ký tự")
        if 50 < desc_length < 160:
            print("✅ Meta Description: Passed")
        else:
            print(f"❌ Meta description nên từ 50-160 ký tự (Hiện tại: {desc_length})")
    except Exception as e:
        print(f"❌ Không tìm thấy thẻ mô tả")


def check_heading_structure(driver):
    print("\n=== KIỂM TRA CẤU TRÚC HEADING ===")
    headings = {f'h{i}': driver.find_elements(By.TAG_NAME, f'h{i}') for i in range(1, 7)}

    # Kiểm tra H1
    h1_count = len(headings['h1'])
    status = "✅" if h1_count == 1 else "❌"
    print(f"{status} Số H1: {h1_count}")

    # Phân tích thứ tự heading
    prev_level = 0
    for h_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        current_headings = headings[h_tag]
        current_level = int(h_tag[1])
        if current_headings:
            print(f"🔍 {h_tag.upper()} ({len(current_headings)}): {[heading.text for heading in current_headings]}")

        for heading in current_headings:
            if current_level - prev_level > 1:
                print(f"❌ Lỗi thứ tự: {h_tag.upper()} sau H{prev_level}")
            prev_level = current_level


def check_internal_links(driver):
    print("\n=== KIỂM TRA LIÊN KẾT NỘI BỘ ===")
    links = driver.find_elements(By.TAG_NAME, "a")
    internal_links = [link.get_attribute("href") for link in links if
                      link.get_attribute("href") and link.get_attribute("href").startswith(driver.current_url)]

    broken_links = []
    for url in internal_links:
        try:
            with requests.head(url, allow_redirects=True) as response:
                if 400 <= response.status_code < 500:
                    broken_links.append(url)
        except Exception as e:
            print(f"❌ Lỗi khi kiểm tra liên kết: {url} - {str(e)}")

    if broken_links:
        print(f"❌ Phát hiện {len(broken_links)} liên kết lỗi 4xx:")
        for link in broken_links:
            print(f"🔗 {link}")
    else:
        print("✅ Không có liên kết nội bộ nào bị lỗi 4xx.")


def check_images_alt(driver):
    print("\n=== KIỂM TRA ẢNH THIẾU ALT ===")
    images = driver.find_elements(By.TAG_NAME, "img")
    missing_alt = [img for img in images if not img.get_attribute("alt")]

    if missing_alt:
        print(f"❌ Phát hiện {len(missing_alt)} ảnh thiếu alt:")
        for img in missing_alt:
            print(f"📷 {img.get_attribute('src')}")
    else:
        print("✅ Tất cả ảnh đều có thuộc tính alt hợp lệ")


def run_seo_checks(driver):
    print("\n=== BẮT ĐẦU KIỂM TRA SEO ===")

    # Các kiểm tra cơ bản
    check_title(driver)
    check_meta_description(driver)

    # Kiểm tra cấu trúc
    check_heading_structure(driver)

    # Kiểm tra liên kết
    check_internal_links(driver)

    # Kiểm tra media
    check_images_alt(driver)

    print("=== KẾT THÚC KIỂM TRA SEO ===\n")


# EndRegion

# Test case chính
def test_seo_checks(driver):
    logging.info("Đang đăng nhập vào Atlassian...")
    login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
    time.sleep(5)

    print("=== KIỂM TRA SEO TRANG ĐẦU TIÊN ===")
    run_seo_checks(driver)

    logging.info("Đang điều hướng đến trang Trello Home...")
    navigate_to_trello(driver)
    time.sleep(5)

    print("=== KIỂM TRA SEO TRANG TRELLO HOME ===")
    run_seo_checks(driver)


if __name__ == "__main__":
    pytest.main()
