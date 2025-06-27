import allure 

class TestLogo:

    @allure.title('Проверка перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description('''1. Перейти на страницу заказа
                           2. Кликнуть Лого Самокат
                           3. Дождаться изменения URL
                           4. Сверить заголовок на главной странице содержит слово "Самокат"''')
    def test_logo_scooter_go_to_main(self, main_page):
        header = main_page.check_on_logo_scooter()
        assert 'Самокат' in header


    @allure.title('Проверка перехода на Дзен по клику на логотип "Яндекс"')
    @allure.description('''1. Перейти на сайт
                           2. Кликнуть Лого Яндекс
                           3. Дождаться открытия новой вкладки
                           4. Сверить текст плейсхолдера в найденной на странице поисковой строке содержит "ПоискЯндекса"''')
    def test_logo_yandex_redirect_to_dzen(self, main_page):
        text = main_page.check_on_logo_yandex()
        assert 'Поиск Яндекса' in text
