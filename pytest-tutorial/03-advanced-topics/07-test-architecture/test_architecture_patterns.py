# test_architecture_patterns.py
from page_objects import LoginPage
from data_builders import UserBuilder
from helpers import login_user, assert_is_valid_user

# Note: This is a conceptual example. In a real application, the `driver`
# would be a fixture that provides a Selenium WebDriver or Playwright Page instance.
class MockDriver:
    """A mock driver to simulate a browser driver."""
    def get(self, url): pass
    def find_element(self, by, value): pass

def test_login_with_page_object(mocker):
    """
    This test uses the LoginPage Page Object to interact with the login page.
    """
    mock_driver = MockDriver()
    # Spy on the driver methods to assert that they are called.
    mocker.spy(mock_driver, 'get')

    login_page = LoginPage(mock_driver)

    # Use the test helper to perform the login.
    login_user(login_page, "testuser", "password")

    # This is a conceptual assertion. A real test would assert that the
    # user is redirected to the dashboard page, for example.
    assert mock_driver.get.call_count == 1

def test_user_creation_with_builder():
    """
    This test uses the UserBuilder to create different types of users.
    """
    # Create a standard user.
    standard_user = UserBuilder().with_name("Standard").with_email("standard@test.com").build()
    assert_is_valid_user(standard_user)
    assert not standard_user["is_admin"]

    # Create an admin user.
    admin_user = UserBuilder().with_name("Admin").as_admin().build()
    assert_is_valid_user(admin_user)
    assert admin_user["is_admin"]
