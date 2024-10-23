import time
import allure
from config.environment import BASE_URL
from pages.booking_page import BookingPage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger()

LANGUAGES = ["English", "Español", "Português", "Français"]

@allure.epic('Cambio de idioma')
@allure.feature('Idioma dinámico')
@allure.story('Seleccionar idioma y verificar el cambio')
def test_change_language(driver, start_recording):
    """Test dinámico para cambiar el idioma a uno especificado usando XPath basado en la clase 'language-selector'."""

    booking_page = BookingPage(driver)

    booking_page.open(BASE_URL)  # Abre la página principal

    time.sleep(3)

    for language in LANGUAGES:
        with allure.step(f"Iniciar la prueba para cambiar el idioma a '{language}'"):
            logger.info(f"Iniciando la prueba para cambiar el idioma a '{language}' dinámicamente usando XPath basado en la clase 'language-selector'")

            booking_page.open_language_dropdown()  # Abre el menú de selección de idioma
            logger.info("Menú de selección de idioma abierto.")

            time.sleep(2)

            booking_page.select_language(language)  # Selecciona el idioma proporcionado
            logger.info(f"Idioma '{language}' seleccionado.")

            time.sleep(2)

            # Aserción para verificar que el idioma ha cambiado
            current_language_xpath = f"//*[@class='language-selector']//button[contains(@aria-label, '{language}')]"
            current_language = driver.find_element(By.XPATH, current_language_xpath)
            assert language in current_language.get_attribute("aria-label"), f"No se cambió el idioma a '{language}'"

            logger.info(f"Prueba completada: El idioma fue cambiado correctamente a '{language}'")

            allure.attach(driver.get_screenshot_as_png(), name=f"Idioma_{language}",attachment_type=allure.attachment_type.PNG)