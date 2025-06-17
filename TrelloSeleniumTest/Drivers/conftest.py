import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from TrelloSeleniumTest.Base.grid_config import BROWSER_NAME, PLATFORM


@pytest.fixture(scope="session")
def chrome_driver():
    """Fixture để khởi tạo và trả về driver Chrome."""

    options = webdriver.ChromeOptions()
    options.set_capability("browserName", BROWSER_NAME)
    options.set_capability("platformName", PLATFORM)
    options.set_capability("se:options", {
        "timezone": "UTC+7",
        "screenResolution": "1920x1080"
    })

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
