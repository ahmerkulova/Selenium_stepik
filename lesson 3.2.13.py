from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestInputData(unittest.TestCase):
    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        browser.find_element(By.CSS_SELECTOR, '.first:required').send_keys('Текст в обязательном поле')
        browser.find_element(By.CSS_SELECTOR, '.second:required').send_keys('Текст в обязательном поле')
        browser.find_element(By.CSS_SELECTOR, '.third:required').send_keys('Текст в обязательном поле')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        actual_welcome_text = welcome_text_elt.text
        correct_welcome_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(actual_welcome_text, correct_welcome_text, f'Incorrect welcome text: {actual_welcome_text} instead of {correct_welcome_text}')
        browser.quit()


    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)

        browser.find_element(By.CSS_SELECTOR, '.first:required').send_keys('Текст в обязательном поле')
        browser.find_element(By.CSS_SELECTOR, '.second:required').send_keys('Текст в обязательном поле')
        browser.find_element(By.CSS_SELECTOR, '.third:required').send_keys('Текст в обязательном поле')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        actual_welcome_text = welcome_text_elt.text
        correct_welcome_text = 'Congratulations! You have successfully registered!'

        self.assertEqual(actual_welcome_text, correct_welcome_text,
                         f'Incorrect welcome text: {actual_welcome_text} instead of {correct_welcome_text}')
        browser.quit()

if __name__ == "__main__":
    unittest.main()