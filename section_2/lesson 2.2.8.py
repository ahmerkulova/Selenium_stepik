from selenium import webdriver
from time import sleep
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys('Arina')
    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys('Merkul')
    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys('arina@hello.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson 2.2.8_ex.txt')
    file_button = browser.find_element_by_css_selector('#file')
    file_button.send_keys(file_path)

    button = browser.find_element_by_tag_name('button').click()

finally:
    sleep(5)
    browser.quit()