import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def driver():
    # Asignacion de capabilities
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "9",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity"
    }

    url = "http://0.0.0.0:4723/wd/hub"
    # Creacion de driver y sele pasan las capabilities
    driver = webdriver.Remote(url, desired_cap)
    yield driver
    # Cerrar driver
    driver.quit()


@pytest.fixture(scope="module")
def appium_start():
    appium_service = AppiumService()
    # Iniciar servicio appium
    appium_service.start()
    yield
    # Detener servicio appium
    appium_service.stop()
