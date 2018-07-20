from selenium import webdriver
import unittest
from time import sleep


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_unit(self):

        self.driver.get("http://myanmarnet.com/")

        element = self.driver.find_element_by_xpath(
            '//*[@id="menu-788-1"]/a')  # go to the desired page
        element.click()
        target = self.driver.find_element_by_xpath(
            '//*[@id="accordion"]/div[3]/div/div[3]/p/a')
        self.assertEqual("cs@myanmarnet.com", target.text)
        sleep(10)
        print(target.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
