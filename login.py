from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.swaglabsmobileapp",
  "appium:appActivity": "com.swaglabsmobileapp.MainActivity"
}

url = "http://localhost:4723/wd/hub"
espera = 30

driver = webdriver.Remote(url, desired_cap)
driver.implicitly_wait(espera)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Usuario").send_keys("standard_user")
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Contraseña").send_keys("secret_sauce")
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN").click()

driver.quit()
