import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login()
    app.create_new_contact(Contact(firstname="FN", middlename="MN", lastname="LN", nickname="NN", title="Title", company="Company", address="Street", home="123", mobile="123", work="123", fax="123",
                       email="r@d.ru", byear="1990"))
    app.logout()


def test_add_empty_contact(app):
    app.login()
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                       home="", mobile="", work="", fax="",
                       email="", byear=""))
    app.logout()


