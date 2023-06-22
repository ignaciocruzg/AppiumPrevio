from appium.webdriver.common.appiumby import AppiumBy

from pages.ProductsPage import ProductsPage
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    # Declaracion de componentes a utilizar
    userTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Usuario")
    passwordTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Contraseña")
    loginBtn = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    dataIncorrectMsg = (AppiumBy.ACCESSIBILITY_ID, "test-Error")

    def type_user(self, usuario):
        self.wait_for_element_to_be_visible(LoginPage.userTextBox)
        username_input = self.find(LoginPage.userTextBox)
        print(username_input.is_displayed())
        username_input.send_keys(usuario)

    def type_password(self, contrasena):
        self.wait_for_element_to_be_visible(LoginPage.passwordTextBox)
        password_input = self.find(LoginPage.passwordTextBox)
        print(password_input.is_displayed())
        password_input.send_keys(contrasena)

    def tap_login_btn(self):
        self.find(LoginPage.loginBtn).click()

    def login(self, usuario, password):
        self.type_user(usuario)
        self.type_password(password)
        self.tap_login_btn()
        return ProductsPage(self.driver)

    def get_error_msg_text(self):
        return self.find(LoginPage.dataIncorrectMsg).text
