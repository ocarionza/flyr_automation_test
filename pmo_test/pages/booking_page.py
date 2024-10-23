from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class BookingPage(BasePage):
    LANGUAGE_DROPDOWN_BUTTON = (By.XPATH, "//*[@class='language-selector']//button[contains(@class, 'dropdown_trigger')]")
    LANGUAGE_OPTION_TEMPLATE = "//*[@class='language-selector']//span[contains(text(), '{}')]"

    def open_language_dropdown(self):
        """Hace clic en el botón para abrir el dropdown de selección de idioma."""
        logger.info("Abriendo el menú de selección de idioma")

        # Espera explícita para asegurarse de que el botón esté listo para ser clicado
        wait = WebDriverWait(self.driver, 10)
        dropdown_button = wait.until(EC.element_to_be_clickable(self.LANGUAGE_DROPDOWN_BUTTON))

        dropdown_button.click()
        logger.info("Menú de selección de idioma abierto")

    def select_language(self, language):
        """Selecciona un idioma dinámicamente en el menú desplegable usando el nombre del idioma."""
        logger.info(f"Seleccionando el idioma '{language}' dinámicamente usando la clase 'language-selector'")

        # XPath dinámico basado en el idioma
        language_option_xpath = (By.XPATH, self.LANGUAGE_OPTION_TEMPLATE.format(language))

        # Espera explícita para que la opción de idioma esté disponible
        wait = WebDriverWait(self.driver, 10)
        language_option = wait.until(EC.element_to_be_clickable(language_option_xpath))

        language_option.click()
        logger.info(f"Idioma '{language}' seleccionado correctamente")
