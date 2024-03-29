# coding=utf-8
import unittest
from htmltestrunner import HTMLTestRunner
from selenium import webdriver
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
import os
from datetime import datetime
from time import sleep
from time import gmtime, strftime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from change_password import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)

run_locally = True
#@on_platforms(browsers)

class SmokeTest(unittest.TestCase):

    def test_add_new_consignment_not_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_unlogged_text_field, u"Jeszcze tylko chwila..."), u"The text <Jeszcze tylko chwila...> didn't appear on page after adding consignment unlogged")
        # Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source(), u"The text <Jeszcze tylko chwila> didn't appear on confirmation page after entering congigment details consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników.", add_consignment_page.get_page_source(), u"The text <Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.", add_consignment_page.get_page_source(), u"The text <Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        home_page.header.login_after_adding_consignment(USER, PASSWORD)

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")

    def test_add_new_consignment_not_activated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        registeration_page = home_page.header.continue_to_registration_page()
        registeration_page.add_new_consignment_unactivated_fill_username_field()
        registeration_page.add_new_consignment_unactivated_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), u"The text <Odbierz pocztę> wasn't found on confirmastion page after entering new user data")
        Assert.contains(registeration_page._email_user_add_new_consignment, registeration_page.get_page_source(), u"The user email wasn't found on confirmastion page after entering new user data")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), u"The text <i kliknij link aktywacyjny, aby ukończyć rejestrację> wasn't found on confirmastion page after entering new user data")

    def test_add_new_consignment_not_logged_in_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_unlogged_text_field, u"Jeszcze tylko chwila..."), u"The text <Jeszcze tylko chwila...> didn't appear on page after adding consignment unlogged")
        # Assert.contains(u"Jeszcze tylko chwila...", add_consignment_page.get_page_source(), u"The text <Jeszcze tylko chwila> didn't appear on confirmation page after entering congigment details consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników.", add_consignment_page.get_page_source(), u"The text <Twoje ogłoszenie o przesyłce  zostało zapisane, ale musisz się zalogować, aby było widoczne dla Przewoźników> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        Assert.contains(u"Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione.", add_consignment_page.get_page_source(), u"The text <Nie masz konta? <b>Zarejestruj si\u0119 w 1 minut\u0119 (za darmo).</b> Twoje dane s\u0105 chronione i nie b\u0119d\u0105 upublicznione> didn't appear on confirmation page after adding consignment, probably the consignment details were wrongly entered")
        home_page.header.login_after_adding_consignment(PROVIDER_USER, PROVIDER_PASSWORD)

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")

    def test_add_new_consignment_logged_in_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        # add_consignment_page.get_consignment_title_from_result_page()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        if u"Nie chcesz czekać? Podaj swoją cenę, a my szybko znajdziemy" in add_consignment_page.get_page_source():
            pass
        elif u"Nie chcesz czekać? Wyróżnij swoją przesyłkę, aby" in add_consignment_page.get_page_source():
            pass
        elif u"Nie chcesz czekać? Poproś najbardziej dopasowanych" in add_consignment_page.get_page_source():
            pass
        else:
            raise NoSuchElementException(u"The one of 3 random shown messages after adding consignement didn't appear")
        # Assert.contains(u"została wystawiona!", add_consignment_page.get_page_source(), u"The text <została wystawiona!> didn't appear on confirmation page after adding consignment")
        # Assert.equal(add_consignment_page.consignment_title_result_page, add_consignment_page._title_uuid, u"The consignment title didn't appear on confirmation page after adding consignment")

    def test_new_consignment_should_appear_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()

        Assert.contains(add_consignment_page._title_uuid, view_consignments_page.get_page_source(), u"THe consignment title didn't appear on added consignment page")
        Assert.contains(u"Wrocław, Polska", view_consignments_page.get_page_source(), u"The text <Wrocław, Polska> didn't appear on added consignment page")
        Assert.contains(u'Radom', view_consignments_page.get_page_source(), u"The text <Warszawa, Polska> didn't appear on added consignment page")
        Assert.contains(u'357.00  km', view_consignments_page.get_page_source(), u"The text <357.00  km> didn't appear on added consignment page, probably the distance between cities has changed")
        Assert.contains(u'Kompleksowa usługa: transport, załadunek i rozładunek', view_consignments_page.get_page_source(), u"The text <Kompleksowa usługa: transport, załadunek i rozładunek> didn't appear on added consignment page")
        Assert.contains(u'This is my additional info', view_consignments_page.get_page_source(), u"The text <This is my additional info> didn't appear on added consignment page")
        Assert.contains(add_consignment_page._send_date_from_value, view_consignments_page.get_text(consignment._consignement_send_date_from_field), u"The set in add consignement send date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(add_consignment_page._send_date_to_value, view_consignments_page.get_text(consignment._consignement_send_date_to_field), u"The set in add consignement send date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(add_consignment_page._receive_date_from_value, view_consignments_page.get_text(consignment._consignement_receive_date_from_field), u"The set in add consignement receive date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(add_consignment_page._receive_date_to_value, view_consignments_page.get_text(consignment._consignement_receive_date_to_field), u"The set in add consignement receive date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(add_consignment_page._consignment_length_value, view_consignments_page.get_text(consignment._consignement_length_field), u"The set in add consignement length value didn't appear on consignement page in suitable place")
        Assert.contains(add_consignment_page._consignment_width_value, view_consignments_page.get_text(consignment._consignement_width_field), u"The set in add consignement width value didn't appear on consignement page in suitable place")
        Assert.contains(add_consignment_page._consignment_height_value, view_consignments_page.get_text(consignment._consignement_height_field), u"The set in add consignement height value didn't appear on consignement page in suitable place")
        Assert.contains(add_consignment_page._consignment_weight_value, view_consignments_page.get_text(consignment._consignement_weight_field), u"The set in add consignement weight value didn't appear on consignement page in suitable place")
        Assert.contains(add_consignment_page._quantity_value, view_consignments_page.get_text(consignment._consignement_items_number_field), u"The set in add consignement items number value didn't appear on consignement page in suitable place")

    def test_change_consignement_to_quick_commision_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.change_to_quick_commision()

        Assert.contains(u"Gratulacje! Twoja przesyłka została zmieniona na Szybkie Zlecenie. Wkrótce powinien zgłosić się Przewoźnik do Twojego zlecenia i poinformujemy Cię o tym mailem. Tylko najlepsi z naszych Przewoźników będą mogli wykonać Twoje zlecenie.", consignment.get_page_source(), u"the confirmation info obout successful change to quick commision on consignement page didn't show")

        Assert.contains(consignment._quick_commision_change_price_value, consignment.get_text(consignment._added_quick_commision_price_field), u"The set quick commision price didn't appear on consignement page in added quick commision box")
        Assert.contains(consignment._quick_commision_change_send_date_from_value, consignment.get_text(consignment._added_quick_commision_send_date_from_field), u"The set quick commision send date <from> didn't appear on consignement page in added quick commision box")
        Assert.contains(consignment._quick_commision_change_send_date_to_value, consignment.get_text(consignment._added_quick_commision_send_date_to_field), u"The set quick commision send date <to> didn't appear on consignement page in added quick commision box")
        Assert.contains(consignment._quick_commision_change_receive_date_from_value, consignment.get_text(consignment._added_quick_commision_receive_date_from_field), u"The set quick commision receive date <from> didn't appear on consignement page in added quick commision box")
        Assert.contains(consignment._quick_commision_change_receive_date_to_value, consignment.get_text(consignment._added_quick_commision_receive_date_to_field), u"The set quick commision receive date <to> didn't appear on consignement page in added quick commision box")
        Assert.contains(consignment._quick_commision_change_send_date_from_value, consignment.get_text(consignment._consignement_send_date_from_field), u"The set quick commision send date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(consignment._quick_commision_change_send_date_to_value, consignment.get_text(consignment._consignement_send_date_to_field), u"The set quick commision send date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(consignment._quick_commision_change_receive_date_from_value, consignment.get_text(consignment._consignement_receive_date_from_field), u"The set quick commision receive date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(consignment._quick_commision_change_receive_date_to_value, consignment.get_text(consignment._consignement_receive_date_to_field), u"The set quick commision receive date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(consignment._quick_commision_change_lenght_value, consignment.get_text(consignment._consignement_length_field), u"The set quick commision length value didn't appear on consignement page in suitable place")
        Assert.contains(consignment._quick_commision_change_width_value, consignment.get_text(consignment._consignement_width_field), u"The set quick commision width value didn't appear on consignement page in suitable place")
        Assert.contains(consignment._quick_commision_change_height_value, consignment.get_text(consignment._consignement_height_field), u"The set quick commision height value didn't appear on consignement page in suitable place")
        Assert.contains(consignment._quick_commision_change_weight_value, consignment.get_text(consignment._consignement_weight_field), u"The set quick commision weight value didn't appear on consignement page in suitable place")
        Assert.contains(consignment._quick_commision_change_items_number_value, consignment.get_text(consignment._consignement_items_number_field), u"The set quick commision items number value didn't appear on consignement page in suitable place")

    def test_register_user_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.register_user_fill_username_field()
        registeration_page.register_user_fill_email_field()
        registeration_page.new_user_fill_data()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), u"The text <Odbierz pocztę> didn't appear on confirmation page after registering user, probably the registration didn't work")
        Assert.contains(registeration_page._email_user_register, registeration_page.get_page_source(), u"The registered user email didn't appear on confirmation page after registering user")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), u"The text <i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on confirmation page after registering user")

    def test_login_unactivated_user_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_user_click_register()
        registeration_page.login_unactivated_user_fill_username_field()
        registeration_page.login_unactivated_user_fill_email_field()
        registeration_page.new_user_fill_data()
        account_page = home_page.header.login(registeration_page._username_user_login_unactivated, registeration_page._password)

        Assert.contains(u"Twoja rejestracja nie została ukończona", registeration_page.get_page_source(), u"The text <Twoja rejestracja nie została ukończona> didn't appear on page after logging unactivated user")
        Assert.contains(u"Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.", registeration_page.get_page_source(), u"The text <Odbierz pocztę i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on page after logging unactivated user")

    def test_logout_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        home_page.header.login(USER, PASSWORD)
        home_page.header.logout()
        sleep(3)
        Assert.contains(u"Prześlesz wszystko i wszędzie!", home_page.get_page_source(), u"The text <Prześlesz wszystko i wszędzie!> didn't appear on home page")
        Assert.contains(u"Masz pytania? Kontakt:", home_page.get_page_source(), u"The text <Masz pytania? Kontakt:> didn't appear on home page")

    def test_register_new_transport_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        registeration_page = home_page.header.open_registration_page()
        registeration_page.new_transport_provider()

        Assert.contains(u"Odbierz pocztę", registeration_page.get_page_source(), u"The text <Odbierz pocztę> didn't appear on confirmation page after registering provider, probably the registration didn't work")
        Assert.contains(registeration_page._email, registeration_page.get_page_source(), u"The registered provider email didn't appear on confirmation page after registering provider")
        Assert.contains(u'i kliknij link aktywacyjny, aby ukończyć rejestrację.', registeration_page.get_page_source(), u"The text <i kliknij link aktywacyjny, aby ukończyć rejestrację.> didn't appear on confirmation page after registering provider")

    def test_edit_user_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_user_profile()

        Assert.contains(u"Twoje dane zostały zaktualizowane", profile_page.get_page_source(), u"The text <Twoje dane zostały zaktualizowane> didn't appear on confirmation page after editing user profile")
        Assert.contains(u"Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.", profile_page.get_page_source(), u"The text <Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.> didn't appear on confirmation page after editing user profile")

    def test_edit_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.edit_consignment()
        consignment = settings.edit_consignment_cars()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(settings._edit_consignment_result_field, u"Zmiany zostały pomyślnie zapisane!"), u"The text <Zmiany zostały pomyślnie zapisane! > didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        # Assert.contains(u"Zmiany w Twojej przesyłce", settings.get_page_source(), u"The text <Zmiany w Twojej przesyłce> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        # Assert.contains(settings._title_uuid, profile_page.get_page_source(), u"The edited consignment title didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        # Assert.contains(u"zostały pomyślnie zapisane.", settings.get_page_source(), u"The text <zostały pomyślnie zapisane.> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        #
        # settings.view_added_consignment()

        Assert.contains(settings._title_uuid, settings.get_page_source(), u"The edited consignment title didn't appear on consignment page after editing consignment")
        Assert.contains(u"Katowice, Polska", settings.get_page_source(), u"The text <Katowice, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'Poznań, Polska', settings.get_page_source(), u"The text <Poznań, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'409.00  km', settings.get_page_source(), u"The text <409.00  km> didn't appear on consignment page after editing consignment, probably the distance between cities has changed")
        Assert.contains(u'This is my additional info after edit', settings.get_page_source(), u"The text <This is my additional info after edit> didn't appear on consignment page after editing consignment")
        Assert.contains(settings._send_date_from_older_value, consignment.get_text(consignment._consignement_send_date_from_field), u"The set in edit consignement send date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(settings._send_date_to_older_value, consignment.get_text(consignment._consignement_send_date_to_field), u"The set in edit consignement send date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(settings._receive_date_from_older_value, consignment.get_text(consignment._consignement_receive_date_from_field), u"The set in edit consignement receive date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(settings._receive_date_to_older_value, consignment.get_text(consignment._consignement_receive_date_to_field), u"The set in edit consignement receive date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(settings._consignment_cars_brand_value, consignment.get_text(consignment._consignement_car_brand_field), u"The set in edit consignement car brand value didn't appear on consignement page in suitable place")
        Assert.contains(settings._consignment_weight_value, consignment.get_text(consignment._consignement_car_weight_field), u"The set in edit consignement weight value didn't appear on consignement page in suitable place")

    def test_withdraw_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        sleep(3)

        Assert.contains(u"Ogłoszenie zostało wycofane", profile_page.get_page_source(), u"The text <Ogłoszenie zostało wycofane> didn't appear on profile page after withdrawing consignment")


    def test_report_violation_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        consignment = add_consignment_page.view_added_consignment()
        consignment.report_violation_to_consignmeent()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), u"The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation")


    def test_report_violation_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        account_page = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.report_violation_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), u"The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to offer")

    def test_report_violation_to_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.report_violation_to_question_to_offer()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), u"The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to question to offer")

    def test_report_violation_to_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        consignment.report_violation_to_question_to_consignment()

        Assert.contains(u"Zgłoszenie zostało odnotowane", consignment.get_page_source(), u"The text <Zgłoszenie zostało odnotowane> didn't appear on consignment page after reporting violation to question to consignment")

