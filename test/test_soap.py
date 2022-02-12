import string


def test_soap(app):
    username = "administrator"
    password = "123"
    assert app.soap.can_login(username, password)