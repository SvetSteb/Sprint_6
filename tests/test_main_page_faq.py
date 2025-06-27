import allure 
from data import Data
import pytest


class TestQuestionsAndAnswersMainPage:
    @allure.title('Проверка списка вопросов и ответов в разделе "Вопросы о важном"')
    @allure.description('''1. Перейти на главную страницу
                           2. Скролл до списка вопросов 
                           3. Кликнуть на вопрос
                           4. Сверить появившийся текст ответа''')
    @pytest.mark.parametrize("item", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_questions_and_answers(self, main_page, item):
        main_page.click_on_question(item)
        answer_fr = main_page.find_answer(item)
        assert answer_fr == Data.ANSWERS[item]