# no possibility to add question to consignment

    def test_check_categories_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.add_consignment_parcel()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        view_consignment_page = home_page.header.view_consignments_page()
        view_consignment_page.check_categories()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(view_consignment_page._first_result_posting_province, "azowieckie"), u"The first result on view consignments page posting province didn't match posting province entered into search field")
        view_consignment_page.click_first_result()
        Assert.contains('Paczki', view_consignment_page.get_page_source(), u"The text <Paczki> didn't appear on consignment page, probably the category on view consignments page wasn't chosen")

    def test_submit_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()

        Assert.contains(u"Oferta została złożona", submit_offer.get_page_source(), u"The text <Oferta została złożona> didn't appear on consignment page after submitting offer, probably offer wasn't submitted")

    def test_withdraw_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        profile = home_page.header.open_profile_page()
        profile.withdraw_offer()

        Assert.contains(u"Oferta może zostać wycofana najwcześniej 3 godziny od jej złożenia.", profile.get_page_source(), u"The text <Oferta może zostać wycofana najwcześniej 3 godziny od jej złożenia.> didn't appear on consignment page after trying to withdraw offer")

    def test_issue_consignment_again_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        profile_page = home_page.header.open_profile_page()
        settings = profile_page.withdraw_consignment()
        profile = home_page.header.open_profile_page()
        edit_settings = profile.issue_consignment_again()
        consignment = edit_settings.edit_consignment_parcel()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        # Assert.contains(u"Zmiany w Twojej przesyłce", settings.get_page_source(), u"The text <Zmiany w Twojej przesyłce> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        # Assert.contains(settings._title_uuid, profile_page.get_page_source(), u"The edited consignment title didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        # Assert.contains(u"zostały pomyślnie zapisane.", settings.get_page_source(), u"The text <zostały pomyślnie zapisane.> didn't appear on confirmation page after editing consignment, probably the edit didn't work well")
        #
        add_consignment_page.view_added_consignment()

        Assert.contains(edit_settings._title_uuid, edit_settings.get_page_source(), u"The edited consignment title didn't appear on consignment page after editing consignment")
        Assert.contains(u"Katowice, Polska", edit_settings.get_page_source(), u"The text <Katowice, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'Poznań, Polska', edit_settings.get_page_source(), u"The text <Poznań, Polska> didn't appear on consignment page after editing consignment")
        Assert.contains(u'409.00  km', edit_settings.get_page_source(), u"The text <409.00  km> didn't appear on consignment page after editing consignment, probably the distance between cities has changed")
        Assert.contains(u'This is my additional info after edit', edit_settings.get_page_source(), u"The text <This is my additional info after edit> didn't appear on consignment page after editing consignment")
        Assert.contains(edit_settings._send_date_from_edit_value, edit_settings.get_text(consignment._consignement_send_date_from_field), u"The set in edit consignement send date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(edit_settings._send_date_to_edit_value, edit_settings.get_text(consignment._consignement_send_date_to_field), u"The set in edit consignement send date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(edit_settings._receive_date_from_edit_value, edit_settings.get_text(consignment._consignement_receive_date_from_field), u"The set in edit consignement receive date <from> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(edit_settings._receive_date_to_edit_value, edit_settings.get_text(consignment._consignement_receive_date_to_field), u"The set in edit consignement receive date <to> didn't appear on consignement page in consignement send-receive dates field")
        Assert.contains(edit_settings._consignment_length_value, edit_settings.get_text(consignment._consignement_length_field), u"The set in edit consignement length value didn't appear on consignement page in suitable place")
        Assert.contains(edit_settings._consignment_width_value, edit_settings.get_text(consignment._consignement_width_field), u"The set in edit consignement width value didn't appear on consignement page in suitable place")
        Assert.contains(edit_settings._consignment_height_value, edit_settings.get_text(consignment._consignement_height_field), u"The set in edit consignement height value didn't appear on consignement page in suitable place")
        Assert.contains(edit_settings._consignment_weight_value, edit_settings.get_text(consignment._consignement_weight_field), u"The set in edit consignement weight value didn't appear on consignement page in suitable place")
        Assert.contains(edit_settings._quantity_value, edit_settings.get_text(consignment._consignement_items_number_field), u"The set in edit consignement items number value didn't appear on consignement page in suitable place")


    def test_watch_auction_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.watch_consignment()

        sleep(2)
        Assert.contains(u"Ogłoszenie obserwowane", consignment.get_page_source(), u"The text <Ogłoszenie obserwowane> didn't appear on consignment page after watching consignment")

    def test_commission_payback_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.payback_commission()

        Assert.contains(u"Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.", profile.get_page_source(), u"The text <Wniosek został wysłany do rozpatrzenia. O wyniku zostaniesz poinformowany mailem.> didn't appear on profile page after making payback commission")

    def test_edit_provider_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_profile()
        sleep(2)

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_from_value, profile_page.get_value(profile_page._route_from_field), u"The edited route <From> value didn't appear on profile page after editing provider profile")
        Assert.equal(profile_page._route_to_value, profile_page.get_value(profile_page._route_to_field), u"The edited route <To> value didn't appear on profile page after editing provider profile")


    def test_edit_provider_data_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER2, PROVIDER_PASSWORD2)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_data()

        Assert.contains(u"Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail.", profile_page.get_page_source(), u"The text <Sprawdź pocztę. Na Twój nowy adres e-mail wysłaliśmy wiadomość z instrukcją jak ukończyć zmianę adresu e-mail> didn't appear on profile page after editing provider data")
        Assert.contains(u"Twoje dane zostały zaktualizowane", profile_page.get_page_source(), u"The text <Twoje dane zostały zaktualizowane> didn't appear on profile page after editing provider data")

    def test_edit_provider_company_data_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_company_data()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider company data")
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile_page._changes_saved_field, u"Zmiany zostały zapisane."), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider company data")
        Assert.contains(u"Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem.", profile_page.get_page_source(), u"The text <Dane na Twoim koncie oczekują na sprawdzenie przez pracownika Clicktrans.pl. Do weryfikacji danych może być potrzebne nadesłanie dokumentów potwierdzających. Powiadomimy Cię o tym e-mailem> disn't appear on profile page after editing provider company data")

    def test_edit_provider_notifications_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        account_page = home_page.header.login(PROVIDER_USER2, PROVIDER_PASSWORD2)
        profile_page = home_page.header.open_profile_page()
        profile_page.edit_provider_notifications()

        Assert.contains(u"Zmiany zostały zapisane.", profile_page.get_page_source(), u"The text <Zmiany zostały zapisane.> didn't appear on profile page after editing provider notifications")

    def test_reject_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.reject_offer()
        sleep(3)

        Assert.contains(u"Oferta została odrzucona.", consignment.get_page_source(), u"The text <Oferta została odrzucona.> didn't appear on consignment page after rejecting offer")

    def test_add_question_to_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        consignment.show_offer_details()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source(), u"The text <Twoja wiadomość została dodana.> didn't appear on consignment page after adding question to offer")
        Assert.contains(u"This is my question", consignment.get_page_source(), u"The text <This is my question> didn't appear on consignment page after adding question to offer")

    def test_provider_reply_to_question_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.add_question_to_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_message()
        consignment.reply_to_question()
        consignment.show_offer_details()

        Assert.contains(u"Twoja wiadomość została dodana.", consignment.get_page_source(), u"The text <Twoja wiadomość została dodana.> didn't appear on consignment page after replying to question to offer")
        Assert.contains(u"This is my answer", consignment.get_page_source(), u"The text <This is my answer> didn't appear on consignment page after replying to question to offer")

    def test_provider_add_question_to_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()

        Assert.contains(u"Twoje pytanie zostało dodane.", consignment.get_page_source(), u"The text <Twoje pytanie zostało dodane.> didn't appear on consignment page after adding question to consignment")
        Assert.contains(u"This is my question", consignment.get_page_source(), u"The text <This is my question> didn't appear on consignment page after adding question to consignment")

