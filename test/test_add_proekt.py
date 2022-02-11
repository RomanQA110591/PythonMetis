import pytest
from model.proekt import Proekt
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_proekt(app):
    app.open_home_page()
    app.session.login(username="administrator", password="123")
    app.proekt.open_proj_page()
    app.proekt.create(Proekt(name="Test", description="test"))
    app.session.logout()
