from selenium.webdriver.common.by import By

class OrderFormLocators:
    NAME_FIELD = (By.XPATH, './/input[@placeholder="* Имя"]')
    SECOND_NAME_FIELD = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADRESS_FIELD = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_MENU = (By.XPATH, './/input[@placeholder="* Станция метро"]')

    METRO_STATION_ITEM = (By.XPATH, './/div[@class="select-search__select"]' )
    PHONE_FIELD = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Далее"]')
    DATE_FIELD = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    TERM_MENU = (By.CLASS_NAME, 'Dropdown-control')
    TERM_ITEM_2 = (By.XPATH, './/div[@class="Dropdown-option" and text()="двое суток"]')
    COLOUR_BLACK = (By.XPATH, './/input[@class="Checkbox_Input__14A2w" and id="black"]')

    SUBMIT_ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRM_ORDER_YES_BUTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')

    ORDER_INFO_FORM = (By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"]')

