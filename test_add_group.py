# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import pytest
from selenium import webdriver

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    return wd
    
def test_(driver):
    success = True
    driver.get("http://localhost/addressbook/")
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys("admin")
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys("secret")
    driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    driver.find_element_by_link_text("groups").click()
    driver.find_element_by_name("new").click()
    driver.find_element_by_name("group_name").click()
    driver.find_element_by_name("group_name").clear()
    driver.find_element_by_name("group_name").send_keys("Name1")
    driver.find_element_by_name("group_header").click()
    driver.find_element_by_name("group_header").clear()
    driver.find_element_by_name("group_header").send_keys("Header1")
    driver.find_element_by_name("group_footer").click()
    driver.find_element_by_name("group_footer").clear()
    driver.find_element_by_name("group_footer").send_keys("Foooter1")
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("groups").click()
    driver.find_element_by_link_text("Logout").click()
    
def tearDown(driver):
    driver.wd.quit()

if __name__ == '__main__':
    unittest.main()
