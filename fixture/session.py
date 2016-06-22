class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='login-window']//button[.='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.exit").click()