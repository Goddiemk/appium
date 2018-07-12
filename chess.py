import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class ChessAndroidTests(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = os.path.abspath(
            'C:/Users/Min Khant Ko Ko/Desktop/chessfree.apk')
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps[
            'appActivity'] = 'uk.co.aifactory.chessfree.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_mode(self):
        element1 = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("uk.co.aifactory.chessfree:id/ButtonPlay")'
        )
        element1.click()
        self.driver.implicitly_wait(30)
        element2 = self.driver.find_element_by_id(
            'uk.co.aifactory.chessfree:id/CrossProm_ExitButton')
        element2.click()
        element3 = self.driver.find_element_by_id(
            'uk.co.aifactory.chessfree:id/MediumButton')
        element3.click()
        element4 = self.driver.find_element_by_id(
            'uk.co.aifactory.chessfree:id/NewGameSettings_ContinueButton')
        element4.click()
        """
        self.driver.implicitly_wait(30)
        element5 = self.driver.find_element_by_id(
            'uk.co.aifactory.chessfree:id/ContinueButton')
        element5.click()
        self.driver.implicitly_wait(30)
        """
        #TouchAction(driver).tap(x=838, y=1397).perform()
        #TouchAction(driver).tap(x=721, y=1155).perform()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
