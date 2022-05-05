from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    result = str(int(num1) + int(num2))  # need a string type for searching

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(result)  # find result in dropdown options

    submit = browser.find_element_by_tag_name('button')
    submit.click()

finally:
    sleep(10)
    browser.quit()