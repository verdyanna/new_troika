import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_contact(app):
    app.session.login(username="admin@rsso.ru", password="bigthree3")
    app.session.logout()