import os
from appium.webdriver.common.appiumby import AppiumBy

from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass
from dotenv import load_dotenv


class LoginPage(BaseClass):

    # Obtencion de textos contenidos en .env
    load_dotenv("../AppiumPrevio/utilities/.env")
    msgErrorCredentials = os.getenv("MSG_ERROR_INCORRECT_CREDENTIALS")
    msgErrorUserEmpty = os.getenv("MSG_ERROR_USER_EMPTY")
    msgErrorPasswordEmpty = os.getenv("MSG_ERROR_PASSWORD_EMPTY")

    # Declaracion de componentes a utilizar
    userTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Usuario")
    passwordTextBox = (AppiumBy.ACCESSIBILITY_ID, "test-Contraseña")
    loginBtn = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    dataIncorrectMsg = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("{}")'
                        .format(msgErrorCredentials))
    dataRequiredUser = (AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("{}")'
                        .format(msgErrorUserEmpty))
    dataRequiredPassword = (AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("{}")'
                            .format(msgErrorPasswordEmpty))

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

    def get_error_msg_text_incorrect_credentials(self):
        print("Texto del mensaje de error: "
              + self.find(LoginPage.dataIncorrectMsg).text)
        return self.find(LoginPage.dataIncorrectMsg).text

    def get_error_msg_text_user_required(self):
        print("Texto del mensaje de error: "
              + self.find(LoginPage.dataRequiredUser).text)
        return self.find(LoginPage.dataRequiredUser).text

    def get_error_msg_text_password_required(self):
        print("Texto del mensaje de error: "
              + self.find(LoginPage.dataRequiredPassword).text)
        return self.find(LoginPage.dataRequiredPassword).text
