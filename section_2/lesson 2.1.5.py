from selenium import webdriver
import time
import math

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector(".form-check-input[type='checkbox']")
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()