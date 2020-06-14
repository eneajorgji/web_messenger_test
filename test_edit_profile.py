import unittest
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

NEW_NAME = names.get_first_name()


class EditProfile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('http://kmg.hcm.pl/testowanie/index.html')
        self.driver.find_element_by_id('userLogin').send_keys('adam442')
        self.driver.find_element_by_id('passwordLogin').send_keys('adam442')
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)
        time.sleep(3)
        assert ' Zalogowano' in self.driver.title
        time.sleep(3)

        self.driver.find_element_by_xpath('//img[@src="./icon_profile.png"]').click()
        time.sleep(3)

        self.driver.find_element_by_id('editOSobie').click()
        self.driver.find_element_by_id('editOSobie').send_keys(
            'For the reason of test I used the module of the name, so I would be able to check whether this section has been changed ',
            NEW_NAME)
        time.sleep(3)

        self.driver.find_element_by_id('editBttn').click()
        time.sleep(5)

        assert 'Dane ' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()