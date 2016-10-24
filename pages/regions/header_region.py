# coding=utf-8
from pages.add_consignment import AddConsignmentPage
from pages.page import Page
from pages.profile_page import ProfilePage
from pages.provider_page import ProviderPage
from pages.registration_page import RegistrationPage
from pages.view_consignments import ViewConsignmentsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages.home import HomePage



class HeaderRegion(Page):
    _login_field = (By.ID, "_username")
    _password_field = (By.ID, "_password")
    _login_button = (By.ID, "submit")
    # _base_url2 = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/"
    # _base_url = "http://clicktrans_dev:czx1mcc713d@dev.clicktrans.pl/app_dev.php/"
    _logout_button = (By.LINK_TEXT, u"Wyloguj się")
    _continue_to_registration_page_button = (By.LINK_TEXT, u'Zarejestruj się >>')
    _base_url = HomePage._url

    def login(self, login, password):
        self.get(self._base_url + "login")
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)

    def login_after_adding_consignment(self, login, password):
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)

    def logout(self):
        self.click(self._logout_button)
        sleep(2)

    def add_consignment_page(self):
        self.get(self._base_url + "zlec-transport-1")
        return AddConsignmentPage(self.get_driver())

    def view_consignments_page(self):
        self.get(self._base_url + "przegladaj-przesylki/")
        return ViewConsignmentsPage(self.get_driver())

    def open_registration_page(self):
        self.get(self._base_url + "register1")
        return RegistrationPage(self.get_driver())

    def open_profile_page(self):
        self.get(self._base_url + "my-account")
        return ProfilePage(self.get_driver())

    def view_provider_JLMTranspol_page(self):
        self.get(self._base_url + "firmy-transportowe/JLMTranspol.html")
        return ProviderPage(self.get_driver())

    def continue_to_registration_page(self):
        # self.click(self._continue_to_registration_page_button)
        return RegistrationPage(self.get_driver())