

class SessionHelper:
    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_xpath(u"//input[@value='Вход']").click()
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Вход']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/a/i[2]").click()
        wd.find_element_by_link_text(u"Выход").click()