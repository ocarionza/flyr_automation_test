from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class SeatmapPage(BasePage):
    ALL_BTN_SEGMENT = "//*[starts-with(@class,'segment-selector_tab ')]"
    BTN_SEGMENT = "//*[starts-with(@class,'segment-selector_tab ')][{}]"
    ALL_PAX = "//*[starts-with(@class,'pax-selector_item ')]"
    BTN_PAX = "//*[starts-with(@class,'pax-selector_item ')][{}]"
    BTN_RESET_SEAT = "//*[@class='pax-selector_list']/div[{}]//button[starts-with(@class,'pax-seat_reset ')]"

    BTN_ANY_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group--')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    BTN_SEAT = "//*[starts-with(@class,'seatmap_group--{}')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]"
    BTN_ANY_PREMIUM_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group-premium)]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    BTN_ANY_ECONOMY_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group--economy')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    BTN_ANY_PLUS_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group--plus')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    BTN_ANY_EMERGENCY_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group--emergency')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    BTN_ANY_FLATBED_SEAT = (By.XPATH, "//*[starts-with(@class,'seatmap_group--flatbed')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")

    BTN_CONTINUE = (By.XPATH, "//*[starts-with(@class,'button amount-summary_button ')][2]")

    def click_segment(self, segment_number):
        locator = (By.XPATH, self.BTN_SEGMENT.format(segment_number))
        self.click(locator)

    def click_all_segment(self):
        elements = self.driver.find_elements(By.XPATH, self.ALL_BTN_SEGMENT)
        count = len(elements)
        for i in range(1, count + 1):
            locator = (By.XPATH, self.BTN_SEGMENT.format(i))
            self.click(locator)
            self.click_pax_select_seat()
            self.loader_invisibility()

    def click_pax(self, pax_number):
        locator = (By.XPATH, self.BTN_PAX.format(pax_number))
        self.click(locator)

    def click_pax_select_seat(self):
        elements = self.driver.find_elements(By.XPATH, self.ALL_PAX)
        count = len(elements)
        for i in range(1, count + 1):
            locator = (By.XPATH, self.BTN_PAX.format(i))
            self.click(locator)
            self.click_select_any_seat()

    def click_select_any_seat(self):
        self.scroll(self.BTN_ANY_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_SEAT)
        self.click(self.BTN_ANY_SEAT)
        self.loader_invisibility()

    def click_select_any_premium_seat(self):
        self.scroll(self.BTN_ANY_PREMIUM_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_PREMIUM_SEAT)
        self.click(self.BTN_ANY_PREMIUM_SEAT)
        self.loader_invisibility()

    def click_select_any_economy_seat(self):
        self.scroll(self.BTN_ANY_ECONOMY_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_ECONOMY_SEAT)
        self.click(self.BTN_ANY_ECONOMY_SEAT)
        self.loader_invisibility()

    def click_select_any_plus_seat(self):
        self.scroll(self.BTN_ANY_PLUS_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_PLUS_SEAT)
        self.click(self.BTN_ANY_PLUS_SEAT)
        self.loader_invisibility()

    def click_select_any_emergency_seat(self):
        self.scroll(self.BTN_ANY_EMERGENCY_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_EMERGENCY_SEAT)
        self.click(self.BTN_ANY_EMERGENCY_SEAT)
        self.loader_invisibility()

    def click_select_any_flatbed_seat(self):
        self.scroll(self.BTN_ANY_FLATBED_SEAT)
        self.scroll_up_arrows(self.BTN_ANY_FLATBED_SEAT)
        self.click(self.BTN_ANY_FLATBED_SEAT)
        self.loader_invisibility()

    def click_continue_seatmap(self):
        self.scroll(self.BTN_CONTINUE)
        self.click(self.BTN_CONTINUE)
        self.loader_invisibility()