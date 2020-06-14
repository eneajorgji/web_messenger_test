import unittest
from selenium import webdriver
import time
import names  # generates different name

NEW_NAME = names.get_first_name()


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_navigate(self):  # zmien nazwe
        self.driver.get('http://kmg.hcm.pl/testowanie/register.html')
        # used module names to generate different name each time test runs
        self.driver.find_element_by_id('username').send_keys(NEW_NAME)
        time.sleep(2)
        self.driver.find_element_by_id('pass1').send_keys('Test123')
        self.driver.find_element_by_id('pass2').send_keys('Test123')
        self.driver.find_element_by_id('name').send_keys('Name1')
        self.driver.find_element_by_id('surname').send_keys('Surname1')
        self.driver.find_element_by_id('kodgrupy').send_keys('wsb_g2')
        self.driver.find_element_by_id('register').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
