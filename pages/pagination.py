from selenium.webdriver.common.by import By

class Pagination:
    def __init__(self, driver):
        self.driver = driver

    def show_all_products(self):
        self.driver.find_element(By.CSS_SELECTOR,'#pagination [type="submit"]').click()
