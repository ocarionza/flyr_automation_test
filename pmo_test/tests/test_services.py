import time
import allure
from faker import Faker
from pages.services_page import ServicesPage
from utils.logger import get_logger

faker = Faker()
logger = get_logger()

@allure.epic('Seleccionar servicios')
@allure.feature('Seleccionar servicios')
@allure.story('Seleccionar servicios')
def test_services(driver, start_recording):

    services_page = ServicesPage(driver)

    with allure.step(f"Iniciar la prueba para seleccionar servicios"):

        services_page.select_service()
        time.sleep(2)
        services_page.click_continue_services()
        time.sleep(5)

    logger.info("Se seleccionaron los servicios correctamente")

    allure.attach(driver.get_screenshot_as_png(), name="services_test",attachment_type=allure.attachment_type.PNG)