# helpers.py

def login_user(login_page, username, password):
    """
    A test helper that encapsulates the steps for logging in a user.
    """
    login_page.navigate_to()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

def assert_is_valid_user(user):
    """
    A helper for making assertions about a user object.
    """
    assert "name" in user
    assert "email" in user
    assert isinstance(user["is_admin"], bool)
