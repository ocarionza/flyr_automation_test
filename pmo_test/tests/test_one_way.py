import allure
import pytest
from config.environment import BASE_URL
from pages.booking_page import BookingPage
from utils.logger import get_logger
from .test_select_flight import test_select_flight
from .test_passengers import test_fill_passengers
from .test_services import test_services
from .test_seatmap import test_seatmap
from .test_payment import test_payment

logger = get_logger()

@allure.epic('Reservacion ONE WAY')
@allure.feature('Reservacion ONE WAY')
@allure.story('Realizar booking One-way (Solo ida) realizando las siguientes validaciones en cada página.')
@pytest.mark.oneway
def test_booking(driver, start_recording):

    booking_page = BookingPage(driver)
    booking_page.open(BASE_URL)  # Abre la página principal

    with allure.step(f"Iniciar la prueba para realizar booking one way "):

        booking_page.open_language_dropdown()
        booking_page.select_language("English")  # Selecciona el idioma proporcionado
        booking_page.open_pos_selector()
        booking_page.select_pos("Colombia")
        booking_page.apply_pos()
        allure.attach(driver.get_screenshot_as_png(), name=f"booking_one_way",attachment_type=allure.attachment_type.PNG)
        logger.info("Idioma y POS seleccionados")

        booking_page.click_one_way()
        booking_page.write_origin('PEI')
        booking_page.write_destination('CTG')
        allure.attach(driver.get_screenshot_as_png(), name=f"booking_one_way",attachment_type=allure.attachment_type.PNG)
        booking_page.click_passengers()
        booking_page.add_youth()
        booking_page.add_child()
        booking_page.add_infant()
        allure.attach(driver.get_screenshot_as_png(), name=f"booking_one_way",attachment_type=allure.attachment_type.PNG)
        booking_page.click_confirm()
        booking_page.click_search()
        booking_page.loader_invisibility()
        test_select_flight(driver, start_recording)
        test_fill_passengers(driver, start_recording)
        test_services(driver, start_recording)
        test_seatmap(driver, start_recording)
        test_payment(driver, start_recording)

        logger.info("se completo la prueba de reserva")