#brak mozliwosci dodania pytania do przesyłki

    def test_user_reply_to_question_to_consignment_from_provider_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.user_open_first_message()
        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", consignment.get_page_source(), u"The text <Twoja odpowiedź została dodana.> didn't appear on consignment page after replying to question to consignment")
        Assert.contains(u"This is my reply", consignment.get_page_source(), u"The text <This is my reply> didn't appear on consignment page after replying to question to consignment")

#brak mozliwosci dodania pytania do przesyłki

    def test_accept_offer_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        store = home_page.header.open_profile_page()
        store.store_provider_data()
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        sleep(3)

        Assert.contains("Gratulacje", consignment.get_page_source(), u"The text <Gratulacje> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Wybrałeś ofertę Przewoźnika <strong>"+PROVIDER_USER, consignment.get_page_source(), u"The text <Wybrałeś ofertę Przewoźnika <b>PROVIDER_USER_NAME> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Skontaktuj się z nim w celu finalizacji usługi.", consignment.get_page_source(), u"The text <Skontaktuj się z nim w celu finalizacji usługi.> didn't appear on consignment page after accepting offer")
        Assert.contains(store.name1, consignment.get_page_source(), u"The text <STORED_NAME_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.tel, consignment.get_page_source(), u"The text <STORED_PHONE_FORM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.mail, consignment.get_page_source(), u"The text <STORED_EMAIL_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        Assert.contains(store.www, consignment.get_page_source(), u"The text <STORED_WWW_FROM_PROFILE> didn't appear on consignment page after accepting offer")
        # Assert.contains(store.address_table_0_splitted[0]+" "+store.address_table_0_splitted[1], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_!> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[0], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_!> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[1], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_2> didn't appear on consignment page after accepting offer")
        Assert.contains(store.address_table[2], consignment.get_page_source(), u"The text <STORED_PROVIDER_ADDRESS_LINE_3> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Dane kontaktowe Przewoźnika zostały również wysłane na Twoją skrzynkę e-mail. Znajdziesz je także w dowolnym momencie w zakładce <strong>Moje Konto</strong>.", consignment.get_page_source(), u"The text <Dane kontaktowe Przewoźnika zostały również wysłane na Twoją skrzynkę e-mail. Znajdziesz je także w dowolnym momencie w zakładce <strong>Moje Konto</strong>.> didn't appear on consignment page after accepting offer")
        Assert.contains(u"Pobierz list przewozowy", consignment.get_page_source(), u"The text <Pobierz list przewozowy> didn't appear on consignment page after accepting offer")

#  PROVIDER ADDRESS TABLE[0] IS SHOWN WITH 2 SPACES, zgłoszone, ale poprawione splittem

    def test_make_offer_executed_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.make_offer_executed()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._executed_result_field, u"Oferta ma status zrealizowana"), u"The text <Oferta ma status zrealizowana> didn't match the text in Offer executed result field in provider profile after making offer executed")

    def test_provider_send_commentary_from_my_offers_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_my_offers_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary form my offers menu")


    def test_reply_to_question_to_consignment_from_panel_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        consignment = view_consignments_page.open_added_consignment()
        consignment.provider_add_question_to_consignment()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.user_click_reply_to_question()

        Assert.contains(u"Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika.", profile.get_page_source(), u"The text <Napisz wiadomość i ustal z Przewoźnikiem niezbędne szczegóły. Aby transakcja była bezpieczna musisz jeszcze zaakceptować ofertę Przewoźnika> didn't appear on user profile page ofter clicking <reply to question>")

        consignment.reply_to_provider_question_to_consignment()

        Assert.contains(u"Twoja odpowiedź została dodana.", profile.get_page_source(), u"The text <Twoja odpowiedź została dodana> didn't appear on consignment page after replying to provider question to consignment")
        Assert.contains(u"This is my reply", profile.get_page_source(), u"The text <This is my reply> didn't appear on consignment page after replying to provider question to consignment")

    def test_user_send_commentary_from_ended_transactions_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_ended_transactions_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from ended transactions menu")


    def test_user_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        profile = home_page.header.open_profile_page()
        profile.user_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on user profile page after sending commentary from commentaries menu")


    # def test_provider_reply_to_negative_commentary_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     view_consignments_page = home_page.header.view_consignments_page()
    #     view_consignments_page.search_for_added_consignment()
    #     WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
    #     submit_offer = view_consignments_page.open_added_consignment()
    #     submit_offer.submit_offer()
    #     submit_offer.confirm_submit_offer()
    #     home_page.header.logout()
    #     user = home_page.header.login(USER, PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     consignment = profile.open_first_auction()
    #     consignment.accept_offer()
    #     profile = home_page.header.open_profile_page()
    #     profile.user_send_negative_commentary()
    #     home_page.header.logout()
    #     provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
    #     profile = home_page.header.open_profile_page()
    #     profile.provider_reply_to_negative_commentary()
    #
    #     Assert.contains(u"This is my negative commentary", profile.get_page_source(), u"The text <This is my negative commentary> didn't appear on provider profile page after replying to negative commentary")
    #     Assert.contains(u"This is my reply", profile.get_page_source(), u"The text <This is my reply> didn't appear on provider profile page after replying to negative commentary")

