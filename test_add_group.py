import unittest
import pytest
from selenium import webdriver
from group import Group

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    return wd

def login(driver, username="admin", password="secret"):
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(username)
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

def go_to_home_page(driver):
    driver.get("http://localhost/addressbook/")

def create_new_group(driver, group):
    driver.find_element_by_link_text("groups").click()
    driver.find_element_by_name("new").click()
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    driver.find_element_by_name("group_name").send_keys(group.group_name)
    driver.find_element_by_name("group_header").click()
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys(group.group_header)
    driver.find_element_by_name("group_footer").click()
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys(group.group_footer)
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("groups").click()

def logout(driver):
    driver.find_element_by_link_text("Logout").click()


def test_add_group(driver):
    go_to_home_page(driver)
    login(driver)
    create_new_group(driver, Group(group_name="Name1", group_header="Header1", group_footer="Foooter1"))
    logout(driver)

def test_add_empty_group(driver):
    go_to_home_page(driver)
    login(driver)
    create_new_group(driver, Group(group_name="", group_header="", group_footer=""))
    logout(driver)

def tearDown(driver):
    driver.wd.quit()

if __name__ == '__main__':
    unittest.main()
