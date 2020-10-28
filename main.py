from selenium import webdriver
from page import AllegroPage

'''
Script tested with Chrome Driver v86 and GeckoDriver on Windows Python v3.7.2
 - requires selenium package to be installed using e.g. pip command
 - requires chromedriver to be installed, ideally provide path to driver exe/so file in webdriver constructor below
Procedure:
Reteat below until succesfull loading of price list or retry_count exceeded
    1. Go to web page www.allegro.pl
    2. Type in search box 'Iphone 11'
    3. Select black color 'czarny'
    4. Display in console number of presented phones on the first page
    5. Look for most expensive price and display it to console
    6. Add 23% to most expensive phone, [Here I decided to display it]
'''


def main():
    # Retry count for obtaining price list from Allegor's results page
    # In case of failure it will repeat procedure up to rety_count times
    retry_count = 10
    # Here you need to set path to constructor if is not available related configuration ev variable - PATH
    driver = webdriver.Chrome('C:\gecko\chromedriver.exe')
    # driver = webdriver.Firefox(executable_path=r'C:\gecko\geckodriver.exe')
    allegro = AllegroPage()
    [products_price_list, currency] = allegro.get_product_price_list_with_retry(driver, "Iphone 11", "czarny",
                                                                                retry_count)
    print("Total products found on first page : " + str(len(products_price_list)))
    if len(products_price_list) > 0:
        print("Most expensive price : " + str("{:.2f}".format(products_price_list[0])) + currency)
        print("Most expensive price + 23% VAT : " + str("{:.2f}".format(products_price_list[0] * 1.23)) + currency)
    else:
        print("Could not get price list")
    driver.close()


if __name__ == "__main__":
    main()
