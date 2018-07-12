import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class Calltest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'Pixel API 28'
        desired_caps['appPackage'] = 'com.android.dialer'
        desired_caps['appActivity'] = 'com.android.dialer.DialtactsActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)
        self.driver.orientation = "PORTRAIT"

    def tearDown(self):
        self.driver.quit()

    def testcall(self):
        element1 = self.driver.find_element_by_id(
            'com.android.dialer:id/floating_action_button_container')
        element1.click()
        element2 = self.driver.find_element_by_id('com.android.dialer:id/zero')
        action = TouchAction(self.driver)
        action.long_press(element2)
        action.perform()
        id = self.driver.find_element_by_id(
            'com.android.dialer:id/digits').text
        self.assertEquals(id, '+')
        sleep(5)
        print(self.driver.contexts)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Calltest)
    unittest.TextTestRunner(verbosity=2).run(suite)
