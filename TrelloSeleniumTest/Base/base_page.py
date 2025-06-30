from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def Wait_And_Click(self, locator, timeout=30):
        """Chờ cho phần tử hiển thị và nhấp vào nó."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def Wait_And_Send_Keys(self, locator, keys, timeout=20):
        """Chờ cho phần tử hiển thị và gửi keys vào nó."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(keys)

    def Wait_For_Element(self, locator, timeout=20):
        """Chờ cho phần tử hiển thị và trả về phần tử đó."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
