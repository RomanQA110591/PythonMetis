import pytest
from model.proekt import Proekt
from fixture.application import Application


def test_add_proekt(app):
    app.open_home_page()
    app.session.login(username="administrator", password="123")
    assert app.soap.can_login(username="administrator", password="123")
    app.proekt.open_proj_page()
    old_proekts = app.proekt.get_proekt_list()
    app.proekt.create(Proekt(name="Test", description="test"))
    new_proekts = app.proekt.get_proekt_list()
    assert len(old_proekts) + 1 == len(new_proekts)
    app.session.logout()
