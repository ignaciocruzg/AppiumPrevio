from appium.webdriver.common.appiumby import AppiumBy

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    homePageTitle = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"PRODUCTOS\")")
    def get_home_page_name_title(self):
        return self.find(HomePage.homePageTitle).text
