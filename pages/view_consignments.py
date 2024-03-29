# coding=utf-8
from pages.base import BasePage
from pages.consignment_page import ConsignmentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep





class ViewConsignmentsPage(BasePage):
    _title = "View consignment"

    _category_furniture = (By.XPATH, "//label/a")
    _category_parcels = (By.XPATH, "//div[7]/div/div/label/a")
    _search_in_region = (By.XPATH, "//form/div/div/label")
    _province_posting_in_selected_region_checkbox = (By.XPATH, "//div[2]/div/div/div/div/div/label")
    _province_field = (By.ID, "AuctionSearch_region_vueRegion")
    _province_dropdown_first_result = (By.XPATH, "//form/div/div[2]/div/div[2]/div/div")
    _auction_search = (By.ID, "AuctionSearch_title")
    _auction_search_button = (By.ID, "AuctionSearch_submit")
    _first_result = (By.XPATH, "//h3/a")
    _first_result_posting_province = (By.XPATH, "//td[3]/span")
    _title_uuid = 1

    def __init__(self, driver):
        super(ViewConsignmentsPage, self).__init__(driver, self._title)

    def search_for_added_consignment(self):
        self.click(self._category_furniture, "The category <Furniture> button couldn't be clicked or wasn't visible on view consignments page")
        self.send_keys(self._title_uuid, self._auction_search, "The attempt to enter added consignment title into the search field on view consignments page was unsuccessful")
        self.click(self._auction_search_button, "The auction search button couldn't be clicked or wasn't visible on view consignments page")
        self.get_driver().execute_script("window.scrollTo(1, 1);")

    def open_added_consignment(self):
        # _first_result_value = (By.PARTIAL_LINK_TEXT, self._title_uuid)
        # self.click(_first_result_value)
        self.click(self._first_result, "The first result on view consignments page couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())

    def check_categories(self):
        self.click(self._category_parcels, "The category <Parcels> button couldn't be clicked or wasn't visible on view consignments page")
        self.condition_click(self._search_in_region, "The <Search in region> button couldn't be clicked or wasn't visible on view consignments page")
        self.send_keys("m", self._province_field)
        self.send_keys("a", self._province_field)
        self.send_keys("z", self._province_field)
        sleep(1)
        self.send_keys("o", self._province_field)
        sleep(1)
        self.send_keys("w", self._province_field)
        sleep(4)
        # self.send_keys('\b', self._province_field)
        self.condition_click(self._province_dropdown_first_result, "The attempt to click first result on province dropdown on view consignments page was unsuccessful")
        self.click(self._province_posting_in_selected_region_checkbox, "The province posting in selected region checkbox on view consignments page couldn't be clicked or wasn't visible")
        self.click(self._auction_search_button, "The auction search button couldn't be clicked or wasn't visible on view consignments page")

    def click_first_result(self):
        self.click(self._first_result, "The first result on view consignments page couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())