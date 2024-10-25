import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class PassengersPage(BasePage):
    btn_gender_list = (By.XPATH, "//button[contains(@id,'IdPaxGender') and not(contains(@class,'has-value'))]")
    input_first_name = (By.XPATH, "//*[contains(@id,'IdFirstName') and not(contains(@class,'has-value'))]")
    input_last_name = (By.XPATH, "//*[contains(@id,'IdLastName') and not(contains(@class,'has-value'))]")

    btn_day = "//*[starts-with(@id,'dateDayId_')][not(contains(@class,'has-value'))]"
    btn_month = "//*[starts-with(@id,'dateMonthId_')][not(contains(@class,'has-value'))]"
    btn_year = "//*[starts-with(@id,'dateYearId_')][not(contains(@class,'has-value'))]"

    btn_nationality = (By.XPATH, "//button[starts-with(@id,'IdDocNationality') and not(contains(@class,'has-value'))]")
    options_nationality = "//button[contains(@id, 'IdDocNationality_') and not(@style)]"
    option_nationality = "//button[contains(@id, 'IdDocNationality_') and not(@style) and contains(.,'{}')]"

    btn_frequent_flyer_program_list = (By.ID, "customerPrograms")
    input_frequent_flyer_number = (By.ID, "AVloyaltyNumber")

    btn_phone_prefix = (By.ID, "phone_prefixPhoneId")
    input_phone_number = (By.ID, "phone_phoneNumberId")
    input_email_address = (By.ID, "email")

    dropdown_select_options = "//li/button[@class='ui-dropdown_item_option']"
    dropdown_select_value = "//li[starts-with(@class,'ui-dropdown_item') and contains(.,'{}')]"

    check_box_privacy_policy = (By.XPATH, "//*[@class='contact_terms ng-star-inserted']")

    btn_continue = (By.XPATH, "//button[starts-with(@class,'button page_button')]")

    def select_gender(self):
        self.click(self.btn_gender_list)
        gender_value = self.select_random_option('xpath', self.dropdown_select_options)
        if gender_value:
            locator = (By.XPATH, self.dropdown_select_value.format(gender_value))
            self.click(locator)

    def type_first_name(self, text):
        self.enter_text(self.input_first_name, text)

    def type_last_name(self, text):
        self.enter_text(self.input_last_name, text)

    def select_day(self):
        self.click_js(self.btn_day)
        day_value = self.select_random_option('xpath', self.dropdown_select_options)
        if day_value:
            locator = (By.XPATH, self.dropdown_select_value.format(day_value))
            self.click(locator)

    def select_month(self):
        self.click_js(self.btn_month)
        month_value = self.select_random_option('xpath', self.dropdown_select_options)
        if month_value:
            locator = (By.XPATH, self.dropdown_select_value.format(month_value))
            self.click(locator)

    def select_year(self):
        self.click_js(self.btn_year)
        year_value = self.select_random_option('xpath', self.dropdown_select_options)
        if year_value:
            locator = (By.XPATH, self.dropdown_select_value.format(year_value))
            self.click(locator)

    def select_nationality(self):
        self.click(self.btn_nationality)
        nationality_value = self.select_random_option('xpath', self.options_nationality)
        if nationality_value:
            locator = (By.XPATH, self.option_nationality.format(nationality_value))
            self.click(locator)

    def select_frequent_flyer_program(self):
        self.click(self.btn_frequent_flyer_program_list)
        program_list_value = self.select_random_option('xpath', self.dropdown_select_options)
        if program_list_value:
            locator = (By.XPATH, self.dropdown_select_value.format(program_list_value))
            self.click(locator)

    def type_frequent_flyer_number(self, text):
        self.enter_text(self.input_frequent_flyer_number, text)

    def select_phone_prefix(self):
        self.click(self.btn_phone_prefix)
        phone_prefix_value = self.select_random_option('xpath', self.dropdown_select_options + "/span[1]")
        if phone_prefix_value:
            locator = (By.XPATH, self.dropdown_select_value.format(phone_prefix_value))
            self.click(locator)

    def type_phone_number(self, text):
        self.enter_text(self.input_phone_number, text)

    def type_email_address(self, text):
        self.enter_text(self.input_email_address, text)

    def click_check_box_privacy_policy(self):
        self.click(self.check_box_privacy_policy)

    def click_continue_passengers(self):
        self.scroll(self.btn_continue)
        self.click(self.btn_continue)
        self.loader_invisibility()