import time
import allure
from pages.payment_page import PaymentPage
from selenium.webdriver.common.devtools.v85.debugger import pause
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
        payment_page.type_card_holder_card('Quinzia Tobenna')
        time.sleep(2)
        payment_page.type_card_number_card('4544001898922433')
        time.sleep(2)
        payment_page.select_expire_month_card('07')
        time.sleep(2)
        payment_page.select_expire_year_card('26')
        time.sleep(2)
        payment_page.type_cvv_card('826')
        time.sleep(2)
        payment_page.close_iframe_card()
        time.sleep(2)
        payment_page.type_email_card('zajoseza@gamil.com')
        time.sleep(2)
        payment_page.type_address_card('CR 10 B # 50 A 39')
        time.sleep(2)
        payment_page.type_city_card('Manizales')
        time.sleep(2)
        payment_page.select_country()
        time.sleep(2)
        payment_page.click_check_box_privacy_policy()
        time.sleep(2)
        payment_page.click_btn_confirm_pay()

    logger.info("Se ha realizado el pago")

    allure.attach(driver.get_screenshot_as_png(), name="payment_test",attachment_type=allure.attachment_type.PNG)