import time
import allure
from faker import Faker
from pages.passengers_page import PassengersPage
from utils.logger import get_logger

faker = Faker()
logger = get_logger()

@allure.epic('Datos pasajeros')
@allure.feature('Datos pasajeros')
@allure.story('Passengers: Ingresar la información de los pasajeros.')
def test_fill_passengers(driver, start_recording):

    passengers_page = PassengersPage(driver)

    with allure.step(f"Iniciar la prueba para llenar datos de pasajeros"):

        first_name = faker.first_name()
        last_name = faker.last_name()

        while passengers_page.validate_nationality():
            passengers_page.select_gender()
            passengers_page.type_first_name(first_name)
            passengers_page.type_last_name(last_name)
            passengers_page.select_year()
            passengers_page.select_month()
            passengers_page.select_day()
            passengers_page.select_nationality()
            allure.attach(driver.get_screenshot_as_png(), name="fill_passengers",attachment_type=allure.attachment_type.PNG)
            time.sleep(1)

        passengers_page.select_phone_prefix()
        passengers_page.type_phone_number(1234567890)
        passengers_page.type_email_address("zajoseza@gmail.com")
        passengers_page.click_check_box_privacy_policy()
        allure.attach(driver.get_screenshot_as_png(), name="fill_passengers", attachment_type=allure.attachment_type.PNG)
        passengers_page.click_continue_passengers()
        time.sleep(5)

        logger.info("Se llenaron los datos correctamente")