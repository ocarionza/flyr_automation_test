import time
import allure
from config.environment import BASE_URL
from pages.booking_page import BookingPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()

COUNTRIES = countries = [
    "Otros países",
    "España",
    "Chile",
]

@allure.epic('Cambio de POS')
@allure.feature('POS dinámico')
@allure.story('Seleccionar POS y verificar el cambio')
def test_change_pos(driver, start_recording):
    """Test dinámico para cambiar el idioma a uno especificado usando XPath basado en la clase 'language-selector'."""

    booking_page = BookingPage(driver)
    booking_page.open(BASE_URL)  # Abre la página principal

    time.sleep(3)

    for pos in COUNTRIES:
        with allure.step(f"Iniciar la prueba para cambiar el pos a '{pos}'"):
            logger.info(f"Iniciando la prueba para cambiar el pos a '{pos}'")

            booking_page.open_pos_selector()  # Abre el menú de selección de idioma
            logger.info("Selector de pos abierto.")

            time.sleep(2)

            booking_page.select_pos(pos)  # Selecciona el idioma proporcionado
            logger.info(f"POS '{pos}' seleccionado.")

            time.sleep(2)

            booking_page.apply_pos()
            logger.info(f"Se da click en el boton aplicar con el pos a '{pos}'")

            time.sleep(2)


            pos_button_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//*[@id='pointOfSaleSelectorId']//span[2][contains(.,'{pos}')]")))
            selected_pos_text = pos_button_element.text.strip()
            selected_pos_text = selected_pos_text.split('\n')[0].strip()
            assert selected_pos_text == pos, f"El texto del selector POS '{selected_pos_text}' no coincide con el POS esperado '{pos}'"

            logger.info(f"Prueba completada: El pos fue cambiado correctamente a '{pos}'")
            allure.attach(driver.get_screenshot_as_png(), name=f"pos_{pos}",attachment_type=allure.attachment_type.PNG)