# There's no possibility to reply to negative commentary as provider, zgłoszone
#chrome



    def test_provider_send_commentary_from_commentaries_menu_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        view_consignments_page = home_page.header.view_consignments_page()
        view_consignments_page.search_for_added_consignment()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(view_consignments_page._first_result, view_consignments_page._title_uuid), u"The first consignment on view consignments page didn't match consignment title entered into search field, probably the search function didn't work properly")
        submit_offer = view_consignments_page.open_added_consignment()
        submit_offer.submit_offer()
        submit_offer.confirm_submit_offer()
        home_page.header.logout()
        user = home_page.header.login(USER, PASSWORD)
        profile = home_page.header.open_profile_page()
        consignment = profile.open_first_auction()
        consignment.accept_offer()
        home_page.header.logout()
        provider = home_page.header.login(PROVIDER_USER, PROVIDER_PASSWORD)
        profile = home_page.header.open_profile_page()
        profile.provider_send_commentary_from_commentaries_menu()

        Assert.contains(u"Komentarz został wystawiony.", consignment.get_page_source(), u"The text <Komentarz został wystawiony.> didn't appear on provider profile page after sending commentary from commentaries menu")

        profile.enter_provider_sent_commentaries_tab()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_field, "This is my commentary"), u"The text in provider first sent commentary field in provider sent commentaries tab didn't match text <This is my commentary>")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(profile._provider_first_sent_commentary_consignment_uuid, view_consignments_page._title_uuid), u"The text in provider first sent commentary consignment title field in provider sent commentaries tab didn't match <CONSIGNMENT_TITLE>")


    def test_ask_for_offer_on_provider_page_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        provider_page = home_page.header.view_provider_damian_wiklina_page()
        provider_page.ask_for_offer_on_provider_page()

        Assert.contains(u"Twoja prośba o ofertę została wysłana do Przewoźnika", provider_page.get_page_source(), u"THe text <Twoja prośba o ofertę została wysłana do Przewoźnika> didn't appear on provider <damian wilkina> page after asking for offer on this page")

    # def test_ask_for_offer_while_adding_consignment_should_succeed(self):
    #     home_page = HomePage(self.driver).open_page_testowe()
    #     user = home_page.header.login(USER, PASSWORD)
    #     add_consignment_page = home_page.header.add_consignment_page()
    #     add_consignment_page.new_furniture_consignment()
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
    #     add_consignment_page.ask_for_offer_while_adding_consignment()
    #     sleep(2)
    #
    #     Assert.contains(u"Prośba wysłana", add_consignment_page.get_page_source(), u"The text <Prośba wysłana> didn't appear on add consignment page after asking for offer while adding consignment")

