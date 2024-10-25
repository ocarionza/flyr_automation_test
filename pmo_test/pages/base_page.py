import random
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from utils.logger import get_logger
from config.environment import LOADER

logger = get_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Abre la URL especificada en el navegador."""
        try:
            logger.info(f"Abrir página: {url}")
            self.driver.get(url)
        except Exception as e:
            logger.error(f"Error abriendo la página: {e}")
            raise

    def find_element(self, locator):
        """Busca un elemento en la página."""
        try:
            self.wait_for_element(locator)
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            logger.error(f"No se encontró el elemento: {locator}")
            raise

    def wait_for_element(self, locator, timeout=10):
        """Espera hasta que un elemento sea visible."""
        try:
            logger.info(f"Esperar el elemento: {locator}")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Timeout esperando por el elemento: {locator}")
            raise

    def click(self, locator):
        """Hace clic en un elemento."""
        self.find_element(locator).click()

    def click_js(self, locator):
        script = f"""
            var element_path = "{locator}";
            function getElementByXpath(path) {{
                return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            }}
            var element = getElementByXpath(element_path);
            if (element) {{
                element.click();
                console.log("Click en el toggle realizado.");
            }} else {{
                console.log("Elemento no encontrado para el XPath: " + element_path);
            }}
            """
        self.driver.execute_script(script)

    def enter_text(self, locator, text):
        """Ingresa texto en un campo."""
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def key_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def key_end(self, locator):
        self.find_element(locator).send_keys(Keys.END)

    def loader_invisibility(self):
        WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located((By.XPATH, LOADER)))

    def scroll(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def select_random_option(self, type_selector, locator):
        options = []
        try:
            if type_selector == "xpath":
                options = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_all_elements_located((By.XPATH, locator)))
            elif type_selector == "id":
                options = WebDriverWait(self.driver, 15).until(
                    EC.visibility_of_all_elements_located((By.ID, locator)))

            if options:
                selected_option = random.choice(options)
                selected_option_text = selected_option.text

                return selected_option_text

        except WebDriverException as exception:
            logger.info(f"No se pueden obtener las opciones del listado {exception.msg}")
            return None

    def validate_element(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except TimeoutException:
            return False

    def scroll_up_arrows(self, locator):
        self.find_element(locator).send_keys(Keys.ARROW_UP)
        self.find_element(locator).send_keys(Keys.ARROW_UP)
        self.find_element(locator).send_keys(Keys.ARROW_UP)

    def scroll_down_arrows(self, locator):
        self.find_element(locator).send_keys(Keys.ARROW_DOWN)
        self.find_element(locator).send_keys(Keys.ARROW_DOWN)
        self.find_element(locator).send_keys(Keys.ARROW_DOWN)