import os
import unittest
from appium import webdriver
from time import sleep


class DictionaryTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Pixel API 22'
        desired_caps['app'] = os.path.abspath(
            'C:/Users/Min Khant Ko Ko/Desktop/dictionary.apk')
        desired_caps['appPackage'] = 'livio.pack.lang.en_US'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_mode(self):
        el1 = self.driver.find_element_by_accessibility_id("Search")
        el1.click()
        el2 = self.driver.find_element_by_id(
            "livio.pack.lang.en_US:id/search_src_text")
        el2.send_keys("doctor")
        self.driver.press_keycode(66)
        sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DictionaryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)