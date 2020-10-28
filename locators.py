from selenium.webdriver.common.by import By


class AllegroPageLocators:
    # Locators
    ACCEPT_CONSENT = (By.XPATH, '//button[@data-role="accept-consent"]')
    SEARCH_BOX = (By.XPATH, '//input[@type="search"]')
    ONLY_PHONES_LINK = (By.XPATH, '//a[contains(@data-custom-params,"telefo")]')
    DESCENDING_SORT_ORDER_DDL = (By.XPATH, '//select[option and contains(.,"najwyższej")]')
    PAGINATION_CONTROL = (By.XPATH, '//div[@data-role="pagination-counter"]')
    ITEMS_CONTAINER = (By.XPATH, '//div[contains(@data-box-name,"items container") and count(div)> 0]')
    # Regexps
    PRICE_PLACEHOLDER_REGEXP = r'([0-9 ]+)(,)(<span class=\"[_a-zA-Z0-9]+\">)([0-9]{2})( zł)(<\/span>)'

    # Option labels
    PRICE_ORDER_OPTION = "cena: od najwyższej"

    @staticmethod
    def COLOR_LOCATOR(color):
        return (By.XPATH, '//label[span/text()="' + color + '"]/span')
