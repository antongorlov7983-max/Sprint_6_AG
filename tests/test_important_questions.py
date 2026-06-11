import pytest
import allure
from selenium import webdriver
from page_object.page_object_main import MainPage
import test_data as TD


class TestImportantQuestion:

    driver = None
    
    @classmethod
    def setup_class(cls):
        # Создание драйвера для браузера Firefox
        cls.driver = webdriver.Firefox()
        # Переход на страницу Самокат
        cls.driver.get(TD.url_main_page)
        # Создаем объект класса MainPage
        cls.main_page = MainPage(cls.driver)
        cls.main_page.click_order_button_cookies()
        
    @pytest.mark.parametrize('index',[0, 1, 2, 3, 4, 5, 6, 7], ids = [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Проверка вопросов о важном")
    @allure.step("Клик на вопрос {index}")
    def test_important_question(self, index):
        self.main_page.click_question_locator(index)
        actual_answers = self.main_page.text_answer(index)
        expected_answers = TD.answers[index]
        assert actual_answers == expected_answers

    @classmethod
    def teardown_class(cls):
        # закроем браузер
        cls.driver.quit() 


