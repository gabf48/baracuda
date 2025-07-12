from selenium.webdriver.common.by import By

class Pagination:
    def __init__(self, driver):
        self.driver = driver

    def show_all_products(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.product-container .product-name')
        if len(product_elements) > 12:
            self.driver.find_element(By.CSS_SELECTOR,'#pagination [type="submit"]').click()
