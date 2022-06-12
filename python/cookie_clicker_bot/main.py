from selenium import webdriver
import time

chrome_driver = 'R:\Development\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.maximize_window()
driver.get('https://orteil.dashnet.org/cookieclicker/')
cookie = driver.find_element_by_id('bigCookie')

CLICKING = True
UPGRADES_UNLOCKED = False


def buy_idles():
    global UPGRADES_UNLOCKED
    products = driver.find_elements_by_class_name('product.unlocked.enabled')
    products.reverse()
    for product in products:
        try:
            product.click()
        except:
            continue
    UPGRADES_UNLOCKED = True


def buy_upgrades():
    upgrades = driver.find_elements_by_class_name('upgrade.enabled')
    for upgrade in upgrades:
        try:
            upgrade.click()
        except:
            continue


while True:
    if CLICKING:
        for _ in range(110):
            cookie.click()
        CLICKING = False
    else:
        if UPGRADES_UNLOCKED:
            buy_upgrades()
        buy_idles()
        CLICKING = True
