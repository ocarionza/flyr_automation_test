import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class PaymentPage(BasePage):
    BTN_PANEL_HEADER_CARD = (By.XPATH, "//*[contains(@class,'payment_methods_group_item--card-payment')]//panel-header")
    BTN_PANEL_IFRAME_CARD = (By.XPATH, "//*[contains(@class,'payment-forms-layout_iframe')]")

    INPUT_CARD_HOLDER_CARD = (By.ID, "Holder")
    INPUT_CARD_NUMBER_CARD = (By.ID, "Data")
    DROPDOWN_EXPIRE_MONTH_CARD = (By.ID, "expirationMonth_ExpirationDate")
    DROPDOWN_EXPIRE_YEAR_CARD = (By.ID, "expirationYear_ExpirationDate")
    INPUT_CVV_CARD = (By.ID, "Cvv")

    INPUT_EMAIL = (By.XPATH, "(//*[contains(@id, 'PaymentAmount_')])[1]")
    INPUT_ADDRESS = (By.XPATH, "(//*[contains(@id, 'PaymentAmount_')])[2]")
    INPUT_CITY = (By.XPATH, "(//*[contains(@id, 'PaymentAmount_')])[3]")

    INPUT_COUNTRY = (By.XPATH, "//*[contains(@class,'ds-select-container')]//button")
    DS_SELECT_OPTIONS = "//li/button[@class='ds-select-dropdown_item_option']"
    DS_SELECT_VALUE = "(//li/button[@class='ds-select-dropdown_item_option'])[{}]"

    DROPDOWN_SELECT_OPTIONS = "//li/button[@class='ui-dropdown_item_option']"
    DROPDOWN_SELECT_VALUE = "//li[starts-with(@class,'ui-dropdown_item') and contains(.,'{}')]"
    CHECK_BOX_PRIVACY_POLICY = (By.XPATH, "//*[@class='payment-container_terms-checkbox']//input")
    BTN_CONFIRM_AND_PAY = (By.XPATH, "//*[contains(@class,'ds-btn-primary')]")

    def click_panel_header_card(self):
        self.click(self.BTN_PANEL_HEADER_CARD)

    def open_iframe_card(self):
        self.driver.switch_to.frame(self.find_element(self.BTN_PANEL_IFRAME_CARD))

    def close_iframe_card(self):
        self.driver.switch_to.default_content()

    def type_card_holder_card(self, text):
        self.enter_text(self.INPUT_CARD_HOLDER_CARD, text)

    def type_card_number_card(self, text):
        self.enter_text(self.INPUT_CARD_NUMBER_CARD, text)

    def select_expire_month_card(self, expire_month_value):
        self.click(self.DROPDOWN_EXPIRE_MONTH_CARD)
        if expire_month_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(expire_month_value))
            self.click(locator)

    def select_expire_year_card(self, expire_year_value):
        self.click(self.DROPDOWN_EXPIRE_YEAR_CARD)
        if expire_year_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(expire_year_value))
            self.click(locator)

    def type_cvv_card(self, text):
        self.enter_text(self.INPUT_CVV_CARD, text)

    def type_email_card(self, text):
        self.enter_text(self.INPUT_EMAIL, text)

    def type_address_card(self, text):
        self.enter_text(self.INPUT_ADDRESS, text)

    def type_city_card(self, text):
        self.enter_text(self.INPUT_CITY, text)

    def select_country(self):
        self.click(self.INPUT_COUNTRY)
        elements = self.driver.find_elements(By.XPATH, self.DS_SELECT_OPTIONS)
        count = len(elements)
        random_number = random.randint(1, count)
        if random_number:
            locator = (By.XPATH, self.DS_SELECT_VALUE.format(random_number))
            self.click(locator)

    def click_check_box_privacy_policy(self):
        self.click(self.CHECK_BOX_PRIVACY_POLICY)

    def click_btn_confirm_pay(self):
        self.scroll(self.BTN_CONFIRM_AND_PAY)
        self.click(self.BTN_CONFIRM_AND_PAY)
        self.loader_invisibility()