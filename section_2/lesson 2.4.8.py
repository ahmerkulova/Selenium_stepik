from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
from time import sleep
import pyperclip


def calc(x):
    return str(log(abs(12*sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = browser.find_element(By.ID, 'book').click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = calc(int(x_element.text))

    input = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', input)  # scroll to input
    input.send_keys(x)

    button = browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    pyperclip.copy(alert_text.split(': ')[-1])

finally:
    sleep(5)
    browser.quit()