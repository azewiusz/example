from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(driver, locator, timeout):
    try:
        ignored_exceptions = []  # (NoSuchElementException, StaleElementReferenceException,)
        last_element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located(locator))
       
        return last_element
    except TimeoutException:
        print("Loading took too much time - do not worry I'm making another attempt")
    return None


def get_element_inner_html(driver, element):
    return driver.execute_script("return arguments[0].innerHTML;", element)


def wait_for_page_to_load(driver):
    wait = WebDriverWait(driver, 60);
    wait.until(lambda driver: (driver.execute_script("return document.readyState") == "complete"))
