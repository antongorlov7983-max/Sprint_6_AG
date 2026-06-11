from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:

    upper_order_button = (By.XPATH, '//div[contains(@class,"Nav")]/button[contains(@class,"Button")]') # Кнопка "Заказать" в заголовке страницы
    lower_order_button = (By.XPATH, '//button[contains(@class,"Button_Button") and contains(text(),"Заказать")]') # Кнопка "Заказать" внизу страницы
    logo_scooter = (By.XPATH, '//a[contains(@class,"LogoScooter")]') # Логотип самокат
    logo_yandex = (By.CSS_SELECTOR,'[class*="Header_LogoYandex"]') # Логотип яндекса
    button_cookies = (By.ID,'rcc-confirm-button') # Кнопка закрытия банеры куки

    def __init__(self,driver):
        self.driver = driver 

    def click_order_button_cookies(self):
        try:
            self.driver.find_element(*self.button_cookies).click()
        except:
            pass

    # Кликаем на верхнюю кнопку
    def click_upper_order_button(self):
        self.driver.find_element(*self.upper_order_button).click()

    # Кликаем на нижнюю кнопку
    def click_lower_order_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.driver.find_element(*self.lower_order_button)
        self.driver.execute_script("arguments[0].click();", element)

    # получаем локатор на вопрос
    def get_question_locator(self, index):
        return (By.ID, f'accordion__heading-{index}')
    
    # кликаем на вопрос
    def click_question_locator(self, index):
        element = self.driver.find_element(*self.get_question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    # получаем локатор на ответ
    def get_answer_locator(self, index):
        return (By.ID, f'accordion__panel-{index}')
    
    # получаем текст ответа из страницы
    def text_answer(self, index):
        answer = self.driver.find_element(*self.get_answer_locator(index))
        WebDriverWait(self.driver, 5).until(EC.visibility_of(answer))
        return answer.text

    # Клик по логотипу "Самокат"
    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    # Кликаем по логотипу яндекс
    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()
