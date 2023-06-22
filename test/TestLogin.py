import pytest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("appium_start")
class MyTestCase:
    def test_login_success(self):
        driver = self.driver
        loginpage = LoginPage(self)
        LoginPage.login(loginpage)
