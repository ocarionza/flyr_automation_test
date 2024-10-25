import time
import allure
from pages.seatmap_page import SeatmapPage
from utils.logger import get_logger

logger = get_logger()

@allure.epic('Seleccionar Asiento')
@allure.feature('Seleccionar Asiento')
@allure.story('Seleccionar Asiento')
def test_seatmap(driver, start_recording):

    seatmap_page = SeatmapPage(driver)

    with allure.step(f"Iniciar la prueba para seleccionar Asiento"):

        seatmap_page.click_pax_select_seat()
        seatmap_page.click_continue_seatmap()
        time.sleep(10)

    logger.info("Se seleccionaron los Asientos correctamente")

    allure.attach(driver.get_screenshot_as_png(), name="seatmap_test",attachment_type=allure.attachment_type.PNG)