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

class object_fill(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_object_fill(self):
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
        wd.find_element_by_link_text("Начать работу").click()
        wd.find_element_by_id("add-object").click()
        wd.find_element_by_id("id_address").click()
        wd.find_element_by_id("id_address").clear()
        wd.find_element_by_id("id_address").send_keys("Rhfcyjuhcr")
        wd.find_element_by_id("id_address").click()
        wd.find_element_by_id("id_address").clear()
        wd.find_element_by_id("id_address").send_keys("Красногрск, улю Железнодорожная, 1Б")
        wd.find_element_by_id("id_address").click()
        wd.find_element_by_id("id_address").clear()
        wd.find_element_by_id("id_address").send_keys("Красногрск, улю Железнодорожная, 1Б")
        wd.find_element_by_id("id_mkd").click()
        wd.find_element_by_id("ui-id-8").click()
        wd.find_element_by_id("id_qty_container").click()
        wd.find_element_by_id("id_qty_container").clear()
        wd.find_element_by_id("id_qty_container").send_keys("3")
        wd.find_element_by_id("id_capacity_container").click()
        wd.find_element_by_id("ui-id-11").click()
        wd.find_element_by_id("id_type").click()
        wd.find_element_by_id("ui-id-15").click()
        wd.find_element_by_id("id_surface").click()
        wd.find_element_by_id("ui-id-17").click()
        wd.find_element_by_id("id_fences").click()
        wd.find_element_by_id("ui-id-23").click()
        wd.find_element_by_id("id_place_kgm").click()
        wd.find_element_by_id("ui-id-27").click()
        wd.find_element_by_id("id_dispose").click()
        wd.find_element_by_id("ui-id-29").click()
        wd.find_element_by_id("id_org_1").click()
        wd.find_element_by_id("id_org_1").clear()
        wd.find_element_by_id("id_org_1").send_keys("ООО \"Трест-Осипова\"")
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[11]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[11]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[11]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[11]/div[2]/a").click()
        wd.find_element_by_id("id_org_1_inn").click()
        wd.find_element_by_id("id_org_1_inn").clear()
        wd.find_element_by_id("id_org_1_inn").send_keys("11111")
        wd.find_element_by_id("id_org_1_ogrn").click()
        wd.find_element_by_id("id_org_1_ogrn").clear()
        wd.find_element_by_id("id_org_1_ogrn").send_keys("22222")
        wd.find_element_by_id("id_org_2").click()
        wd.find_element_by_id("id_org_2").clear()
        wd.find_element_by_id("id_org_2").send_keys("ООО \"Тест_Осипова\"")
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_id("id_org_2_inn").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div/div[12]/div[2]/a").click()
        wd.find_element_by_xpath("//div[@class='base-form']/div").click()
        wd.find_element_by_id("save-object").click()
        wd.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()
        wd.find_element_by_id("save-object").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
