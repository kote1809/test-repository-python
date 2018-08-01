import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login()
    app.conftest.create_c(Contact(firstname="FN", middlename="MN", lastname="LN", nickname="NN", title="Title", company="Company", address="Street", home="123", mobile="123", work="123", fax="123",
                               email="r@d.ru", byear="1990"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login()
    app.conftest.create_c(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home="", mobile="", work="", fax="",
                               email="", byear=""))
    app.session.logout()

def test_edit_c(app):
    app.session.login()
    app.conftest.edit_c(Contact(firstname="Sveta", middlename="Zhukova", lastname="Sv", nickname="Zh", title="Not title", company="Not", address="Address", home="900", mobile="900", work="900", fax="900",
                               email="sveta@zhukova.ru", byear="1992"))
    app.session.logout()

def test_detete_c(app):
    app.session.login()
    app.conftest.detele_c()
    app.session.logout()