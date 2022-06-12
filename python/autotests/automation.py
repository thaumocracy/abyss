from selenium import webdriver

chrome = webdriver.Chrome('./chromedriver')

chrome.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome.title

msg_btn = chrome.find_element_by_class_name('btn')
user_msg = chrome.find_element_by_id('user-message')
out_msg = chrome.find_element_by_id('display')

user_msg.clear()
user_msg.send_keys('TEST TEST THIS IS A TEST')

msg_btn.click()

assert 'TEST TEST THIS IS A TEST' in out_msg.text
