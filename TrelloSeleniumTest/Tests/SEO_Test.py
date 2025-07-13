import time
import logging
import pytest
import requests
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from TrelloSeleniumTest.Until.untils import login_to_atlassian, navigate_to_trello
from selenium.webdriver.support.wait import WebDriverWait

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

def check_headings(driver):
   """Kiểm tra và liệt kê các thẻ heading (H1, H2, H3, ...) trên trang."""
   try:
       # ========== PHẦN THÊM MỚI ==========
       SEO_STANDARDS = {
           'H1': 70,  # Tiêu chuẩn độ dài 2025
           'H2': 80,
           'H3': 100,
           'H4': 120,
           'H5': 120,
           'H6': 120
       }

       headings = driver.find_elements(By.CSS_SELECTOR, 'h1, h2, h3, h4, h5, h6')
       heading_texts = [heading.text for heading in headings]

       # Kiểm tra và liệt kê thẻ H1 trong <noscript>
       noscript_h1 = driver.execute_script(
           "return document.querySelector('noscript') ? document.querySelector('noscript').innerHTML : '';"
       )
       if '<h1>' in noscript_h1:
           start_index = noscript_h1.index('<h1>') + len('<h1>')
           end_index = noscript_h1.index('</h1>')
           noscript_h1_text = noscript_h1[start_index:end_index]
           heading_texts.append(noscript_h1_text)

       if heading_texts:
           print("✅ Các thẻ heading phát hiện:")
           for heading in headings:
               tag_name = heading.tag_name.upper()
               heading_text = heading.text.strip()

               text_length = len(heading_text)
               length_status = "✅" if text_length <= SEO_STANDARDS[
                   tag_name] else f"❌ VƯỢT {text_length - SEO_STANDARDS[tag_name]} ký tự"

               print(f"{tag_name}: {heading_text} (class: {heading.get_attribute('class')})")
               print(f"   Độ dài: {text_length}/{SEO_STANDARDS[tag_name]} chars - {length_status}")  # Thêm dòng này

           if '<h1>' in noscript_h1:
               noscript_h1_text = noscript_h1_text.strip()
               # ========== PHẦN THÊM MỚI ==========
               noscript_length = len(noscript_h1_text)
               noscript_status = "✅" if noscript_length <= SEO_STANDARDS[
                   'H1'] else f"❌ NGUY CƠ PENALTY ({noscript_length} chars)"

               print(f"H1 (trong noscript): {noscript_h1_text}")
               print(f"   Độ dài: {noscript_length}/{SEO_STANDARDS['H1']} chars - {noscript_status}")  # Thêm dòng này
       else:
           print("❌ Không phát hiện thẻ heading nào.")

       # Kiểm tra số lượng H2
       h2_count = len(driver.find_elements(By.CSS_SELECTOR, 'h2'))
       if h2_count == 0:
           print("\n❌ Thiếu thẻ H2.")
       else:
           print(f"\n✅ Phát hiện {h2_count} thẻ H2.")

       # Kiểm tra thứ tự H1 với H2
       h1_elements = driver.find_elements(By.TAG_NAME, 'h1')
       if h1_elements:
           h1 = h1_elements[0]
           previous_elements = driver.execute_script('return arguments[0].previousElementSibling;', h1)

           if previous_elements and 'h2' in previous_elements.tag_name.lower():
               print("\n✅ H1 đứng trước H2.")
           else:
               print("\n❌ H1 không đứng trước H2.")

       print("\n📊 Báo cáo tổng quan:")
       total_violations = sum(1 for h in headings if len(h.text.strip()) > SEO_STANDARDS[h.tag_name.upper()])
       print(f"- Tỷ lệ heading đạt chuẩn: {(len(headings) - total_violations) / len(headings) * 100:.1f}%")
       print(f"- Heading dài nhất: {max(len(h.text.strip()) for h in headings)} chars")
       # ===================================

   except Exception as e:
       print(f"\n❌ Có lỗi xảy ra khi kiểm tra các thẻ heading: {str(e)}")

def check_canonical(driver):
   """1. Kiểm tra thẻ Canonical (STT1,32)"""
   try:
       canonical = driver.find_element(By.CSS_SELECTOR, 'link[rel="canonical"]')
       current_url = driver.current_url
       if canonical.get_attribute('href') != current_url:
           print(f"❌ Canonical sai: {canonical.get_attribute('href')} vs {current_url}")
       if not canonical.get_attribute('href').startswith('https://'):
           print("❌ Canonical dùng HTTP thay vì HTTPS")
   except:
       print("❌ Thiếu thẻ canonical")

def check_headers(url):
   """2. Kiểm tra Security Headers (STT2,21,27)"""
   with requests.get(url) as res:
       headers = res.headers
       missing = []
       if 'X-Frame-Options' not in headers: missing.append('X-Frame-Options')
       if 'Content-Security-Policy' not in headers: missing.append('Content-Security-Policy')
       if 'Referrer-Policy' not in headers: missing.append('Referrer-Policy')
       if missing:
           print(f"❌ Thiếu headers bảo mật: {', '.join(missing)}")

def run_seo_checks(driver):
   print("\n=== BẮT ĐẦU KIỂM TRA SEO ===")

   # Các kiểm tra cơ bản
   check_title(driver)
   check_meta_description(driver)

   # Kiểm tra cấu trúc
   check_heading_structure(driver)

  # Kiểm tra các yếu tố SEO bổ sung
   check_headings(driver)
   check_headers(driver.current_url)
   check_canonical(driver)

   # Kiểm tra liên kết
   check_internal_links(driver)

   # Kiểm tra media
   check_images_alt(driver)

   print("=== KẾT THÚC KIỂM TRA SEO ===\n")

# Test case chính
def test_seo_checks(driver):
   logging.info("Đang đăng nhập vào Atlassian...")
   login_to_atlassian(driver, "ngotrongnghia8424@gmail.com", "khongcomatkhau4654")
   time.sleep(5)

   print("=== KIỂM TRA SEO TRANG HOME ATLASSIAN ===")
   run_seo_checks(driver)

   logging.info("Đang điều hướng đến trang Trello Home...")
   navigate_to_trello(driver)
   time.sleep(5)

   print("=== KIỂM TRA SEO TRANG TRELLO HOME ===")
   run_seo_checks(driver)

if __name__ == "__main__":
   pytest.main()
