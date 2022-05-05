from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Arina")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Merkul")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Saint P")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[@type='submit']")  # // is path, [] is filter
    button.click()

finally:
    time.sleep(30)
    browser.quit()