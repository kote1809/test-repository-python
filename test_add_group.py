import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login()
    app.create_new_group(Group(group_name="Name1", group_header="Header1", group_footer="Foooter1"))
    app.logout()

def test_add_empty_group(app):
    app.login()
    app.create_new_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()

