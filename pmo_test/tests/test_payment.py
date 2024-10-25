import time
import allure
from pages.payment_page import PaymentPage
from utils.logger import get_logger

logger = get_logger()

@allure.epic('Realizar pago')
@allure.feature('Realizar pago')
@allure.story('Realizar pago')
def test_payment(driver, start_recording):

    payment_page = PaymentPage(driver)

    with allure.step(f"Iniciar la prueba para realizar el pago"):

        #payment_page.click_panel_header_card()
        #time.sleep(2)
        payment_page.open_iframe_card()
        time.sleep(2)
        payment_page.type_card_holder_card('Matti Tien')
        time.sleep(2)
        payment_page.type_card_number_card('4099836470157372')
        time.sleep(2)
        payment_page.select_expire_month_card('12')
        time.sleep(2)
        payment_page.select_expire_year_card('27')
        time.sleep(2)
        payment_page.type_cvv_card('547')
        time.sleep(2)
        payment_page.close_iframe_card()



    logger.info("Se ha realizado el pago")

    allure.attach(driver.get_screenshot_as_png(), name="payment_test",attachment_type=allure.attachment_type.PNG)