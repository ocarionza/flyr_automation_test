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

        passengers_page.select_gender()
        time.sleep(2)
        passengers_page.type_first_name(first_name)
        time.sleep(2)
        passengers_page.type_last_name(last_name)
        time.sleep(2)
        passengers_page.select_year()
        time.sleep(2)
        passengers_page.select_month()
        time.sleep(2)
        passengers_page.select_day()
        time.sleep(2)
        passengers_page.select_nationality()
        time.sleep(2)

        passengers_page.select_phone_prefix()
        time.sleep(2)
        passengers_page.type_phone_number(1234567890)
        time.sleep(2)
        passengers_page.type_email_address("zajoseza@gmail.com")
        time.sleep(2)
        passengers_page.click_check_box_privacy_policy()
        time.sleep(2)
        passengers_page.click_continue_passengers()
        time.sleep(5)

        logger.info("Se llenaron los datos correctamente")

    allure.attach(driver.get_screenshot_as_png(), name="fill_passengers",attachment_type=allure.attachment_type.PNG)