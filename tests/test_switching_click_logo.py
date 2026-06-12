import allure
import test_data as TD


# Тестирование перехода при клике на логотип Самокат
@allure.title("Проверка отсутствия перехода при клике на логотип 'Самокат'")
def test_click_logo_scooter(main_page):
    main_page.click_logo_scooter()
    assert TD.url_main_page == main_page.driver.current_url

# Тестирование перехода при клике на логотип яндекс
@allure.title("Проверка перехода на страницу Дзен при клике на логотип 'Яндекс'")
def test_click_logo_yandex(main_page):
    main_page.open_page_dzen("dzen.ru")
    assert "dzen.ru" in main_page.driver.current_url
