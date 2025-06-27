import allure 
from data import Data
import pytest
from locators.main_page_locators import MainPageLocators


class TestOrderForm:
    @allure.title('Проверка заказа самоката')
    @allure.description('''1. Нажать Заказать 
                           2. Заполнить первую форму 
                           3. Нажать Далее
                           4. Заполнить вторую часто формы 
                           5. Нажать Заказать
                           6. Нажать подтверждение "Да"
                           7. Сверить заголовок формы "Информация о заказе"''')
    @pytest.mark.parametrize("info, button", [(Data.CUSTOMER_1, MainPageLocators.ORDER_BUTTON_TOP),
                                      (Data.CUSTOMER_2, MainPageLocators.ORDER_BUTTON_DOWN)])
    def test_order_form(self, order_page, info, button):
        order_page.scroll_and_click_on__button(button)
        title = order_page.fill_order_form(info)
        assert "Заказ оформлен" in title
