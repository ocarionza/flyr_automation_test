import random
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class PassengersPage(BasePage):
    BTN_GENDER_LIST = (By.XPATH, "//button[contains(@id,'IdPaxGender') and not(contains(@class,'has-value'))]")
    INPUT_FIRST_NAME = (By.XPATH, "//*[contains(@id,'IdFirstName') and not(contains(@class,'has-value'))]")
    INPUT_LAST_NAME = (By.XPATH, "//*[contains(@id,'IdLastName') and not(contains(@class,'has-value'))]")

    BTN_DAY = "//*[starts-with(@id,'dateDayId_')][not(contains(@class,'has-value'))]"
    BTN_MONTH = "//*[starts-with(@id,'dateMonthId_')][not(contains(@class,'has-value'))]"
    BTN_YEAR = "//*[starts-with(@id,'dateYearId_')][not(contains(@class,'has-value'))]"

    BTN_NATIONALITY = (By.XPATH, "//button[starts-with(@id,'IdDocNationality') and not(contains(@class,'has-value'))]")
    OPTIONS_NATIONALITY = "//button[contains(@id, 'IdDocNationality_') and not(@style)]"
    OPTION_NATIONALITY = "(//button[contains(@id, 'IdDocNationality_') and not(@style)])[{}]"

    BTN_PHONE_PREFIX = (By.ID, "phone_prefixPhoneId")
    INPUT_PHONE_NUMBER = (By.ID, "phone_phoneNumberId")
    INPUT_EMAIL_ADDRESS = (By.ID, "email")

    DROPDOWN_SELECT_OPTIONS = "//li/button[@class='ui-dropdown_item_option']"
    DROPDOWN_SELECT_VALUE = "//li[starts-with(@class,'ui-dropdown_item') and contains(.,'{}')]"
    DROPDOWN_SELECT_NUMBER = "//li[starts-with(@class,'ui-dropdown_item')][{}]"

    CHECK_BOX_PRIVACY_POLICY = (By.XPATH, "//*[@class='contact_terms ng-star-inserted']")

    BTN_CONTINUE = (By.XPATH, "//button[starts-with(@class,'button page_button')]")

    def select_gender(self):
        self.click(self.BTN_GENDER_LIST)
        gender_value = self.select_random_option('xpath', self.DROPDOWN_SELECT_OPTIONS)
        if gender_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(gender_value))
            self.click(locator)

    def type_first_name(self, text):
        self.enter_text(self.INPUT_FIRST_NAME, text)

    def type_last_name(self, text):
        self.enter_text(self.INPUT_LAST_NAME, text)

    def select_day(self):
        self.click_js(self.BTN_DAY)
        day_value = self.select_random_option('xpath', self.DROPDOWN_SELECT_OPTIONS)
        if day_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(day_value))
            self.click(locator)

    def select_month(self):
        self.click_js(self.BTN_MONTH)
        month_value = self.select_random_option('xpath', self.DROPDOWN_SELECT_OPTIONS)
        if month_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(month_value))
            self.click(locator)

    def select_year(self):
        self.click_js(self.BTN_YEAR)
        year_value = self.select_random_option('xpath', self.DROPDOWN_SELECT_OPTIONS)
        if year_value:
            locator = (By.XPATH, self.DROPDOWN_SELECT_VALUE.format(year_value))
            self.click(locator)

    def select_nationality(self):
        self.click(self.BTN_NATIONALITY)
        elements = self.driver.find_elements(By.XPATH, self.OPTIONS_NATIONALITY)
        count = len(elements)
        random_number = random.randint(1, count)
        if random_number:
            locator = (By.XPATH, self.OPTION_NATIONALITY.format(random_number))
            self.click(locator)

    def validate_nationality(self):
        try:
            self.wait_for_element(self.BTN_NATIONALITY)
            return True
        except TimeoutException:
            return False

    def select_phone_prefix(self):
        self.click(self.BTN_PHONE_PREFIX)
        elements = self.driver.find_elements(By.XPATH, self.DROPDOWN_SELECT_OPTIONS)
        count = len(elements)
        random_number = random.randint(1, count)
        if random_number:
            locator = (By.XPATH, self.DROPDOWN_SELECT_NUMBER.format(random_number))
            self.click(locator)

    def type_phone_number(self, text):
        self.enter_text(self.INPUT_PHONE_NUMBER, text)

    def type_email_address(self, text):
        self.enter_text(self.INPUT_EMAIL_ADDRESS, text)

    def click_check_box_privacy_policy(self):
        self.click(self.CHECK_BOX_PRIVACY_POLICY)

    def click_continue_passengers(self):
        self.scroll(self.BTN_CONTINUE)
        self.click(self.BTN_CONTINUE)
        self.loader_invisibility()