# test_selection.py
import pytest

# This file contains a variety of tests with different markers and names
# to demonstrate advanced test selection techniques.

@pytest.mark.smoke
def test_login_valid_user():
    """A smoke test for a valid user login."""
    assert True

@pytest.mark.regression
def test_login_invalid_user():
    """A regression test for an invalid user login."""
    assert True

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_as_guest():
    """A test that is both a smoke and a regression test."""
    assert True

@pytest.mark.slow
def test_end_to_end_purchase_flow():
    """A slow end-to-end test."""
    import time
    time.sleep(1)
    assert True

class TestUserProfile:
    @pytest.mark.regression
    def test_update_profile_name(self):
        """A test for updating the user profile name."""
        assert True

    def test_update_profile_email(self):
        """A test for updating the user profile email."""
        assert True

# To try out the selection techniques, run pytest with the following commands:
#
# pytest -m "smoke"                       # Run only smoke tests
# pytest -m "not slow"                    # Run all tests except the slow ones
# pytest -m "smoke and regression"        # Run tests with both smoke and regression markers
# pytest -m "smoke or regression"         # Run tests with either smoke or regression markers
#
# pytest -k "login"                       # Run tests with "login" in their name
# pytest -k "UserProfile"                 # Run all tests in the TestUserProfile class
# pytest -k "update and not email"        # Run tests with "update" but not "email" in their name
#
# # Run a specific test by its node ID
# pytest test_selection.py::test_login_valid_user
#
# # Run all tests in the TestUserProfile class by its node ID
# pytest test_selection.py::TestUserProfile
