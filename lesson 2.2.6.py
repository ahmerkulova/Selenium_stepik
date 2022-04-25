from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12*sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector(".form-check-input[type='checkbox']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_tag_name('button').click()

finally:
    sleep(10)
    browser.quit()