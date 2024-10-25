import time
import allure
import pytest
from config.environment import BASE_URL
from pages.booking_page import BookingPage
from utils.logger import get_logger
from .test_select_flight import test_select_flight
from .test_passengers import test_fill_passengers
from .test_services import test_services

logger = get_logger()

@allure.epic('Reservacion ONE WAY')
@allure.feature('Reservacion ONE WAY')
@allure.story('Realizar booking One-way (Solo ida) realizando las siguientes validaciones en cada página.')
@pytest.mark.oneway
def test_booking(driver, start_recording):

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
        time.sleep(2)
        booking_page.click_passengers()
        time.sleep(2)
        booking_page.add_youth()
        time.sleep(2)
        booking_page.add_child()
        time.sleep(2)
        booking_page.add_infant()
        time.sleep(2)
        booking_page.click_confirm()
        time.sleep(3)
        booking_page.click_search()
        time.sleep(5)
        booking_page.loader_invisibility()
        time.sleep(2)
        test_select_flight(driver, start_recording)
        test_fill_passengers(driver, start_recording)
        test_services(driver, start_recording)

        logger.info("se completo la prueba de reserva")

    allure.attach(driver.get_screenshot_as_png(), name=f"booking_one_way",attachment_type=allure.attachment_type.PNG)