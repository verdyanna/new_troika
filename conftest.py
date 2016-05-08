import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application() #инициализация фикстуры
    request.addfinalizer(fixture.destroy)  #указание на то, как должна быть разрушена фикстура
    return fixture