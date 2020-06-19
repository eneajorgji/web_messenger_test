import unittest
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NEW_NAME = names.get_first_name()


class EditProfile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://kmg.hcm.pl/testowanie_poprawione')
        self.driver.implicitly_wait(10)

    def test_login_edit_profile(self):
        self.driver.find_element_by_id('userLogin').send_keys('adam442')
        self.driver.find_element_by_id('passwordLogin').send_keys('adam442')
        self.driver.find_element_by_id('login').send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        self.driver.element = wait.until(EC.title_contains('PSTO webMessenger - Zalogowano'))

        assert 'PSTO webMessenger - Zalogowano' in self.driver.title

        # time.sleep(3)

        self.driver.find_element_by_xpath('//img[@src="./icon_profile.png"]').click()




        self.driver.find_element_by_id('editOSobie').click()
        self.driver.find_element_by_id('editOSobie').send_keys(
            'For the reason of test I used the module of the name, so I would be able to check whether this section has been changed ',
            NEW_NAME)
        # time.sleep(3)

        # self.save_changes = wait_for_element('editCom', profile_div).click()

        self.driver.element = wait.until(EC.presence_of_element_located((By.ID, 'editBttn')))
        self.driver.element.click()


        assert 'Dane ' in self.driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
