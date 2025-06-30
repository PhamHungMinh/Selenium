from selenium import webdriver
from TrelloSeleniumTest.Base.grid_config import BROWSER_NAME, PLATFORM, GRID_HUB_URL

def get_chrome_driver():
    """Hàm để khởi tạo và trả về driver Chrome."""
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", BROWSER_NAME)
    options.set_capability("platformName", PLATFORM)
    options.set_capability("se:options", {
        "timezone": "UTC+7",
        "screenResolution": "1920x1080"
    })

    driver = webdriver.Remote(
        command_executor=GRID_HUB_URL,
        options=options
    )
    driver.maximize_window()
    return driver

def reuse_session(session_id):
    """Hàm để tái sử dụng session."""
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", BROWSER_NAME)
    options.set_capability("platformName", PLATFORM)
    options.set_capability("se:options", {
        "timezone": "UTC+7",
        "screenResolution": "1920x1080"
    })
    options.set_capability("sessionId", session_id)

    driver = webdriver.Remote(
        command_executor=GRID_HUB_URL,
        options=options
    )

    return driver





