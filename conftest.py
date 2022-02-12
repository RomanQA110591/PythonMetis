import pytest
import json
from model.proekt import Proekt
from fixture.application import Application


target = None


@pytest.fixture
def app(request):
    global target
    browser = request.config.getoption("--browser")
    with open(request.config.getoption("--target")) as config_fale:
        target = json.load(config_fale)
    fixture = Application(browser=browser, base_url=target['base_url'])
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
