from selenium import webdriver
from time import sleep
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    hidden_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    hidden_link.click()

    input1 = browser.find_element_by_tag_name('input')  # tag = <tag></tag>
    input1.send_keys("Arina")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Merkul")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Saint P")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")  # button tag inside btn class
    button.click()

finally:
    sleep(30)
    browser.quit()