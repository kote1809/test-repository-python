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
    
def test_test_add_contact(driver):
    success = True
    driver.get("http://localhost/addressbook/group.php")
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys("admin")
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys("secret")
    driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    driver.find_element_by_link_text("add new").click()
    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys("FN")
    driver.find_element_by_name("middlename").click()
    driver.find_element_by_name("middlename").clear()
    driver.find_element_by_name("middlename").send_keys("MN")
    driver.find_element_by_name("lastname").click()
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys("LN")
    driver.find_element_by_name("nickname").click()
    driver.find_element_by_name("nickname").clear()
    driver.find_element_by_name("nickname").send_keys("NN")
    driver.find_element_by_name("title").click()
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys("Title")
    driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys("Company")
    driver.find_element_by_name("address").click()
    driver.find_element_by_name("address").clear()
    driver.find_element_by_name("address").send_keys("Street")
    driver.find_element_by_name("home").click()
    driver.find_element_by_name("home").clear()
    driver.find_element_by_name("home").send_keys("123")
    driver.find_element_by_name("mobile").click()
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys("123")
    driver.find_element_by_name("work").click()
    driver.find_element_by_name("work").clear()
    driver.find_element_by_name("work").send_keys("123")
    driver.find_element_by_name("fax").click()
    driver.find_element_by_name("fax").clear()
    driver.find_element_by_name("fax").send_keys("123")
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("r@d.ru")
    driver.find_element_by_name("homepage").click()
    if not driver.find_element_by_xpath("//div[@id='content']/form/select[1]//option[21]").is_selected():
        driver.find_element_by_xpath("//div[@id='content']/form/select[1]//option[21]").click()
    if not driver.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").is_selected():
        driver.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").click()
    driver.find_element_by_name("byear").click()
    driver.find_element_by_name("byear").clear()
    driver.find_element_by_name("byear").send_keys("1990")
    driver.find_element_by_name("theform").click()
    driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
    driver.find_element_by_link_text("Logout").click()
    
def tearDown(driver):
    self.wd.quit()

if __name__ == '__main__':
    unittest.main()
