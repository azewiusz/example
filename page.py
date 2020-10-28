import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import utils
import locators

'''Page object model for Allegro's home page'''


class AllegroPage:
    # Global configuration for WaitUntil construct timeout
    TIMEOUT = 5
    # Global configuration for product list retrieval attempts
    PRODUCT_LIST_RETRY_LIMIT = 100

    def __init__(self):
        return

    def open_home_page(self, driver):
        driver.get("http://www.allegro.pl")

    def accept_consent_if_present(self, driver):
        elem = utils.wait_for_element(driver, locators.AllegroPageLocators.ACCEPT_CONSENT, self.TIMEOUT)
        # Optional element
        if elem != None:
            elem.click()

    def search_product(self, driver, product_name):
        search_textbox = utils.wait_for_element(driver, locators.AllegroPageLocators.SEARCH_BOX, self.TIMEOUT)
        search_textbox.click()
        search_textbox.clear()
        search_textbox.send_keys(product_name)
        search_textbox.send_keys(Keys.RETURN)

    def filter_products_by_color(self, driver, color):
        select_black = utils.wait_for_element(driver, locators.AllegroPageLocators.COLOR_LOCATOR(color), self.TIMEOUT)
        select_black.click()

    def select_only_phones(self, driver):
        only_phones_link = utils.wait_for_element(driver, locators.AllegroPageLocators.ONLY_PHONES_LINK, self.TIMEOUT)
        only_phones_link.click()

    def sort_results_descending(self, driver):
        select = utils.wait_for_element(driver, locators.AllegroPageLocators.DESCENDING_SORT_ORDER_DDL, self.TIMEOUT)
        select = Select(select)
        select.select_by_visible_text(locators.AllegroPageLocators.PRICE_ORDER_OPTION)

    def get_product_prices_list(self, driver, product_name, product_color):

        try:
            # Open Allegor's homepage
            self.open_home_page(driver)
            # Accept consent if present
            self.accept_consent_if_present(driver)
            # Search for given product
            self.search_product(driver, product_name)
            # Wait for page to load
            utils.wait_for_page_to_load(driver)

            # Ensures that Pagination elelemnt is present
            utils.wait_for_element(driver, locators.AllegroPageLocators.PAGINATION_CONTROL, self.TIMEOUT)

            # Ensure that only Phones category is selected
            self.select_only_phones(driver)

            # Choose phone color
            self.filter_products_by_color(driver, product_color)

            # waits for page to load
            utils.wait_for_page_to_load(driver)

            # Apply descending ordering by price
            self.sort_results_descending(driver)

            # Wait for page to load
            utils.wait_for_page_to_load(driver)

            # Here we use fragment of page and regexp search to find objects that are candidates to phone prices
            # This search is based on assumption that mainly phone prices are present + some random price objects
            pattern = re.compile(locators.AllegroPageLocators.PRICE_PLACEHOLDER_REGEXP)
            currency = ''
            page_data = None
            local_retry = 0
            while (page_data == None or len(page_data) <= 0) and local_retry < self.PRODUCT_LIST_RETRY_LIMIT:
                # find element that to date of writing this script holds list of phones
                element_for_analysis = utils.wait_for_element(driver,
                                                              locators.AllegroPageLocators.ITEMS_CONTAINER,
                                                              self.TIMEOUT)
                # extract html raw data of entire products list
                page_data = utils.get_element_inner_html(driver, element_for_analysis);
                # apply regexp search
                match = pattern.finditer(page_data)
                phone_prices = []
                counts = 0
                for obj in match:
                    # extract currency name
                    currency = obj.groups()[4]
                    # parse price from regexp, convert to float
                    phone_prices.append(float((obj.groups()[0] + "." + obj.groups()[3]).replace(' ', '')))
                    counts = counts + 1
                # endd of iteration, apply while condition to decide whether we should proceed further

            match = pattern.finditer(page_data)
            phone_prices = []
            counts = 0
            for obj in match:
                phone_prices.append(float((obj.groups()[0] + "." + obj.groups()[3]).replace(' ', '')))
                counts = counts + 1
            local_retry = local_retry + 1

        except Exception as e:
            phone_prices = []
            currency = ""

        phone_prices.sort(reverse=True)
        return [phone_prices, currency]

    def get_product_price_list_with_retry(self, driver, product_name, product_color, retry_count):
        product_prices_list = []
        result = []
        counter = 0
        while (product_prices_list == None or len(product_prices_list) == 0) and counter <= retry_count:
            print("Attempt " + str(counter + 1) + " out of " + str(retry_count))
            result = self.get_product_prices_list(driver, product_name, product_color)
            product_prices_list = result[0]
            counter = counter + 1
        return result
