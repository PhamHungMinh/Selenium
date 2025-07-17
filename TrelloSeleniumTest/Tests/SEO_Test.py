import time
import logging
import re
import pytest
import requests
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor

from TrelloSeleniumTest.Drivers.Chrome_Driver import get_chrome_driver
from TrelloSeleniumTest.Until.untils import open_and_close_tabs

# Cấu hình logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Thiết lập console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Thiết lập file handler với encoding utf-8
file_handler = logging.FileHandler('seo_checks.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
   driver = get_chrome_driver()
   yield driver
   driver.quit()


# Danh sách URL Trello
trello_urls = [
    "https://trello.com/teams/engineering",
    "https://trello.com/webinars",
    "https://trello.com/",
    "https://trello.com/butler-automation",
    "https://trello.com/teams/remote-team-management",
    "https://trello.com/integrations",
    "https://trello.com/integrations/sales-support",
]


# Hàm kiểm tra SEO
def check_meta_description(driver):
    """Kiểm tra meta description."""
    try:
        meta_desc = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content")
        desc_length = len(meta_desc)
        message = f"📏 Độ dài meta description: {desc_length} ký tự"
        logger.info(message)
        print(message)
        if 50 < desc_length < 160:
            message = "✅ Meta Description: Passed"
            logger.info(message)
            print(message)
        else:
            message = f"❌ Meta description nên từ 50-170 ký tự (Hiện tại: {desc_length})"
            logger.warning(message)
            print(message)
    except Exception as e:
        message = f"❌ Không tìm thấy thẻ mô tả: {str(e)}"
        logger.error(message)
        print(message)


import re
import requests
from urllib.parse import urljoin

def check_internal_links(driver, url):
    """Kiểm tra các liên kết lỗi trong thẻ <script>."""
    print(f"\n=== 🔍 KIỂM TRA LIÊN KẾT LỖI TRONG TRANG {url}===")
    base_url = driver.current_url
    scripts = driver.find_elements(By.TAG_NAME, "script")

    script_links = []

    for script in scripts:
        src = script.get_attribute("src")
        if src:
            full_url = urljoin(base_url, src)
            script_links.append(full_url)
        else:
            content = script.get_attribute("innerHTML") or ""
            found_links = re.findall(r'https?://[^\s\'"<>]+', content)
            script_links.extend(found_links)

    broken_links = []

    for url in script_links:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                broken_links.append((url, response.status_code))
        except Exception as e:
            broken_links.append((url, f"Lỗi kết nối: {str(e)}"))

    if broken_links:
        print(f"\n❌ Đã phát hiện {len(broken_links)} liên kết lỗi trong thẻ <script>:")
        for url, status in broken_links:
            print(f"   - {url} ➜ {status}")
    else:
        print("✅ Không có liên kết lỗi nào trong thẻ <script>.")



def check_images_alt(driver):
    """Kiểm tra ảnh thiếu thuộc tính alt."""
    images = driver.find_elements(By.TAG_NAME, "img")
    missing_alt = [img.get_attribute('src') for img in images if not img.get_attribute("alt")]

    if missing_alt:
        message = f"❌ Phát hiện {len(missing_alt)} ảnh thiếu alt:"
        logger.error(message)
        print(message)
        for src in missing_alt:
            message = f"📷 {src}"
            logger.error(message)
            print(message)
    else:
        message = "✅ Tất cả ảnh đều có thuộc tính alt hợp lệ"
        logger.info(message)
        print(message)


def check_canonical(driver):
    """Kiểm tra thẻ Canonical."""
    try:
        canonical = driver.find_element(By.CSS_SELECTOR, 'link[rel="canonical"]')
        current_url = driver.current_url
        if canonical.get_attribute('href') != current_url:
            message = f"❌ Canonical sai: {canonical.get_attribute('href')} vs {current_url}"
            logger.error(message)
            print(message)
        if not canonical.get_attribute('href').startswith('https://'):
            message = "❌ Canonical dùng HTTP thay vì HTTPS"
            logger.error(message)
            print(message)
    except Exception:
        message = "❌ Thiếu thẻ canonical"
        logger.error(message)
        print(message)


def check_headers(url):
    """Kiểm tra Security Headers."""
    try:
        response = requests.get(url)
        headers = response.headers
        missing = [header for header in ['X-Frame-Options', 'Content-Security-Policy', 'Referrer-Policy'] if
                   header not in headers]

        if missing:
            message = f"❌ Thiếu headers bảo mật: {', '.join(missing)}"
            logger.error(message)
            print(message)
    except Exception as e:
        message = f"❌ Lỗi khi kiểm tra headers: {str(e)}"
        logger.error(message)
        print(message)


def run_seo_checks(driver, url):
    """Chạy tất cả các kiểm tra SEO cho một URL."""
    logger.info(f"\n=== BẮT ĐẦU KIỂM TRA SEO CHO: {url} ===")
    print(f"\n=== BẮT ĐẦU KIỂM TRA SEO CHO: {url} ===")

    driver.get(url)  # Mở URL
    time.sleep(2)  # Đợi một chút để trang tải

    check_meta_description(driver)
    check_headers(url)
    check_canonical(driver)

    # Kiểm tra các liên kết trong thẻ <script>
    script_links = []
    base_url = driver.current_url
    scripts = driver.find_elements(By.TAG_NAME, "script")

    for script in scripts:
        src = script.get_attribute("src")
        if src:
            full_url = urljoin(base_url, src)
            script_links.append(full_url)

    check_internal_links(driver, script_links)

    # Kiểm tra media
    check_images_alt(driver)

    logger.info("=== KẾT THÚC KIỂM TRA SEO ===\n")
    print("=== KẾT THÚC KIỂM TRA SEO ===\n")


# Test case chính
def test_seo_checks(driver):
    """Kiểm tra SEO cho tất cả các trang Trello."""
    for url in trello_urls:
        run_seo_checks(driver, url)


if __name__ == "__main__":
    pytest.main()