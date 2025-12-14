# test_allure_reporting.py
import allure
import pytest

# To run this example and generate an Allure report:
# 1. Install allure-pytest: pip install allure-pytest
# 2. Run pytest with the --alluredir option:
#    pytest --alluredir=./allure-results
# 3. Serve the report using the Allure command-line tool:
#    (You may need to install this separately: https://allurereport.org/)
#    allure serve ./allure-results

@allure.feature("Login Feature")
class TestLogin:
    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """
        This test demonstrates a successful login scenario.
        """
        with allure.step("Navigate to the login page"):
            print("Navigating to login page...")
            pass

        with allure.step("Enter username and password"):
            print("Entering credentials...")
            allure.attach("testuser", name="Username", attachment_type=allure.attachment_type.TEXT)
            allure.attach("password123", name="Password", attachment_type=allure.attachment_type.TEXT)
            pass

        with allure.step("Click the login button"):
            print("Clicking login button...")
            pass

        with allure.step("Verify the user is redirected to the dashboard"):
            print("Verifying dashboard...")
            assert True

    @allure.story("Failed Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login_with_invalid_credentials(self):
        """
        This test demonstrates a failed login due to invalid credentials.
        """
        with allure.step("Navigate to the login page"):
            pass

        with allure.step("Enter invalid username and password"):
            pass

        with allure.step("Click the login button"):
            pass

        with allure.step("Verify an error message is displayed"):
            # This step will fail to demonstrate how failures are shown in the report.
            import os
            script_dir = os.path.dirname(__file__)
            screenshot_path = os.path.join(script_dir, "screenshot.png")
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, "Error message was not displayed."