#TERAZ NIE POJAWIA SIE ZAWSZE MOZLIWOSC ZAPYTANIA O OFERTY

    def test_ask_for_offer_for_added_consignment_should_succeed(self):
        home_page = HomePage(self.driver).open_page_testowe()
        user = home_page.header.login(USER, PASSWORD)
        add_consignment_page = home_page.header.add_consignment_page()
        add_consignment_page.new_furniture_consignment()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(add_consignment_page._after_adding_consignment_text_field, u"Gratulacje, Twoja przesyłka już czeka na oferty!"), u"The text <Gratulacje, Twoja przesyłka już czeka na oferty!> didn't appear on page after adding consignment, probably the consignment wasn't added")
        profile = home_page.header.open_profile_page()
        profile.ask_for_offer_for_added_consignment()
        sleep(4)
        Assert.contains(u"Prośba wysłana", profile.get_page_source(), u"The text <Prośba wysłana> didn't appear on user profile page after asking for offer for added consignment")

    def test_change_password_should_succeed(self):

        home_page = HomePage(self.driver).open_page_testowe()
        _saved_password = get_password("change_pass_testowe1.txt")
        account_page = home_page.header.login(CHANGE_PASSWORD_USER, _saved_password)
        profile_page = home_page.header.open_profile_page()
        profile_page.change_password("change_pass_testowe1.txt")

        Assert.contains(u"Hasło zostało zmienione.", profile_page.get_page_source(), u"The text <Hasło zostało zmienione> didn't appear or profile page after changing password")

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        # self._convert_to_html()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            # fp = webdriver.FirefoxProfile()
            # fp.set_preference("browser.startup.homepage", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            # fp.set_preference(" xpinstall.signatures.required", "false")
            # fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            # binary = FirefoxBinary('/__stare/firefox45/firefox')
            # self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            sr_args = ["--verbose", "--log-path=chromedriver.log"]
            from selenium.webdriver.chrome.options import Options
            opts = Options()
            opts.binary_location = "/usr/bin/google-chrome"
            # opts.binary_location = "/usr/lib/chromium-browser/chromium-browser"
            opts.add_argument("--no-sandbox") #This make Chromium reachable
            opts.add_argument("--no-default-browser-check") #Overrides default choices
            opts.add_argument("--no-first-run")
            opts.add_argument("--disable-default-apps")
            self.driver = webdriver.Chrome(executable_path="/var/lib/jenkins/workspace/Testarmy/node_modules/chromedriver", service_args=sr_args, chrome_options=opts)
            # self.driver = webdriver.Chrome(service_args=sr_args, chrome_options=opts)
            self.driver.set_window_size(1024,768)
            # self.driver.implicitly_wait(self.timeout)
            self.errors_and_failures = self.tally()
        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
                if self.tally() > self.errors_and_failures:
                    if not os.path.exists(SCREEN_DUMP_LOCATION):
                        os.makedirs(SCREEN_DUMP_LOCATION)
                    for ix, handle in enumerate(self.driver.window_handles):
                        self._windowid = ix
                        self.driver.switch_to.window(handle)
                        self.take_screenshot()
                        self.dump_html()
                self.driver.quit()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def _get_filename_for_plot(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
            classname=self.__class__.__name__,
            timestamp=timestamp
        )
        return "{folder}/{classname}.plot-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            timestamp=timestamp
            )

    def _save_plot(self):
        import matplotlib.pyplot as plt
        filename = self._get_filename_for_plot() + ".png"
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, 61-fail-err]
        colors = ['red', 'gold', 'green']
        explode = (0.1, 0.1, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        print "\n WYKRES:\n", filename
        plt.savefig(filename)
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <img src=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename_plot+".png>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("Clicktrans3RaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Clicktrans3testowe/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["sergii.demianchuk@Clicktrans.pl", "2.michal.b@clicktrans.pl", "dariusz.grycz@clicktrans.pl", "sebastian.nieciecki@clicktrans.pl"])
        message.Subject = "Raport Clicktrans3 Testowe Testy Automatyczne Jenkins"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Clicktrans 3 Testowe<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny:  <a href="http://ci.testuj.pl/job/Clicktrans3testowe/ws/Clicktrans3testoweReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='maildoklientow@gmail.com', pwd='useme1988')
        sender.send(message)

open("Clicktrans3RaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("Clicktrans3testoweReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Clicktrans3 Testowe', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
     # unittest.main()
     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))