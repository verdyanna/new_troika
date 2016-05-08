class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact_model):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fillin_contact_form(contact_model)

    def fillin_contact_form(self, contact_model):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact_model.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact_model.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact_model.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(contact_model.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact_model.work)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_model.phone2)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_model.address)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


