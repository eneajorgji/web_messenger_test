import unittest
from selenium import webdriver
import time
import names

NEW_NAME = names.get_first_name()
NEW_SURNAME = names.get_last_name()

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register(self):
        self.driver.get('http://kmg.hcm.pl/testowanie/register.html')
        # module names is used to generate different name each time test runs
        self.driver.find_element_by_id('username').send_keys(NEW_NAME)
        time.sleep(2)
        self.driver.find_element_by_id('pass1').send_keys('Test123')
        self.driver.find_element_by_id('pass2').send_keys('Test123')
        self.driver.find_element_by_id('name').send_keys(NEW_NAME)
        self.driver.find_element_by_id('surname').send_keys(NEW_SURNAME)
        self.driver.find_element_by_id('kodgrupy').send_keys('wsb_g2')
        self.driver.find_element_by_id('register').click()
        assert 'Rejestracja ' in self.driver.page_source
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
