from appium.webdriver.common.appiumby import AppiumBy
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.userTextBox = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Usuario")
        self.passwordTextBox = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Contraseña")
        self.loginBtn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
        self.dataIncorrectMsg = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Error")

    def type_user(self):
        self.wait_for_element(self.userTextBox)
        self.find(self.userTextBox).send_keys("standard_user")

    def type_password(self):
        self.wait_for_element(self.passwordTextBox)
        self.find(self.passwordTextBox).send_keys("secret_sauce")

    def login(self):
        self.type_user()
        self.type_password()
        self.wait_for_element(self.loginBtn)
        self.find(self.loginBtn).click()
        return


    # userTextBox = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Usuario")
    # passwordTextBox = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Contraseña")
    # loginBtn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
    # dataIncorrectMsg = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Error")