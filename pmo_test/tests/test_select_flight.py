import time
import allure
from pages.flight_page import FlightPage
from utils.logger import get_logger

logger = get_logger()

@allure.epic('Selecionar vuelo')
@allure.feature('Selecionar vuelo')
@allure.story('Seleccionar tarifa Basic.')
def test_select_flight(driver, start_recording):
    flight_page = FlightPage(driver)

    with allure.step(f"Iniciar la prueba para seleccionar vuelo"):

        flight_page.click_select_flight_and_show_fares()
        flight_page.select_fare("basic")
        allure.attach(driver.get_screenshot_as_png(), name="select_flight", attachment_type=allure.attachment_type.PNG)
        flight_page.click_continue()
        time.sleep(5)

        logger.info("se completo la seleccion de vuelo")
