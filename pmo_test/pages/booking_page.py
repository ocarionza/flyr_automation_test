from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class BookingPage(BasePage):
    LANGUAGE_DROPDOWN_BUTTON = (By.XPATH, "//*[@class='language-selector']//button[contains(@class, 'dropdown_trigger')]")
    LANGUAGE_OPTION_TEMPLATE = "//*[@class='language-selector']//span[contains(text(), '{}')]"

    POS_SELECTOR = (By.XPATH, "//li[contains(@class, 'main-header_nav-secondary_item') and contains(@class, 'main-header_nav-secondary_item--point-of-sale-selector')]//button[@id='pointOfSaleSelectorId']")
    POS_LIST = "//*[contains(@class,'points-of-sale_list_item')][contains(.,'{}')]/button"
    POS_APPLY_SELECTOR = (By.XPATH, "//*[@class='button points-of-sale_footer_action_button']")

    ONE_WAY_RADIO = (By.XPATH, "//input[@id='journeytypeId_1']/following-sibling::label/span")
    ROUND_TRIP_RADIO = (By.XPATH, "//*[@id='journeytypeId_0']/following-sibling::label/span")

    ORIGIN_FIELD = (By.XPATH, "//div[@id='originDiv']/input | //div[@id='originDiv']/button")
    INPUT_ORIGIN = (By.XPATH, "//div[@id='originDiv']//input")
    INPUT_DESTINATION = (By.XPATH, "//input[@aria-labelledby='arrivalStationInputLabel'] | //div[@class='control_field_inner']/div[@id='arrivalStationInputLabel']/following-sibling::input")

    def open_language_dropdown(self):
        """Hace clic en el botón para abrir el dropdown de selección de idioma."""
        logger.info("Abriendo el menú de selección de idioma")

        # Espera explícita para asegurarse de que el botón esté listo para ser clicado
        wait = WebDriverWait(self.driver, 10)
        dropdown_button = wait.until(EC.element_to_be_clickable(self.LANGUAGE_DROPDOWN_BUTTON))

        dropdown_button.click()
        logger.info("Menú de selección de idioma abierto")

    def open_pos_selector(self):
        """Hace clic en el botón para abrir el popup de paises"""
        logger.info("Abriendo el popup para seleccionar el POS")

        # Espera explícita para asegurarse de que el botón esté listo para ser clicado
        wait = WebDriverWait(self.driver, 10)
        pos_button = wait.until(EC.element_to_be_clickable(self.POS_SELECTOR))

        pos_button.click()
        logger.info("Menú de selección de POS abierto")

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

    def select_pos(self, pos):
        """Selecciona un POS dinámicamente"""
        logger.info(f"Seleccionando el pos '{pos}' dinámicamente")

        # XPath dinámico basado en el idioma
        pos_option_xpath = (By.XPATH, self.POS_LIST.format(pos))

        # Espera explícita para que la opción de idioma esté disponible
        wait = WebDriverWait(self.driver, 10)
        pos_option = wait.until(EC.element_to_be_clickable(pos_option_xpath))

        pos_option.click()
        logger.info(f"POS '{pos}' seleccionado correctamente")

    def apply_pos(self):
        """Hace clic en el botón para aplicar el POS"""

        # Espera explícita para asegurarse de que el botón esté listo para ser clicado
        wait = WebDriverWait(self.driver, 10)
        pos_button_apply = wait.until(EC.element_to_be_clickable(self.POS_APPLY_SELECTOR))

        pos_button_apply.click()
        logger.info("Boton aplicar seleccionado")

    def click_one_way(self):
        wait = WebDriverWait(self.driver, 10)
        one_way_button = wait.until(EC.element_to_be_clickable(self.ONE_WAY_RADIO))

        one_way_button.click()
        logger.info("Seleccion tipo de viaje one way")

    def click_round_trip(self):
        wait = WebDriverWait(self.driver, 10)
        round_trip_button = wait.until(EC.element_to_be_clickable(self.ROUND_TRIP_RADIO))

        round_trip_button.click()
        logger.info("Seleccion tipo de viaje one way")

    def write_origin(self, text):
        wait = WebDriverWait(self.driver, 10)
        origin_field = wait.until(EC.element_to_be_clickable(self.ORIGIN_FIELD))
        origin_field.click()
        self.enter_text(self.INPUT_ORIGIN, text)

    def write_destination(self, text):
        self.enter_text(self.INPUT_DESTINATION, text)

