import time
import allure
from config.environment import BASE_URL
from pages.booking_page import BookingPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()

@allure.epic('Reservacion ONE WAY')
@allure.feature('Reservacion ONE WAY')
@allure.story('Realizar booking One-way (Solo ida) realizando las siguientes validaciones en cada página.')
def test_booking(driver, start_recording):
    """Test dinámico para cambiar el idioma a uno especificado usando XPath basado en la clase 'language-selector'."""

    booking_page = BookingPage(driver)
    booking_page.open(BASE_URL)  # Abre la página principal
    time.sleep(3)

    with allure.step(f"Iniciar la prueba para realizar booking one way "):

        booking_page.open_language_dropdown()
        time.sleep(2)
        booking_page.select_language("English")  # Selecciona el idioma proporcionado
        time.sleep(2)
        booking_page.open_pos_selector()
        time.sleep(2)
        booking_page.select_pos("Colombia")
        time.sleep(2)
        booking_page.apply_pos()
        time.sleep(2)

        logger.info("Idioma y POS seleccionados")

        booking_page.click_one_way()
        time.sleep(2)
        booking_page.write_origin('PEI')
        time.sleep(2)
        booking_page.write_destination('CTG')

        logger.info("se completo la prueba de reserva")

    allure.attach(driver.get_screenshot_as_png(), name=f"booking_one_way",attachment_type=allure.attachment_type.PNG)