import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.page_object_main import MainPage
from page_object.page_object_form_order import OrderScooter
import test_data as TD


class TestScooterOrderUpper:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(TD.url_main_page)
        cls.main_page = MainPage(cls.driver)
        cls.order_scooter = OrderScooter(cls.driver)

    @allure.title("Проверка оформления заказа через верхнюю кнопку")
    @allure.step("1. Нажать на верхнюю кнопку\n2. Заполнить форму заказа\n3. Подтвердить заказ")
    def test_upper_button_order(self):
        self.main_page.click_order_button_cookies()
        self.main_page.click_upper_order_button()
        self.order_scooter.filling_form_user(**TD.order_1.get_order_user())
        self.order_scooter.click_button_next()
        self.order_scooter.filling_form_about_rent(**TD.order_1.get_order_about_rent())
        self.order_scooter.click_button_order()
        self.order_scooter.confirming_order()
        assert "Заказ оформлен" in self.order_scooter.get_text_title_order_placed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()