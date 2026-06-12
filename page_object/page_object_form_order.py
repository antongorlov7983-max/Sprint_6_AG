import allure
from page_object.page_object_base import BasePage
from selenium.webdriver.common.by import By


class OrderPageFormUser(BasePage):

    input_name = (By.XPATH, '//input[@placeholder = "* Имя"]') # Поле "Имя"
    input_surname = (By.XPATH, '//input[@placeholder = "* Фамилия"]') # Поле "Фамилия"
    input_address = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]') # Поле "Адрес"
    input_metro_station = (By.XPATH, '//input[@placeholder = "* Станция метро"]') # Поле "Станция"
    input_number = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]') # Поле "Телефон"
    button_next = (By.CSS_SELECTOR,'[class*="Button_Middle"]') # Кнопка "Далее"

    @allure.step('Заполняем поле "Имя"')
    def set_input_name(self, name):
        self.wait_visible(self.input_name).send_keys(name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_input_surname(self, surname):
        self.wait_visible(self.input_surname).send_keys(surname)

    @allure.step('Заполняем поле "Адресс"')
    def set_input_address(self, address):
        self.wait_visible(self.input_address).send_keys(address)

    @allure.step('Кликаем на поле "Станция"')
    def click_input_metro_station(self):
        self.wait_visible(self.input_metro_station).click()

    # Создать локатор станции из списка
    def get_station_locator(self, index_station):
        return (By.XPATH, f'//li[@data-index = {index_station}]')
        
    # Получение названия станции
    def get_name_station(self, index_station):
        return (By.XPATH, f'//li[@data-index = {index_station}]/button/div[contains(@class,"Order_Text")]')
    
    @allure.step('Из выпадающего списка кликаем на станцию')
    def click_station(self, index_station):
        station_name = self.wait_visible(self.get_name_station(index_station)).text
        allure.attach(station_name, name="Выбранная станция", attachment_type=allure.attachment_type.TEXT)
        self.wait_visible(self.get_station_locator(index_station)).click()

    @allure.step('Заполняем поле "Телефон"')
    def set_input_number(self, number):
        self.wait_visible(self.input_number).send_keys(number)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_button_next(self):
        self.wait_visible(self.button_next).click()

    # Заполняем форму "Для кого самокат"
    def filling_form_user(self, name, surname, address, index_station, number):
        self.set_input_name(name)
        self.set_input_surname(surname)
        self.set_input_address(address)
        self.click_input_metro_station()
        self.click_station(index_station)
        self.set_input_number(number)
        

class OrderPageFormScooter(BasePage):

    input_date = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]') # Поле "Когда привезти самокат"
    input_rental_period = (By.CLASS_NAME,'Dropdown-placeholder') #  Поле "Срок аренды"
    choice_rental_day = (By.XPATH,'.//div[@role="option"]') # Список выбора продолжительности аренды (прописью)
    type_locator_checkboxes_color_scooter = By.ID  # Тип локатора выбора цвета скутера
    color_scooter = ('black', 'grey') # цвета скутеров
    input_commit = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]') # Поле "Комментарий для курьера"
    button_order = (By.XPATH, '//button[contains(@class, "Button_Middle") and text() = "Заказать"]') # Кнопка "Заказать"  

    @allure.step('Заполнение поле "Когда привезти самокат"')
    def set_input_date(self, date):
        self.set_input_enter(self.input_date, date)

    @allure.step('Клик по полю "Срок аренды"')
    def click_input_rental_period(self):
        self.wait_visible(self.input_rental_period).click()
        
    @allure.step('Выбор срока аренды')
    def set_rental_day(self, days):
        self.get_all_elements(self.choice_rental_day)[int(days)-1].click()

    # Создание локатора чекбокса цвета скутера
    def choice_color_scooter(self, color):
        return (self.type_locator_checkboxes_color_scooter, f'{color}')
        
    @allure.step('Выбор цвета скутера: {color}')
    def click_checkboxes_color_scooter(self, color):
        if color in self.color_scooter:
            self.wait_visible(self.choice_color_scooter(color)).click()

    @allure.step('Заполнение поля "Коментарий для курьера"')
    def set_input_commit(self, commit):
        self.wait_visible(self.input_commit).send_keys(commit)

    @allure.step('Клик по кнопке "Заказать"')
    def click_button_order(self):
        self.wait_visible(self.button_order).click()

    # Заполнение формы "Про заказ"
    def filling_form_about_rent(self, date, days, color, commit):
        self.set_input_date(date)
        self.click_input_rental_period()
        self.set_rental_day(days)
        self.click_checkboxes_color_scooter(color)
        self.set_input_commit(commit)


class OrderPageConfirmation(BasePage):

    button_yes = (By.XPATH, '//button[text() = "Да"]') # Кнопка подтверждения заказа
    title_order_placed= (By.XPATH,'//*[text()="Заказ оформлен"]') # Заголовок 
    button_check_status = (By.XPATH, '//*[text()="Посмотреть статус"]') # Кнопка "Посмотреть статус"

    @allure.step('Кликаем по кнопке "Да"')
    def click_button_yes(self):
        self.wait_visible(self.button_yes).click()

    # Получение текста подтверждения заказа
    def get_text_title_order_placed(self):
        return self.wait_visible(self.title_order_placed).text