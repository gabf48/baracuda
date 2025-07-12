from pages.product_page import ProductPage
from utils.browser_utils import BrowserUtils
from utils.base_page import BasePage
from pages.pagination import Pagination

if __name__ == "__main__":
    driver = BrowserUtils.init_driver()
    base_page = BasePage(driver)
    pagination = Pagination(driver)
    product_page = ProductPage(driver)

    base_page.navigate_and_accept_cookies(
        "https://baracuda.ro/14-mulinete-crap")
    pagination.show_all_products()
    product_page.click_each_product_and_return()

    input("Apasă Enter pentru a închide browserul...")

