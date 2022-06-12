from selenium import webdriver

wish_list = [
    'https://www.dns-shop.ru/product/d3be14fc84433332/14-noutbuk-lenovo-ideapad-5-14are05-seryj/',
    'https://www.dns-shop.ru/product/9947a5e3caab3120/zasitnye-ocki-sp-glasses-comfort-af024/',
    'https://www.dns-shop.ru/product/69dd57a03edd1b80/zasitnye-ocki-gunnar-vertex-smoke/'
]

chrome_driver = 'R:\Development\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.maximize_window()


def check_wishlist(wishlist):
    items = []
    for item in wishlist:
        driver.get(item)
        price = driver.find_element_by_class_name('product-buy__price')
        print(price.text)
    driver.close()


check_wishlist(wish_list)

# driver.quit()
