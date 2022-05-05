from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import math
import time


@pytest.fixture
def browser():
    print('\nstarting browser')
    browser = webdriver.Chrome()
    yield browser
    print('\nquiting browser')
    print(f'Feedback = {*TestFeedback.special_feedback,}')
    browser.quit()


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898',
                                    '236899', '236903', '236904', '236905'])
class TestFeedback:
    special_feedback = []

    def test_collect_special_feedback(self, browser, lesson):
        browser.get(f'https://stepik.org/lesson/{lesson}/step/1')
        browser.implicitly_wait(10)
        input_for_answer = browser.find_element(By.CLASS_NAME, 'textarea')
        input_for_answer.send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()

        feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        correct_feedback = 'Correct!'
        if feedback != correct_feedback:
            self.special_feedback.append(feedback)
        assert feedback == correct_feedback, f'{lesson} feedback is "{feedback}" instead of "{correct_feedback}"'


if __name__ == "__main__":
    pytest.main()
