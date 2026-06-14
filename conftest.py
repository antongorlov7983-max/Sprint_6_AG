import pytest
from selenium import webdriver
from page_object.page_object_main import MainPage
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
