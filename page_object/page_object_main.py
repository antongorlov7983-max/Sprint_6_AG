import allure
from page_object.page_object_base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    upper_order_button = (By.XPATH, '//div[contains(@class,"Nav")]/button[contains(@class,"Button")]') # Кнопка "Заказать" в заголовке страницы
    lower_order_button = (By.XPATH, '//button[contains(@class,"Button_Button") and contains(text(),"Заказать")]') # Кнопка "Заказать" внизу страницы
    logo_scooter = (By.XPATH, '//a[contains(@class,"LogoScooter")]') # Логотип самокат
    logo_yandex = (By.CSS_SELECTOR,'[class*="Header_LogoYandex"]') # Логотип яндекса
    button_cookies = (By.ID,'rcc-confirm-button') # Кнопка закрытия банера куки

    @allure.step('Закрытие банера куки')
    def close_button_cookies(self):
        self.close_if_exists(self.button_cookies)

    @allure.step('Кликаем на верхнюю кнопку "Заказать"')
    def click_upper_order_button(self):
        self.wait_visible(self.upper_order_button).click()

    @allure.step('Кликаем на нижнюю кнопку "Заказать"')
    def click_lower_order_button(self):
        self.click_with_js(self.lower_order_button)
        
    @allure.step('Выбор кнопки "Заказать"')
    def choice_order_button(self, button):
        if button == 'нижнюю':
            self.click_lower_order_button()
        elif button == 'верхнюю':
            self.click_upper_order_button()
        else:
            raise Exception(f"Такой кнопки нет")
    
    @allure.step('кликаем на вопрос')
    def click_question_locator(self, index):
        self.click_with_js(self.get_question_locator(index))
    
    @allure.step('Клик по логотипу "Самокат"')
    def click_logo_scooter(self):
        self.wait_visible(self.logo_scooter).click()

    @allure.step('Кликаем по логотипу яндекс')
    def click_logo_yandex(self):
        self.wait_visible(self.logo_yandex).click()

    @allure.step("получаем текст ответа из страницы")
    def text_answer(self, index):
        return self.wait_visible(self.get_answer_locator(index)).text
    
    @allure.step("получаем локатор на вопрос")
    def get_question_locator(self, index):
        return (By.ID, f'accordion__heading-{index}')

    @allure.step("получаем локатор на ответ")
    def get_answer_locator(self, index):
        return (By.ID, f'accordion__panel-{index}')
    
    @allure.step("Переходим в новом окно")
    def open_page_dzen(self, expected_url):
        main_handle = self.driver.current_window_handle
        self.click_logo_yandex()
        self.switch_to_new_window(main_handle)
        self.wait_url_contains(expected_url)