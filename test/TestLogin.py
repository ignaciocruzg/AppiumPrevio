import os
import pytest
from dotenv import load_dotenv
from pages.LoginPage import LoginPage


# @pytest.mark.usefixtures("appium_start")
class TestLogin:

    load_dotenv("../AppiumPrevio/utilities/.env")

    @pytest.mark.happypath
    def test_login_success(self, driver):
        username = os.getenv("USER_CORRECT")
        password = os.getenv("PASSWORD_CORRECT")
        titlehomepage = os.getenv("TITTLE_HOME_PAGE")
        login_page = LoginPage(driver)
        home_page = login_page.login(username, password)
        assert home_page.get_home_page_name_title() == titlehomepage

    @pytest.mark.exceptions
    def test_login_incorrect_credentials(self, driver):
        username = os.getenv("USER_INCORRECT")
        password = os.getenv("PASSWORD_INCORRECT")
        msj_error = os.getenv("MSG_ERROR_INCORRECT_CREDENTIALS")
        login_page = LoginPage(driver)
        login_page.login(username, password)
        assert login_page.get_error_msg_text_incorrects_credentials() == msj_error

    @pytest.mark.exceptions
    def test_login_user_required(self, driver):
        username = os.getenv("USER_EMPTY")
        password = os.getenv("PASSWORD_CORRECT")
        msj_error = os.getenv("MSG_ERROR_USER_EMPTY")
        login_page = LoginPage(driver)
        login_page.login(username, password)
        assert login_page.get_error_msg_text_user_required() == msj_error

    @pytest.mark.exceptions
    def test_login_password_required(self, driver):
        username = os.getenv("USER_CORRECT")
        password = os.getenv("PASSWORD_EMPTY")
        msj_error = os.getenv("MSG_ERROR_PASSWORD_EMPTY")
        login_page = LoginPage(driver)
        login_page.login(username, password)
        assert login_page.get_error_msg_text_password_required() == msj_error
