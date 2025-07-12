from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_and_accept_cookies(self, url, timeout=10):
        self.driver.get(url)

        try:
            cookie_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.NAME, "submit_kbcookie_law"))
            )
            cookie_button.click()
        except Exception as e:
            print(f"Cookie accept button not found or not clickable: {e}")
