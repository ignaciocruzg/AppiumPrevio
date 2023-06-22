import pytest
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("appium_start")
class MyTestCase:

    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        home_page = login_page.login("standard_user", "secret_sauce")
        assert home_page.get_home_page_name_title() == "PRODUCTOS"
