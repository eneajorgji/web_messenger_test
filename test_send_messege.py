import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NEW_NAME = names.get_first_name()


class SendNewMessege(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://kmg.hcm.pl/testowanie/index.html')
        self.driver.implicitly_wait(10)

    def test_login_msg(self):
        self.driver.find_element_by_id('userLogin').send_keys('adam442')
        self.driver.find_element_by_id('passwordLogin').send_keys('adam442')
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        self.driver.element = wait.until(EC.title_contains('PSTO webMessenger - Zalogowano'))

        assert 'PSTO webMessenger - Zalogowano' in self.driver.title

        self.driver.find_element_by_xpath(
            '//img[@src="http://kmg.hcm.pl/testowanie/images/avatars/default.jpg"]').click()

        self.driver.find_element_by_xpath('//*[@id="messageInput"]').send_keys(
            'Hello, how is it going? Have you seen recently ', NEW_NAME, '?')

        self.driver.find_element_by_xpath('//*[@id="messageInput"]').click()
        self.driver.find_element_by_xpath('//*[@id="messageInput"]').send_keys(Keys.ENTER)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
