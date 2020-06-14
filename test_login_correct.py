import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class LoginUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('http://kmg.hcm.pl/testowanie/index.html')
        self.driver.find_element_by_id('userLogin').send_keys('adam442')
        self.driver.find_element_by_id('passwordLogin').send_keys('adam442')
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)

        # assert 'PSTO' in self.driver.page_source
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
