from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class ServicesPage(BasePage):
    BTN_SERVICE = (By.ID, "serviceButtonTypeBaggage")
    BTN_ADD_SERVICE_FIRST_COLUMN = (By.XPATH, "//div[contains(@class,'service_options')]/div[1]//button[contains(@class,'plus') and not(contains(@class,'disabled'))]")
    BTN_ADD_SERVICE_SECOND_COLUMN = (By.XPATH, "//div[contains(@class,'service_options')]/div[2]//button[contains(@class,'plus') and not(contains(@class,'disabled'))]")
    BTN_CONFIRM_SERVICE = (By.XPATH, "//*[contains(@class,' amount-summary_button-action')]")

    BTN_CONTINUE = (By.XPATH, "//*[contains(@class,'page_button-primary-flow')]")

    def select_service(self):
        self.click(self.BTN_SERVICE)
        while self.validate_element(self.BTN_ADD_SERVICE_FIRST_COLUMN):
            self.click(self.BTN_ADD_SERVICE_FIRST_COLUMN)
            self.click(self.BTN_ADD_SERVICE_SECOND_COLUMN)
        self.click(self.BTN_CONFIRM_SERVICE)
        self.loader_invisibility()

    def click_continue_services(self):
        self.scroll(self.BTN_CONTINUE)
        self.click(self.BTN_CONTINUE)
        self.loader_invisibility()