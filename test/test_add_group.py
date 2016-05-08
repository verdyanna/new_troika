# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app): #тестовый метод, принимающий параметр- фикстуру
    app.session.login(username="admin", password="secret")
    app.group_helper.create_new_group(Group(name="hhhh", header="rrrrr", footer="tttt"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group_helper.create_new_group(Group( name="hhhh", header="rrrrr", footer="tttt"))
    app.session.logout()
