from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("ожидания видимости элемента")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    @allure.step("Клик через JavaScript (обход перекрытий)")
    def click_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Закрыть элемент, если он присутствует на странице")
    def close_if_exists(self, locator):
        try:
            self.wait_visible(locator).click()
        except:
            pass

    @allure.step("Сохранить текущий дескриптор окна")
    def save_windows_handle(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, main_handle):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_handle = [handle for handle in self.driver.window_handles if handle != main_handle][0]
        self.driver.switch_to.window(new_handle)

    @allure.step("Ожидание появления подстроки {text} в URL")
    def wait_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)

    @allure.step("Заполнить поле и нажать Enter")
    def set_input_enter(self, element, data):
        field = self.wait_visible(element)
        field.send_keys(data)
        field.send_keys(Keys.ENTER)

    @allure.step("Получить список")
    def get_all_elements(self, elements_locator):
        self.wait_visible(elements_locator)
        elements = self.driver.find_elements(*elements_locator)
        if not elements:
            raise Exception(f"Элементы не найдены: {elements_locator}")
        return elements
    
    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url