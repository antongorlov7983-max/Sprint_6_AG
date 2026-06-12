import allure
import pytest
import test_data as TD


test_order_1 = TD.Order('антон','Горлов','Партизана д7','15','79999999999','15.06.2026','3','grey','Позвонить как доставите',)
test_order_2 = TD.Order('мария','Иванова','Партизана д7 кв 77','19','79999999977','13.06.2026','3','black','оставить около двери',)


@pytest.mark.parametrize('button, test_order',
    [('нижнюю', test_order_1),
     ('верхнюю', test_order_2)
    ], 
    ids = ['lower_button',
        'upper_button'
    ])
@allure.title("Проверка оформления заказа через {button} кнопку")
def test_upper_button_order(main_page, form_user, form_scooter, order_confirmation, button, test_order):
    main_page.choice_order_button(button)
    form_user.filling_form_user(**test_order.get_order_user())
    form_user.click_button_next()
    form_scooter.filling_form_about_rent(**test_order.get_order_about_rent())
    form_scooter.click_button_order()
    order_confirmation.click_button_yes()
    assert "Заказ оформлен" in order_confirmation.get_text_title_order_placed()
