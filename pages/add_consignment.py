# coding=utf-8
import datetime
from pages.base import BasePage
from pages.page import *
from pages.view_consignments import ViewConsignmentsPage
from selenium.webdriver.common.by import By
from time import sleep
from utils.utils import *
from pages.consignment_page import ConsignmentPage



class AddConsignmentPage(BasePage):

    _title = "Add consignment"

    _category_dropdown = (By.XPATH, "//div[@id='categories']/form/div/div/div/div/div/div/div")
    _category_furniture = (By.LINK_TEXT, "Meble")
    _category_parcels = (By.XPATH, "//div[7]/a/span")
    _category_cars = (By.XPATH, "//div[3]/a/span")
    _consignment_title_field = (By.ID, "EditAuction_title")
    _send_city_field = (By.ID, "sendLocation")
    _receive_city_field = (By.ID, "receiveLocation")
    _placeholder_results1 = (By.XPATH, "/html/body/div[8]/div[2]/form/div[1]/div[1]/div[3]/div[7]/div/div[1]/div/div")
    _placeholder_results2 = (By.XPATH, "/html/body/div[8]/div[2]/form/div[1]/div[1]/div[3]/div[7]/div/div[2]/div/div")
    _date_fixed_checkbox = (By.XPATH, "//label")
    _today = datetime.date.today()
    _tomorrow = datetime.date.today()+ datetime.timedelta(1)
    _2_days_ahead = datetime.date.today()+ datetime.timedelta(2)
    _send_date_field = (By.NAME, "EditAuction[sendDate]")
    _send_date_value = _today.strftime('%Y-%m-%d')+" - "+_tomorrow.strftime('%Y-%m-%d')
    _send_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month)+"-"+str(datetime.date.today().day)+" - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1"
    # _send_date_from_field = (By.NAME, "daterangepicker_start")
    # _send_date_from_value = _today.strftime('%Y-%m-%d')
    # _send_date_to_field = (By.NAME, "daterangepicker_end")
    # _send_date_to_value = _tomorrow.strftime('%Y-%m-%d')
    _send_date_from_next_month_button = (By.XPATH, "/html/body/div[13]/div[2]/div[2]/table/tbody/tr[3]/td[1]")
    _send_date_to_next_month_button = (By.XPATH, "/html/body/div[13]/div[2]/div[2]/table/tbody/tr[3]/td[2]")
    _send_date_from_next_month_older_button = (By.CSS_SELECTOR, "body > div:nth-child(18) > div.calendar.left > div.calendar-table > table > tbody > tr:nth-child(3) > td:nth-child(3)")
    _send_date_to_next_month_older_button = (By.CSS_SELECTOR, "body > div:nth-child(18) > div.calendar.left > div.calendar-table > table > tbody > tr:nth-child(3) > td:nth-child(4)")
    _send_date_from_next_month_edit_button = (By.XPATH, "/html/body/div[10]/div[2]/div[2]/table/tbody/tr[3]/td[1]")
    _send_date_to_next_month_edit_button = (By.XPATH, "/html/body/div[10]/div[2]/div[2]/table/tbody/tr[3]/td[2]")
    # _receive_date_from_field = (By.XPATH, "(//input[@name='daterangepicker_start'])[2]")
    # _receive_date_from_value = _tomorrow.strftime('%Y-%m-%d')
    # _receive_date_to_field = (By.XPATH, "(//input[@name='daterangepicker_end'])[2]")
    # _receive_date_to_value = _2_days_ahead.strftime('%Y-%m-%d')
    _receive_date_field = (By.ID, "EditAuction_receiveDate")
    _receive_date_value = _tomorrow.strftime('%Y-%m-%d')+" - "+_2_days_ahead.strftime('%Y-%m-%d')
    _receive_date_value_next_month = str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-1 - "+str(datetime.date.today().year)+"-"+str(datetime.date.today().month+1)+"-2"
    _receive_date_from_next_month_button = (By.XPATH, "/html/body/div[14]/div[2]/div[2]/table/tbody/tr[4]/td[1]")
    _receive_date_to_next_month_button = (By.XPATH, "/html/body/div[14]/div[2]/div[2]/table/tbody/tr[4]/td[2]")
    _receive_date_from_next_month_older_button = (By.CSS_SELECTOR, "body > div:nth-child(19) > div.calendar.left > div.calendar-table > table > tbody > tr:nth-child(4) > td:nth-child(3)")
    _receive_date_to_next_month_older_button = (By.CSS_SELECTOR, "body > div:nth-child(19) > div.calendar.left > div.calendar-table > table > tbody > tr:nth-child(4) > td:nth-child(4)")
    _receive_date_from_next_month_edit_button = (By.XPATH, "/html/body/div[11]/div[2]/div[2]/table/tbody/tr[4]/td[1]")
    _receive_date_to_next_month_edit_button = (By.XPATH, "/html/body/div[11]/div[2]/div[2]/table/tbody/tr[4]/td[2]")
    _additional_info_button = (By.XPATH, "//div[3]/div/label")
    _submit_consignment_button = (By.ID, "EditAuction_submit")
    _consignment_length = (By.ID, "EditAuction_item_length")
    _consignment_length_value = get_random_integer(1)
    _consignment_width = (By.ID, "EditAuction_item_width")
    _consignment_width_value = get_random_integer(1)
    _consignment_height = (By.ID, "EditAuction_item_height")
    _consignment_height_value = get_random_integer(1)
    _consignment_weight = (By.ID, "EditAuction_item_weight")
    _consignment_weight_value = get_random_integer(2)
    _consignment_cars_brand_field = (By.ID, "EditAuction_item_model")
    _consignment_cars_brand_value = get_random_string(8)
    _quantity = (By.ID, "EditAuction_item_itemsNumber")
    _quantity_value = get_random_integer(2)
    _type_of_service_dropdown = (By.XPATH, "//div[@id='form']/div[4]/div/div")
    _type_of_service_complex_service_option = (By.XPATH, "//div[4]/div/div[2]/div[2]")
    _budget = (By.ID, "EditAuction_budget")
    _additional_info = (By.ID, "EditAuction_description")
    _save_edit_consignment = (By.XPATH, "//input[@value='Zapisz zmiany']")
    _view_added_consignment_button = (By.XPATH, "//a[contains(text(),'Wolę poczekać na oferty')]")
    _consignment_title_result_page = (By.XPATH, "//span/a")
    _consignment_title_result_page_after_payment = (By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[2]/strong/a")
    _first_offer = (By.XPATH, "//div[4]/button")
    _highlited_checkbox = (By.NAME, "auction_special")
    _urgent_checkbox = (By.NAME, "auction_important")
    _test_payment_radio = (By.XPATH, "//input[@value='t']")
    _invoice_company_country = (By.ID, "invoice_company_country")
    _submit_payment_button = (By.XPATH, "//input[@value='Płacę']")
    _payu_accept_button = (By.XPATH, "//input")
    _payu_valid_authorization = (By.XPATH, "/html/body/div/div[2]/div/div[1]/div/table/tbody/tr/td[1]/form/input[1]")
    _first_payment_date_field = (By.XPATH, "/html/body/div[1]/div[3]/div[4]/div[3]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[3]")
    _edit_consignment_result_field = (By.XPATH, "/html/body/div[8]/div")
    _after_adding_consignment_text_field = (By.CSS_SELECTOR, "h1")
    _after_adding_consignment_unlogged_text_field = (By.CSS_SELECTOR, "div.header")
    _view_consignments_header = (By.XPATH, "//a[2]/h2")

    def __init__(self, driver):
        super(AddConsignmentPage, self).__init__(driver, self._title)
        self._title_uuid = get_random_uuid(7)
        ViewConsignmentsPage._title_uuid = self._title_uuid

    def new_furniture_consignment(self):
        self.click(self._category_dropdown, "The category dropdown on new consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_furniture, "The category <Furniture> on category dropdown on new consignment page couldn't be clicked or wasn't visible")
        self.send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on add consignment page was unsuccessful")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.get_driver().execute_script("document.getElementsByName('EditAuction[sendDate]')[0].removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.get_driver().execute_script("document.getElementById('EditAuction_receiveDate').removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._send_date_field, "The click on send date field on add consignement page was unsuccessful")
        self._send_date_from_value = self.get_text(self._send_date_from_next_month_button)
        self._send_date_to_value = self.get_text(self._send_date_to_next_month_button)
        self.click(self._send_date_from_next_month_button, "The click on send date <from> cell on datepicker on add consignement page was unsuccessful")
        self.click(self._send_date_to_next_month_button, "The click on send date <to> cell on datepicker on add consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        # self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field, "The click on receive date field on add consignement page was unsuccessful")
        self._receive_date_from_value = self.get_text(self._receive_date_from_next_month_button)
        self._receive_date_to_value = self.get_text(self._receive_date_to_next_month_button)
        self.click(self._receive_date_from_next_month_button, "The click on receive date <from> cell on datepicker on add consignement page was unsuccessful")
        self.click(self._receive_date_to_next_month_button, "The click on receive date <to> cell on datepicker on add consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        # self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.if_not_visible_click(self._consignment_length, self._additional_info_button)
        # self.condition_click(self._additional_info_button, "The additional info button on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._consignment_length_value, self._consignment_length, "The attempt to enter random integer to consignment length field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_width_value, self._consignment_width, "The attempt to enter random integer to consignment width field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_height_value, self._consignment_height, "The attempt to enter random integer to consignment height field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_weight_value, self._consignment_weight, "The attempt to enter random integer to consignment weight field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._quantity_value, self._quantity, "The attempt to enter random integer to consignment quantity field on add consignment page was unsuccessful")
        self.click(self._type_of_service_dropdown, "The type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info", self._additional_info, "The attempt to enter <This is my additional info> to consignment additional info field on add consignment page was unsuccessful")
        self.send_keys(u"Wrocław, Polska", self._send_city_field, "The attempt to enter <Wrocław> into send city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on add consignment page couldn't be clicked or wasn't visible")
        self.send_keys(u"Radom, Polska", self._receive_city_field, "The attempt to enter <Warszawa> into receive city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on add consignment page couldn't be clicked or wasn't visible")
        return self._title_uuid

    def edit_consignment_parcel(self):
        self.click(self._category_dropdown, "The category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._category_parcels))
        self.click(self._category_parcels, "The category <Parcels> on category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on edit consignment page was unsuccessful")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.get_driver().execute_script("document.getElementsByName('EditAuction[sendDate]')[0].removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.get_driver().execute_script("document.getElementById('EditAuction_receiveDate').removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._send_date_field, "The click on send date field on edit consignement page was unsuccessful")
        self._send_date_from_edit_value = self.get_text(self._send_date_from_next_month_edit_button)
        self._send_date_to_edit_value = self.get_text(self._send_date_to_next_month_edit_button)
        self.click(self._send_date_from_next_month_edit_button, "The click on send date <from> cell on datepicker on edit consignement page was unsuccessful")
        self.click(self._send_date_to_next_month_edit_button, "The click on send date <to> cell on datepicker on edit consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        # self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field, "The click on receive date field on edit consignement page was unsuccessful")
        self._receive_date_from_edit_value = self.get_text(self._receive_date_from_next_month_edit_button)
        self._receive_date_to_edit_value = self.get_text(self._receive_date_to_next_month_edit_button)
        self.click(self._receive_date_from_next_month_edit_button, "The click on receive date <from> cell on datepicker on edit consignement page was unsuccessful")
        self.click(self._receive_date_to_next_month_edit_button, "The click on receive date <to> cell on datepicker on edit consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        # self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Katowice, Polska", self._send_city_field, "The attempt to enter <Katowice> into send city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań, Polska", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on edit consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        self.if_not_visible_click(self._consignment_length, self._additional_info_button)
        # self.condition_click(self._additional_info_button, "The additional info button on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._consignment_length_value, self._consignment_length, "The attempt to enter random integer to consignment length field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_width_value, self._consignment_width, "The attempt to enter random integer to consignment width field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_height_value, self._consignment_height, "The attempt to enter random integer to consignment height field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_weight_value, self._consignment_weight, "The attempt to enter random integer to consignment weight field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._quantity_value, self._quantity, "The attempt to enter random integer to consignment quantity field on edit consignment page was unsuccessful")
        # self.click(self._type_of_service_dropdown, "The type of service dropdown on edit consignment page couldn't be clicked or wasn't visible")
        # self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on edit consignment page couldn't be clicked or wasn't visible")
        # self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info after edit", self._additional_info, "The attempt to enter <This is my additional info after edit> to consignment additional info field on edit consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on edit consignment page couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())

    def edit_consignment_cars(self):
        self.click(self._category_dropdown, "The category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.click(self._category_cars, "The category <Parcels> on category dropdown on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on edit consignment page was unsuccessful")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.get_driver().execute_script("document.getElementsByName('EditAuction[sendDate]')[0].removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.get_driver().execute_script("document.getElementById('EditAuction_receiveDate').removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._send_date_field, "The click on send date field on edit consignement page was unsuccessful")
        sleep(1)
        self._send_date_from_older_value = self.get_text(self._send_date_from_next_month_older_button)
        self._send_date_to_older_value = self.get_text(self._send_date_to_next_month_older_button)
        self.click(self._send_date_from_next_month_older_button, "The click on send date <from> cell on datepicker on edit consignement page was unsuccessful")
        self.click(self._send_date_to_next_month_older_button, "The click on send date <to> cell on datepicker on edit consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        # self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field, "The click on receive date field on edit consignement page was unsuccessful")
        sleep(1)
        self._receive_date_from_older_value = self.get_text(self._receive_date_from_next_month_older_button)
        self._receive_date_to_older_value = self.get_text(self._receive_date_to_next_month_older_button)
        self.click(self._receive_date_from_next_month_older_button, "The click on receive date <from> cell on datepicker on edit consignement page was unsuccessful")
        self.click(self._receive_date_to_next_month_older_button, "The click on receive date <to> cell on datepicker on edit consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        # self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Katowice, Polska", self._send_city_field, "The attempt to enter <Katowice> into send city field on edit consignment page was unsuccessful")
        sleep(1)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        # self.click(self._placeholder_results1)
        self.click(self._receive_city_field, "The receive city field on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań, Polska", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on edit consignment page was unsuccessful")
        sleep(1)
        # self.click(self._placeholder_results2)
        self.click(self._consignment_title_field, "The consignment title field on edit consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on edit consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on edit consignment page was unsuccessful")
        self.if_not_visible_click(self._consignment_cars_brand_field, self._additional_info_button)
        # self.condition_click(self._additional_info_button, "The additional info button on edit consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._consignment_cars_brand_value, self._consignment_cars_brand_field, "The attempt to enter random text to consignment cars brand and model field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys(self._consignment_weight_value, self._consignment_weight, "The attempt to enter random integer to consignment weight field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on edit consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info after edit", self._additional_info, "The attempt to enter <This is my additional info after edit> to consignment additional info field on edit consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on edit consignment page couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())

    def view_added_consignment(self):
        self.click(self._view_added_consignment_button, "The view added consignment button on confirmation page after adding consignment couldn't be clicked or wasn't visible")
        return ConsignmentPage(self.get_driver())


    def get_consignment_title_from_result_page(self):
        self.consignment_title_result_page = self.get_text(self._consignment_title_result_page)

    def get_consignment_title_from_result_page_after_payment(self):
        self.consignment_title_result_page_after_payment = self.get_text(self._consignment_title_result_page_after_payment)

    def ask_for_offer_while_adding_consignment(self):
        self.click(self._first_offer, "The first offer button on ask for offer while adding consignment page couldn't be clicked or wasn't visible")

    def add_consignment_parcel(self):
        self.click(self._category_dropdown, "The category dropdown on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.get_driver().execute_script("return arguments[0].scrollIntoView();", self.find_element(self._category_parcels))
        self.click(self._category_parcels, "The category <Parcels> on category dropdown on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(self._title_uuid, self._consignment_title_field, "The attempt to send random consignment title to consignment title field on add consignment page was unsuccessful")
        self.if_not_visible_click(self._send_date_field, self._date_fixed_checkbox)
        # self.condition_click(self._date_fixed_checkbox, "The date fixed checkbox on add consignment page couldn't be clicked or wasn't visible")
        sleep(1)
        self.get_driver().execute_script("document.getElementsByName('EditAuction[sendDate]')[0].removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._send_date_value, self._send_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.get_driver().execute_script("document.getElementById('EditAuction_receiveDate').removeAttribute('readonly',0);")
        # self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field)
        # self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.click(self._send_date_field, "The click on send date field on add consignement page was unsuccessful")
        self.click(self._send_date_from_next_month_button, "The click on send date <from> cell on datepicker on add consignement page was unsuccessful")
        self.click(self._send_date_to_next_month_button, "The click on send date <to> cell on datepicker on add consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._send_date_from_value, self._send_date_from_field)
        # self.clear_field_and_send_keys(self._send_date_to_value, self._send_date_to_field)
        self.click(self._receive_date_field, "The click on receive date field on add consignement page was unsuccessful")
        self.click(self._receive_date_from_next_month_button, "The click on receive date <from> cell on datepicker on add consignement page was unsuccessful")
        self.click(self._receive_date_to_next_month_button, "The click on receive date <to> cell on datepicker on add consignement page was unsuccessful")
        # self.clear_field_and_send_keys(self._receive_date_from_value, self._receive_date_from_field)
        # self.clear_field_and_send_keys(self._receive_date_to_value, self._receive_date_to_field)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Radom, Polska", self._send_city_field, "The attempt to enter <Warszawa> into send city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._receive_city_field, "The receive city field on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys(u"Poznań, Polska", self._receive_city_field, "The attempt to enter <Poznań> into receive city field on add consignment page was unsuccessful")
        sleep(2)
        self.click(self._consignment_title_field, "The consignment title field on add consignment page couldn't be clicked or wasn't visible")
        # if str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._send_date_value_next_month, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._send_date_value, self._send_date_field, "The attempt to send date to send date field on add consignment page was unsuccessful")
        # if str(datetime.date.today().day) == 29:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 30:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().day) == 31:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # elif str(datetime.date.today().month) == 2 and str(datetime.date.today().day) == 28:
        #     self.clear_field_and_send_keys(self._receive_date_value_next_month, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        # else:
        #     self.clear_field_and_send_keys(self._receive_date_value, self._receive_date_field, "The attempt to send date to receive date field on add consignment page was unsuccessful")
        self.if_not_visible_click(self._consignment_length, self._additional_info_button)
        # self.condition_click(self._additional_info_button, "The additional info button on add consignment page couldn't be clicked or wasn't visible")
        self.clear_field_and_send_keys("5", self._consignment_length, "The attempt to enter <5> to consignment length field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._consignment_width, "The attempt to enter <3> to consignment width field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("8", self._consignment_height, "The attempt to enter <8> to consignment height field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("12", self._consignment_weight, "The attempt to enter <12> to consignment weight field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("3", self._quantity, "The attempt to enter <3> to consignment quantity field on add consignment page was unsuccessful")
        # self.click(self._type_of_service_dropdown, "The type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        # self.click(self._type_of_service_complex_service_option, "The complex service option in type of service dropdown on add consignment page couldn't be clicked or wasn't visible")
        # self.clear_field_and_send_keys("200", self._budget, "The attempt to enter <200> to consignment budget field on add consignment page was unsuccessful")
        self.clear_field_and_send_keys("This is my additional info", self._additional_info, "The attempt to enter <This is my additional info> to consignment additional info field on add consignment page was unsuccessful")
        self.click(self._submit_consignment_button, "The submit consignment button on add consignment page couldn't be clicked or wasn't visible")

    def set_highlited(self):
        self.check(self._highlited_checkbox)
        self.click(self._receive_city)

    def set_urgent(self):
        self.click(self._urgent_checkbox)
        self.click(self._receive_city)

    def pay_with_test_payment(self):
        self.click(self._test_payment_radio)
        self.select_index_from_dropdown(get_random_integer(2), self._invoice_company_country)
        self.click(self._submit_payment_button)
        sleep(2)
        self.click(self._payu_accept_button)
        # self.click(self._payu_valid_authorization)

    def get_first_payment_date(self):
        return self.get_text(self._first_payment_date_field)
