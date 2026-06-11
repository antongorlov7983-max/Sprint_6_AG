import allure
from selenium import webdriver
from page_object.page_object_main import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_data as TD


class TestClickLogo:

    driver = None
    @classmethod
    def setup_class(cls):
        # Создание драйвера для браузера Firefox
        cls.driver = webdriver.Firefox()
        # Переход на страницу Самокат
        cls.driver.get(TD.url_main_page)
        # Создаем объект класса MainPage
        cls.main_page = MainPage(cls.driver)

    # Тестирование перехода при клике на логотип Самокат
    @allure.title("Проверка отсутствия перехода при клике на логотип 'Скутор'")
    @allure.step("Кликнуть на логотип 'Самокат'")
    def test_click_logo_scooter(self):
        self.main_page.click_order_button_cookies()
        self.main_page.click_logo_scooter()
        assert TD.url_main_page == self.driver.current_url

    # Тестирование перехода при клике на логотип яндекс
    @allure.title("Проверка перехода на страницу Дзен при клике на логотип 'Яндекс'")
    @allure.step("Кликнуть на логотип 'Яндекс'")
    def test_click_logo_yandex(self):
        self.main_page.click_order_button_cookies()
        main_window = self.driver.current_window_handle
        self.main_page.click_logo_yandex()
        WebDriverWait(self.driver, 5).until(EC.number_of_windows_to_be(2))
        new_handle = [handle for handle in self.driver.window_handles if handle != main_window][0]
        self.driver.switch_to.window(new_handle)
        WebDriverWait(self.driver, 10).until(lambda d: "dzen.ru" in d.current_url)
        assert "dzen.ru" in self.driver.current_url  

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit() 