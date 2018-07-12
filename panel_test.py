from selenium import webdriver
import unittest


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    


    
    def test_unit(self):
        self.driver.get("http://172.16.255.21")
        elm1 =self.driver.find_element_by_xpath(''//*[@id="gn-menu"]/li[1]/div/a/span'')