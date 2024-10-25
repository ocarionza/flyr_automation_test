from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class SeatmapPage(BasePage):
    btn_segment = "//*[starts-with(@class,'segment-selector_tab ')][{}]"
    all_pax = "//*[starts-with(@class,'pax-selector_item ')]"
    btn_pax = "//*[starts-with(@class,'pax-selector_item ')][{}]"
    btn_reset_seat = "//*[@class='pax-selector_list']/div[{}]//button[starts-with(@class,'pax-seat_reset ')]"

    btn_any_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group--')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    btn_seat = "//*[starts-with(@class,'seatmap_group--{}')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]"
    btn_any_premium_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group-premium)]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    btn_any_economy_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group--economy')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    btn_any_plus_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group--plus')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    btn_any_emergency_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group--emergency')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")
    btn_any_flatbed_seat = (By.XPATH, "//*[starts-with(@class,'seatmap_group--flatbed')]//button[contains(@class,'seat') and not(contains(@class,'unavailable')) and not(contains(@class,'selected'))]")

    BTN_CONTINUE = (By.XPATH, "//*[starts-with(@class,'button amount-summary_button ')][2]")

    def click_segment(self):
        locator = (By.XPATH, self.btn_segment.format(1))
        self.click(locator)

    def click_pax(self, pax_number):
        locator = (By.XPATH, self.btn_pax.format(pax_number))
        self.click(locator)

    def click_pax_select_seat(self):
        elements = self.driver.find_elements(By.XPATH, self.all_pax)
        count = len(elements)
        for i in range(1, count + 1):
            locator = (By.XPATH, self.btn_pax.format(i))
            self.click(locator)
            self.click_select_any_seat()

    def click_select_any_seat(self):
        self.scroll(self.btn_any_seat)
        self.scroll_up_arrows(self.btn_any_seat)
        self.click(self.btn_any_seat)
        self.loader_invisibility()

    def click_select_any_premium_seat(self):
        self.scroll(self.btn_any_premium_seat)
        self.scroll_up_arrows(self.btn_premium_seat)
        self.click(self.btn_any_premium_seat)
        self.loader_invisibility()

    def click_select_any_economy_seat(self):
        self.scroll(self.btn_any_economy_seat)
        self.scroll_up_arrows(self.btn_economy_seat)
        self.click(self.btn_any_economy_seat)
        self.loader_invisibility()

    def click_select_any_plus_seat(self):
        self.scroll(self.btn_any_plus_seat)
        self.scroll_up_arrows(self.btn_any_plus_seat)
        self.click(self.btn_any_plus_seat)
        self.loader_invisibility()

    def click_select_any_emergency_seat(self):
        self.scroll(self.btn_any_emergency_seat)
        self.scroll_up_arrows(self.btn_any_emergency_seat)
        self.click(self.btn_any_emergency_seat)
        self.loader_invisibility()

    def click_select_any_flatbed_seat(self):
        self.scroll(self.btn_any_flatbed_seat)
        self.scroll_up_arrows(self.btn_any_flatbed_seat)
        self.click(self.btn_any_flatbed_seat)
        self.loader_invisibility()

    def click_continue_seatmap(self):
        self.scroll(self.BTN_CONTINUE)
        self.click(self.BTN_CONTINUE)
        self.loader_invisibility()