import pytest
import allure
import test_data as TD


class TestImportantQuestions:

    @pytest.mark.parametrize('index', list(TD.question.keys()), ids=list(TD.question.keys()))
    def test_important_question(self, main_page, index):
        allure.dynamic.title(f'Проверка ответа на вопрос: {TD.question[index][0]}')
        allure.dynamic.description(f'Ожидаемый ответ: {TD.question[index][1]}')
    
        main_page.click_question_locator(index)
        actual = main_page.text_answer(index)
        assert actual == TD.question[index][1]