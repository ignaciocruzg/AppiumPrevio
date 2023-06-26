import pytest
from appium import webdriver
# from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def driver():
    # Asignacion de capabilities
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "13",
        "deviceName": "56295fdf",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }

    url = "http://localhost:4723/wd/hub"
    # Creacion de driver y sele pasan las capabilities
    wait_seconds = 5
    driver = webdriver.Remote(url, desired_cap)
    driver.implicitly_wait(wait_seconds)
    yield driver
    # Cerrar driver
    driver.quit()


# @pytest.fixture(scope="module")
# def appium_start():
    # appium_service = AppiumService()
    # print("Start appium server")
    # appium_service.start()
    # yield
    # print("Stop appium server")
    # appium_service.stop()
