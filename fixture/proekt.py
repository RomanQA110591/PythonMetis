from model.proekt import Proekt


class ProektHelper:
    def __init__(self, app):
        self.app = app

    def open_proj_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_page.php")

    def create(self, proekt):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_create_page.php")
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(proekt.name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(proekt.description)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()
        wd.find_element_by_xpath(u"//a[contains(text(),'Продолжить')]").click()
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_page.php")

    def delete_proekt(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='публичный'])[1]/preceding::a[1]").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_delete.php")
        wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/form/input[4]").click()
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_page.php")

    def count(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_page.php")
        return len(wd.find_elements_by_xpath(u"//a[contains(text(),'Управление проектами')]"))

    def get_proekt_list(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/manage_proj_page.php")
        list = []
        for element in wd.find_elements_by_xpath(u"//a[contains(text(),'Управление проектами')]"):
            text = element.text
            list.append(Proekt(name=text))
        return list






