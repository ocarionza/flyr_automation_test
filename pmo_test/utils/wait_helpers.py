from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger

logger = get_logger()

def wait_for_element(driver, locator, timeout=10):
    """Espera hasta que el elemento esté visible."""
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException as e:
        logger.error(f"Timeout esperando por el elemento: {locator}")
        raise
