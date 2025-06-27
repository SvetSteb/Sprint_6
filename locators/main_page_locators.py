from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_BUTTON_MENU = [(By.ID, "accordion__heading-0"), #Локаторы кнопок списка вопросов, 8 вопросов с индексами от 0 до 7
                            (By.ID, "accordion__heading-1"),
                            (By.ID, "accordion__heading-2"),
                            (By.ID, "accordion__heading-3"),
                            (By.ID, "accordion__heading-4"),
                            (By.ID, "accordion__heading-5"),
                            (By.ID, "accordion__heading-6"),
                            (By.ID, "accordion__heading-7")]
    
    ANSWERS_MENU = [        (By.XPATH, "//div[@id='accordion__panel-0']/p"), # Локаторы текста ответов из списка вопросов
                            (By.XPATH, "//div[@id='accordion__panel-1']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-2']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-3']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-4']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-5']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-6']/p"),
                            (By.XPATH, "//div[@id='accordion__panel-7']/p")]

    DOWN = (By.CLASS_NAME, "Home_FinishButton__1_cWm")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g') #Кнопка Заказать вверху страницы
    ORDER_BUTTON_DOWN = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]') # Кнопка Заказать внизу страницы
    LOGO_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]')
    LOGO_YA = (By.XPATH, './/img[@alt="Yandex"]')
    HEADER_MAIN = (By.CLASS_NAME, 'Home_Header__iJKdX')
