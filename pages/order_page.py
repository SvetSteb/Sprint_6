from pages.base_page import BasePage
from locators.order_page_locators import OrderFormLocators
import allure
import helpers


@allure.feature('Оформление заказа самоката')
class OrderPage(BasePage):

    @allure.step('Заполнение и отправка формы заказа самоката')
    def fill_order_form(self, info):
        self.wait_for_visibiliti_of_element(OrderFormLocators.NAME_FIELD)
        self.send_keys(OrderFormLocators.NAME_FIELD, info['name'])
        self.send_keys(OrderFormLocators.SECOND_NAME_FIELD, info['second_name'])
        self.send_keys(OrderFormLocators.ADRESS_FIELD, info['adress'])
        self.wait_for_and_click_element(OrderFormLocators.METRO_STATION_MENU)
        self.send_keys(OrderFormLocators.METRO_STATION_MENU, info['metro'])
        self.wait_for_and_click_element(OrderFormLocators.METRO_STATION_ITEM)
        self.send_keys(OrderFormLocators.PHONE_FIELD, info['phone'])
        self.wait_for_and_click_element(OrderFormLocators.NEXT_BUTTON)
        self.wait_for_visibiliti_of_element(OrderFormLocators.DATE_FIELD)
        date = helpers.tomorrow_date()
        self.send_keys_enter(OrderFormLocators.DATE_FIELD, date)
        self.wait_for_and_click_element(OrderFormLocators.TERM_MENU)
        self.wait_for_and_click_element(OrderFormLocators.TERM_ITEM_2)
        self.wait_for_and_click_element(OrderFormLocators.SUBMIT_ORDER_BUTTON)
        self.wait_for_and_click_element(OrderFormLocators.CONFIRM_ORDER_YES_BUTON)
        window_title = self.wait_for_visibiliti_of_element(OrderFormLocators.ORDER_INFO_FORM).text
        return window_title

