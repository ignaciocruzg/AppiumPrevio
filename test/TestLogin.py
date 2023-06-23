from pages.LoginPage import LoginPage


class TestLogin:

    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        home_page = login_page.login("standard_user", "secret_sauce")
        assert home_page.get_home_page_name_title() == "PRODUCTOS"

    def test_login_incorrect_credentials(self, driver):
        msj_error = "El usuario y contraseña no coinciden con ningun usuario en este servicio."
        login_page = LoginPage(driver)
        login_page.login("pruebas", "password")
        assert login_page.get_error_msg_text_incorrects_credentials() == msj_error

    def test_login_user_required(self, driver):
        msj_error = "Usuario es requerido"
        login_page = LoginPage(driver)
        login_page.login("", "password")
        assert login_page.get_error_msg_text_user_required() == msj_error

    def test_login_password_required(self, driver):
        msj_error = "Contraseña es requerida"
        login_page = LoginPage(driver)
        login_page.login("pruebas", "")
        assert login_page.get_error_msg_text_password_required() == msj_error
