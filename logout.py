# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class logout(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_logout(self):
        success = True
        wd = self.wd
        wd.get("http://www.region.rsoo.ru/login/")
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys("admin@rsso.ru")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("bigthree3")
        wd.find_element_by_xpath("//div[@class='login-window']//button[.='Войти']").click()
        wd.find_element_by_css_selector("a.exit").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
