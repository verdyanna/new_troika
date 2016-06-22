import pytest
from fixture.application import Application
from model.contact_model import Contact_fill

@pytest.fixture
def app(request):
    fixture = Application() #инициализация фикстуры
    request.addfinalizer(fixture.destroy)  #указание на то, как должна быть разрушена фикстура
    return fixture

def test_contact(app):
    app.session.login(username="admin@rsso.ru", password="bigthree3")
    app.session.logout()