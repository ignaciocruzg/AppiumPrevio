from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BaseClass:

    # Constructor de la clase base
    def __init__(self, driver):
        self.driver = driver
        # self._wait = WebDriverWait(self, driver, 10)

    # Esperamos a que un elemento este presente
    def wait_for_element(self, locator):
        return EC.presence_of_element_located(locator)

    # Esperamos a que un elemento este visible
    def wait_for_element_to_be_visible(self, locator):
        return EC.visibility_of_element_located(locator)

    # Buscamos y retornamos un elemento
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Hacemos scroll hasta ubicar x elemento
    def scroll_to_element(self, x0, y0, x1, y1, locator):
        # Este numero va acorder a nustras necesidades
        for _ in range(10):
            try:
                if self.find(locator).is_displayed():
                    # Para debugear
                    print("Element found")
                    sleep(10)
                    ######
                    break
            except:
                self.driver.swipe(x0, y0, x1, y1)
                sleep(3)
                continue
