import pytest
from appium import webdriver


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
