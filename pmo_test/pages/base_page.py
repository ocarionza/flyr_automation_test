from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import get_logger

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
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            logger.error(f"No se encontró el elemento: {locator}")
            raise

    def wait_for_element(self, locator, timeout=10):
        """Espera hasta que un elemento sea visible."""
        try:
            logger.info(f"Esperar el elemento: {locator}")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Timeout esperando por el elemento: {locator}")
            raise

    def click(self, locator):
        """Hace clic en un elemento."""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Ingresa texto en un campo."""
        self.find_element(locator).send_keys(text)