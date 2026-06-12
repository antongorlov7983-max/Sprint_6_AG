import pytest
from selenium import webdriver
from page_object.page_object_main import MainPage
import page_object.page_object_form_order as PO
import test_data as TD


@pytest.fixture(scope="function")
def driver():
    # Открываем браузер
    driver = webdriver.Firefox()
    # Переход на страницу Самокат
    driver.get(TD.url_main_page)
    yield driver
    # Закрываем браузер
    driver.quit()
    
@pytest.fixture(scope="function")
def main_page(driver):
    page = MainPage(driver)
    page.close_button_cookies()
    return page

@pytest.fixture(scope="function")
def form_user(driver):
    return PO.OrderPageFormUser(driver)

@pytest.fixture(scope="function")
def form_scooter(driver):
    return PO.OrderPageFormScooter(driver)

@pytest.fixture(scope="function")
def order_confirmation(driver):
    return PO.OrderPageConfirmation(driver)
