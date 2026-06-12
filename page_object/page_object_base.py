from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Метод ожидания видимости элемента
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    # Метод со скроллом  вниз и кликом на элемент игнорирующий перекрытие другими элементами
    def click_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
        self.driver.execute_script("arguments[0].click();", element)

    # Закрытие всплывающих банеров
    def close_if_exists(self, locator):
        try:
            self.wait_visible(locator).click()
        except:
            pass

    # Метод сохранения текущий дескриптор окна
    def save_windows_handle(self):
        return self.driver.current_window_handle

    # Метод ожидания появления второго окна и переключения на него
    def switch_to_new_window(self, main_handle):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_handle = [handle for handle in self.driver.window_handles if handle != main_handle][0]
        self.driver.switch_to.window(new_handle)

    # Метод ожидания появления ожидаемого url
    def wait_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)

    # Метод заполнения поля и подтверждения ввода
    def set_input_enter(self, element, data):
        field = self.wait_visible(element)
        field.send_keys(data)
        field.send_keys(Keys.ENTER)

    # Метод получения списка элементов
    def get_all_elements(self, elements_locator):
        self.wait_visible(elements_locator)
        elements = self.driver.find_elements(*elements_locator)
        if not elements:
            raise Exception(f"Элементы не найдены: {elements_locator}")
        return elements