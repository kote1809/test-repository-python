from selenium import webdriver
from fixture.session import Session
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.conftest import Conftest
__author__ = 'sveta'

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.session = Session(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.conftest = Conftest(self)


    def go_to_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()