from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class FlightPage(BasePage):
    BTN_SHOW_FARES = (By.XPATH, "//div[2]/div[starts-with(@class,'journey-select_list ng-star-inserted')]/div/journey-control-custom/div/div/div/div[2]")
    BTN_SELECT_FARE = "//div[contains(@class,'fare-control') and contains(@aria-label,'{}')]"
    BTN_CONTINUE = (By.XPATH, "//button[contains(@class,'page_button-primary-flow')]")

    def click_select_flight_and_show_fares(self):
        self.click(self.BTN_SHOW_FARES)

    def select_fare(self, fare):
        select_fare = (By.XPATH, self.BTN_SELECT_FARE.format(fare))
        self.wait_for_element(select_fare)
        self.click(select_fare)
        self.loader_invisibility()

    def click_continue(self):
        self.scroll(self.BTN_CONTINUE)
        self.click(self.BTN_CONTINUE)
        self.loader_invisibility()