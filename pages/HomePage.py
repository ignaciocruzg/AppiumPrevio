import os
from appium.webdriver.common.appiumby import AppiumBy

from utilities.BaseClass import BaseClass
from dotenv import load_dotenv


class HomePage(BaseClass):
    # Cargar archivo con datos de entrada
    load_dotenv("../AppiumPrevio/utilities/.env")
    titlePage = os.getenv("TITTLE_HOME_PAGE")

    homePageTitle = (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("{}")'.format(titlePage))

    def get_home_page_name_title(self):
        return self.find(HomePage.homePageTitle).text
