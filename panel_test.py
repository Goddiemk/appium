from selenium import webdriver
import unittest
from time import sleep


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_unit(self):
        self.driver.get("http://172.16.255.21")
        elm1 = self.driver.find_element_by_xpath(
            '//*[@id="gn-menu"]/li[1]/div/a/span')
        elm1.click()
        sleep(5)
        elm2 = self.driver.find_element_by_link_text('Login')
        elm2.click()
        sleep(5)
        elm3 = self.driver.find_element_by_name('name')
        elm3.send_keys('SEIN.M.M.LWIN')
        elm4 = self.driver.find_element_by_name('pass')
        elm4.send_keys('Fr0nt!!r')
        elm5 = self.driver.find_element_by_name('op')
        elm5.click()
        sleep(5)
        elm6 = self.driver.find_element_by_xpath(
            '//*[@id="gn-menu"]/li[1]/div/a/span')
        elm6.click()
        elm7 = self.driver.find_element_by_link_text('User Management')
        elm7.click()
        elm8 = self.driver.find_element_by_link_text('Batch Add').click()
        elm8.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
