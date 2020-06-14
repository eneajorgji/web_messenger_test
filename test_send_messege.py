import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import names

NEW_NAME = names.get_first_name()


class SendNewMessege(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('http://kmg.hcm.pl/testowanie_poprawione')
        self.driver.find_element_by_id('userLogin').send_keys('adam442')
        self.driver.find_element_by_id('passwordLogin').send_keys('adam442')
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)
        time.sleep(3)
        assert ' Zalogowano' in self.driver.title
        time.sleep(5)

        self.driver.find_element_by_xpath(
            '//img[@src="http://kmg.hcm.pl/testowanie/images/avatars/default.jpg"]').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="messageInput"]').send_keys(
            'Hello, how is it going? Have you seen recently ', NEW_NAME, '?')

        self.driver.find_element_by_xpath('//*[@id="messageInput"]').click()
        self.driver.find_element_by_xpath('//*[@id="messageInput"]').send_keys(Keys.ENTER)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
