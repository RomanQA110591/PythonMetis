from selenium import webdriver
from fixture.session import SessionHelper
from fixture.proekt import ProektHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.proekt = ProektHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-2.25.2/mantisbt-2.25.2/login_page.php")

    def destroy(self):
        self.wd.quit()





