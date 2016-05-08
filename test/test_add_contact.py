import pytest
from fixture.application import Application
from model.contact_model import Contact_fill

@pytest.fixture
def app(request):
    fixture = Application() #инициализация фикстуры
    request.addfinalizer(fixture.destroy)  #указание на то, как должна быть разрушена фикстура
    return fixture

def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_helper.fill_contact_form(Contact_fill(firstname = "hhhhhhhh", lastname = "ggggggggg", home = "77777777777", mobile = "66666666666",
                                                      work = "99999999", phone2 = "3444444444", address = "drftghhuyyhh"))
    app.session.logout()