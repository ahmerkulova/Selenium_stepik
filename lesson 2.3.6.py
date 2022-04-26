from selenium import webdriver
from time import sleep
from math import log, sin
import pyperclip


def calc(x):
    return str(log(abs(12*sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element_by_tag_name('button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = calc(int(x_element.text))

    input = browser.find_element_by_id('answer')
    input.send_keys(x)

    button = browser.find_element_by_tag_name('button').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    pyperclip.copy(alert_text.split(': ')[-1])

finally:
    sleep(5)
    browser.quit()