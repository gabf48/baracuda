from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_each_product_and_return(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.product-container .product-name')
        product_links = [el.get_attribute("href") for el in product_elements]

        for index, link in enumerate(product_links):
            print(f"[{index + 1}/{len(product_links)}] Navighez la: {link}")
            self.driver.get(link)

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.primary_block [itemprop="name"]')))

            self.extract_title()
            self.extract_sku()
            self.extract_images_links()
            self.extract_description()

            self.driver.back()
            print()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.product-container .product-name')))

    def extract_title(self):
        title = self.driver.find_element(By.CSS_SELECTOR, '.primary_block [itemprop="name"]').text
        print(f"Title is = {title}")

    def extract_sku(self):
        sku = self.driver.find_element(By.CSS_SELECTOR, '[itemprop="sku"]').text
        print(f"SKU = {sku}")

    def extract_images_links(self):
        links = self.driver.find_elements(By.CSS_SELECTOR, '.MagicToolboxSelectorsContainer a')

        for link in links:
            href = link.get_attribute("href")
            if href and href.strip().lower().endswith(".jpg"):
                print(href)

    def extract_description(self):
        description = self.driver.find_element(By.CSS_SELECTOR, '[class="rte"]').text
        print(f'Description = {description}')


