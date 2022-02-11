import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_del_proekt(app):
    app.open_home_page()
    app.session.login(username="administrator", password="123")
    app.proekt.open_proj_page()
    app.proekt.delete_proekt()
    app.session.logout()
