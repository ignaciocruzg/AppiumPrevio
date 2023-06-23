from appium.webdriver.common.appiumby import AppiumBy

from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    # Declaracion de componentes a utilizar
    userTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Usuario")
    passwordTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Contraseña")
    loginBtn = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    dataIncorrectMsg = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"El usuario y contraseña no coinciden "
                                                      "con ningun usuario en este servicio.\")")
    dataRequiredUser = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Usuario es requerido\")")
    dataRequiredPassword = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Contraseña es requerida\")")

    def type_user(self, usuario):
        self.wait_for_element_to_be_visible(LoginPage.userTextBox)
        username_input = self.find(LoginPage.userTextBox)
        username_input.send_keys(usuario)
        print("Typing User...")

    def type_password(self, contrasena):
        self.wait_for_element_to_be_visible(LoginPage.passwordTextBox)
        password_input = self.find(LoginPage.passwordTextBox)
        password_input.send_keys(contrasena)
        print("Typing Password...")

    def tap_login_btn(self):
        self.find(LoginPage.loginBtn).click()
        print("Tap login...")

    def login(self, usuario, password):
        self.type_user(usuario)
        self.type_password(password)
        self.tap_login_btn()
        return HomePage(self.driver)

    def get_error_msg_text_incorrects_credentials(self):
        print("Texto del mensaje de error: " + self.find(LoginPage.dataIncorrectMsg).text)
        return self.find(LoginPage.dataIncorrectMsg).text

    def get_error_msg_text_user_required(self):
        print("Texto del mensaje de error: " + self.find(LoginPage.dataRequiredUser).text)
        return self.find(LoginPage.dataRequiredUser).text

    def get_error_msg_text_password_required(self):
        print("Texto del mensaje de error: " + self.find(LoginPage.dataRequiredPassword).text)
        return self.find(LoginPage.dataRequiredPassword).text
