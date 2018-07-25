import unittest
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    return wd


def logout(driver):
    driver.find_element_by_link_text("Logout").click()


def create_new_contact(driver, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work,
                       fax, email, byear):
    driver.find_element_by_link_text("add new").click()
    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys(firstname)
    driver.find_element_by_name("middlename").click()
    driver.find_element_by_name("middlename").clear()
    driver.find_element_by_name("middlename").send_keys(middlename)
    driver.find_element_by_name("lastname").click()
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys(lastname)
    driver.find_element_by_name("nickname").click()
    driver.find_element_by_name("nickname").clear()
    driver.find_element_by_name("nickname").send_keys(nickname)
    driver.find_element_by_name("title").click()
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys(title)
    driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys(company)
    driver.find_element_by_name("address").click()
    driver.find_element_by_name("address").clear()
    driver.find_element_by_name("address").send_keys(address)
    driver.find_element_by_name("home").click()
    driver.find_element_by_name("home").clear()
    driver.find_element_by_name("home").send_keys(home)
    driver.find_element_by_name("mobile").click()
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys(mobile)
    driver.find_element_by_name("work").click()
    driver.find_element_by_name("work").clear()
    driver.find_element_by_name("work").send_keys(work)
    driver.find_element_by_name("fax").click()
    driver.find_element_by_name("fax").clear()
    driver.find_element_by_name("fax").send_keys(fax)
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("homepage").click()
    if not driver.find_element_by_xpath("//div[@id='content']/form/select[1]//option[21]").is_selected():
        driver.find_element_by_xpath("//div[@id='content']/form/select[1]//option[21]").click()
    if not driver.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").is_selected():
        driver.find_element_by_xpath("//div[@id='content']/form/select[2]//option[13]").click()
    driver.find_element_by_name("byear").click()
    driver.find_element_by_name("byear").clear()
    driver.find_element_by_name("byear").send_keys(byear)
    driver.find_element_by_name("theform").click()
    driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


def login(driver, username, password):
    driver.find_element_by_name("user").click()
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys(username)
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


def go_to_home_page(driver):
    driver.get("http://localhost/addressbook/group.php")


def test_add_empty_contact(driver):
    go_to_home_page(driver)
    login(driver, username="admin", password="secret")
    create_new_contact(driver, firstname="FN", middlename="MN", lastname="LN", nickname="NN", title="Title", company="Company", address="Street", home="123", mobile="123", work="123", fax="123",
                       email="r@d.ru", byear="1990")
    go_to_home_page(driver)
    create_new_contact(driver, firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                       home="", mobile="", work="", fax="",
                       email="", byear="")
    logout(driver)

def tearDown(driver):
    driver.wd.quit()

if __name__ == '__main__':
    unittest.main()
