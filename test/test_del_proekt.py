import pytest
from fixture.application import Application
from model.proekt import Proekt


def test_del_proekt(app):
    app.open_home_page()
    app.session.login(username="administrator", password="123")
    assert app.soap.can_login(username="administrator", password="123")
    app.proekt.open_proj_page()
    if app.proekt.count() == 0:
        app.proekt.create(Proekt(name="Test10", description="test"))
    old_proekts = app.proekt.get_proekt_list()
    app.proekt.delete_proekt()
    new_proekts = app.proekt.get_proekt_list()
    assert len(old_proekts) - 1 == len(new_proekts)
    app.session.logout()

