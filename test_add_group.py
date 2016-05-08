# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application() #инициализация фикстуры
    request.addfinalizer(fixture.destroy)  #указание на то, как должна быть разрушена фикстура
    return fixture


def test_add_group(app): #тестовый метод, принимающий параметр- фикстуру
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group(name="hhhh", header="rrrrr", footer="tttt"))
    app.return_to_group_page()
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group( name="hhhh", header="rrrrr", footer="tttt"))
    app.return_to_group_page()
    app.logout()
