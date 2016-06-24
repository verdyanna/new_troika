from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.platform_helper import PlatformHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group_helper = GroupHelper(self)
        self.platform_helper = PlatformHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://region.rsoo.ru/")

    def destroy(self):
        self.wd.quit()