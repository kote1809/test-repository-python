import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login()
    app.conftest.create_g(Group(group_name="Name1", group_header="Header1", group_footer="Foooter1"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login()
    app.conftest.create_g(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()

def test_edit_group(app):
    app.session.login()
    app.conftest.edit_g(Group(group_name="SS", group_header="VV", group_footer="EE"))
    app.session.logout()

def test_delete_group(app):
    app.session.login()
    app.conftest.delete_g()
    app.session.logout()
