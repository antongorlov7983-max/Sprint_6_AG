from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrderScooter:
    # Локаторы формы "Для кого самокат"
    input_name = (By.XPATH, '//input[@placeholder = "* Имя"]') # Поле "Имя"
    input_surname = (By.XPATH, '//input[@placeholder = "* Фамилия"]') # Поле "Фамилия"
    input_address = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]') # Поле "Адрес"
    input_metro_station = (By.XPATH, '//input[@placeholder = "* Станция метро"]') # Поле "Станция"
    input_number = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]') # Поле "Телефон"
    button_next = (By.CSS_SELECTOR,'[class*="Button_Middle"]') # Кнопка "Далее"
    # Локаторы формы "Про аренду"
    input_date = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]') # Поле "Когда привезти самокат"
    input_rental_period = (By.CLASS_NAME,'Dropdown-placeholder') #  Поле "Срок аренды"
    choice_rental_day = (By.XPATH,'.//div[@role="option"]') # Список выбора продолжительности аренды (прописью)
    type_locator_checkboxes_color_scooter = By.ID  # Тип локатора выбора цвета скутера
    color_scooter = ('black', 'grey') # цвета скутеров
    input_commit = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]') # Поле "Комментарий для курьера"
    button_order = (By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]') # Кнопка "Заказать" завершение заполнение форм (такой локатор из-за отсутствия индивидуальности в атрибутах и на странице присутствует другая кнопка "заказать")
    # Локаторы подтверждения заказа
    button_yes = (By.XPATH, '//button[text() = "Да"]') # Кнопка подтверждения заказа
    title_order_placed= (By.XPATH,'//*[text()="Заказ оформлен"]') # Заголовок 
    button_check_status = (By.XPATH, '//*[text()="Посмотреть статус"]') # Кнопка "Посмотреть статус"

    def __init__(self,driver):
        self.driver = driver

    # Проверка видимости кнопки "Далее"
    def visibility_input_name(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.input_name))

    # Методы заполнения формы "Для кого самокат"
    # Заполняем поле "Имя"
    def set_input_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    # Заполняем поле "Фамилия"
    def set_input_surname(self, surname):
        self.driver.find_element(*self.input_surname).send_keys(surname)

    # Заполняем поле "Адресс"
    def set_input_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    # Кликаем на поле "Станция"
    def click_input_metro_station(self):
        self.driver.find_element(*self.input_metro_station).click()

    # Создать локатор станции из списка
    def get_station_locator(self, index_station):
        return (By.XPATH, f'//li[@data-index = {index_station}]')
    
    # Кликаем на станцию из выпадающего списка
    def click_station(self, index_station):
        self.driver.find_element(*self.get_station_locator(index_station)).click()

    # Заполняем поле "Телефон"
    def set_input_number(self, number):
        self.driver.find_element(*self.input_number).send_keys(number)

    # Нажимаем кнопку "Далее"
    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

    # Ожидание видимости кнопки "Заказать"
    def visibility_button_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.button_order))

    # Методы для заполнения формы "Про аренду"
    # Заполнение поле "Когда привезти самокат"
    def set_input_date(self, date):
        field = self.driver.find_element(*self.input_date)
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    # Клик по полю "Срок аренды"
    def click_input_rental_period(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.input_rental_period)).click()
        
    # Выбор срока аренды
    def clik_choice_rental_day(self, days):
        self.driver.find_elements(*self.choice_rental_day)[int(days)-1].click()

    # Создание локатора чекбокса цвета скутера
    def choice_color_scooter(self, color):
            return (self.type_locator_checkboxes_color_scooter, f'{color}')
        
    # Выбор цвета скутера
    def clik_checkboxes_color_scooter(self, color):
        if color in self.color_scooter:
            self.driver.find_element(*self.choice_color_scooter(color)).click()

    # Заполнение поля "Коментарий для курьера"
    def set_input_commit(self, commit):
        self.driver.find_element(*self.input_commit).send_keys(commit)

    # Клик по кнопке "Заказать"
    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()

    # Подтверждение заказа
    # Ожидание кликабельности кнопки "Да"
    def clickability_button_yes(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_yes)
        )
    # Кликаем по кнопке "Да"
    def click_button_yes(self):
        self.driver.find_element(*self.button_yes).click()

    # Проверяе кликабельность кнопки посмотреть статус
    def clickability_button_check_status(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_check_status)
        )

    # Получение текста подтверждения заказа
    def get_text_title_order_placed(self):
        return self.driver.find_element(*self.title_order_placed).text

    # Заполняем форму "Для кого самокат"
    def filling_form_user(self, name, surname, address, index_station, number):
        self.visibility_input_name()
        self.set_input_name(name)
        self.set_input_surname(surname)
        self.set_input_address(address)
        self.click_input_metro_station()
        self.click_station(index_station)
        self.set_input_number(number)
        
    # Заполнение формы "Про заказ"
    def filling_form_about_rent(self, date, days, color, commit):
        self.visibility_button_order()
        self.set_input_date(date)
        self.click_input_rental_period()
        self.clik_choice_rental_day(days)
        self.clik_checkboxes_color_scooter(color)
        self.set_input_commit(commit)

    def confirming_order(self):
        self.clickability_button_yes()
        self.click_button_yes()
        self.clickability_button_check_status()

