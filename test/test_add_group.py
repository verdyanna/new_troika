# -*- coding: utf-8 -*-
from model.platform_model import Platform

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group_helper.create_new_group(Platform(name="hhhh", header="rrrrr", footer="tttt"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group_helper.create_new_group(Platform(name="hhhh", header="rrrrr", footer="tttt"))
    app.session.logout()
