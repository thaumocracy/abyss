from selenium import webdriver
from random import randint
from time import sleep

YES_BTN = 'js-profile-header-vote-yes'
LOGIN_BUTTON = 'js-signin-link'
FB_BUTTON = 'js-fbsession'
LOGGED_IN = False
RUNNING = True

chrome_driver = 'R:\Development\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.maximize_window()


def login_badoo():
    global LOGGED_IN
    base_window = driver.window_handles[0]
    driver.get('https://badoo.com/ru/')
    login = driver.find_element_by_class_name(LOGIN_BUTTON)
    login.click()
    facebook = driver.find_element_by_class_name(FB_BUTTON)
    facebook.click()
    fb_window = driver.window_handles[1]
    driver.switch_to.window(fb_window)
    email = driver.find_element_by_id('email').send_keys('iiseefire@mail.ru')
    password = driver.find_element_by_id('pass').send_keys('K%)4FwxKDrHs9rT')
    login_button = driver.find_element_by_name('login').click()
    LOGGED_IN = True
    driver.switch_to.window(base_window)


def bonk():
    sleep(randint(0, 15))
    driver.find_element_by_class_name(YES_BTN).click()
    try:
        sleep(randint(0, 15))
        element = driver.find_element_by_class_name('js-chrome-pushes-deny')
        driver.execute_script("arguments[0].click();", element)
    except:
        pass


while RUNNING:
    counter = 0
    if counter > 90:
        RUNNING = False
    if LOGGED_IN:
        sleep(randint(3, 10))
        bonk()
        counter += 1
    else:
        login_badoo()
