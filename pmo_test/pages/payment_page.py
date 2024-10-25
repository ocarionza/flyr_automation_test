from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class PaymentPage(BasePage):
    btn_panel_header_card = (By.XPATH, "//*[contains(@class,'payment_methods_group_item--card-payment')]//panel-header")
    btn_panel_iframe_card = (By.XPATH, "//*[contains(@class,'payment-forms-layout_iframe')]")

    input_card_holder_card = (By.XPATH, "//*[(@id='Holder')]")
    input_card_number_card = (By.ID, "Data")
    dropdown_expire_month_card = (By.ID, "expirationMonth_ExpirationDate")
    dropdown_expire_year_card = (By.ID, "expirationYear_ExpirationDate")
    input_cvv_card = (By.ID, "Cvv")

    DROPDOWN_SELECT_OPTIONS = "//li/button[@class='ui-dropdown_item_option']"
    DROPDOWN_SELECT_VALUE = "//li[starts-with(@class,'ui-dropdown_item') and contains(.,'{}')]"

    CHECK_BOX_PRIVACY_POLICY = (By.XPATH, "//*[@class='payment-container_terms-checkbox']")
    BTN_CONFIRM_AND_PAY = "//*[contains(@class,'ds-btn-primary')]"

    def click_panel_header_card(self):
        self.click(self.btn_panel_header_card)

    def open_iframe_card(self):
        self.driver.switch_to.frame(self.find_element(self.btn_panel_iframe_card))

    def close_iframe_card(self):
        self.driver.switch_to.default_content()

    def type_card_holder_card(self, text):
        self.enter_text(self.input_card_holder_card, text)

    def type_card_number_card(self, text):
        self.enter_text(self.input_card_number_card, text)

    def select_expire_month_card(self, expire_month_value):
        self.click(self.dropdown_expire_month_card)
        if expire_month_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(expire_month_value))
            self.click(locator)

    def select_expire_year_card(self, expire_year_value):
        self.click(self.dropdown_expire_year_card)
        if expire_year_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(expire_year_value))
            self.click(locator)

    def type_cvv_card(self, text):
        self.enter_text(self.input_cvv_card, text)