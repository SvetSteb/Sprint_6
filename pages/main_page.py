from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.general_locators import GeneralLocators
import allure
from data import Urls

class MainPage(BasePage):

    @allure.step('Клик по ссылке c вопросом')
    def click_on_question(self, item):
        self.scroll_to_element(MainPageLocators.QUESTION_BUTTON_MENU[7])
        self.wait_for_and_click_element(MainPageLocators.QUESTION_BUTTON_MENU[item])


    @allure.step('Нахождение текста ответа на вопрос')
    def find_answer(self, item):
        answer = self.get_elements_text(MainPageLocators.ANSWERS_MENU[item])
        return answer


    @allure.step('Клик по логотипу "Самокат"')
    def click_on_logo_scooter(self):
        self.wait_for_and_click_element(MainPageLocators.LOGO_SCOOTER)


    @allure.step('Клик по логотипу "Яндекс"')
    def click_on_logo_yandex(self):
        self.wait_for_and_click_element(MainPageLocators.LOGO_YA)

    
    @allure.step('Клик по лого "Самокат" и получение заголовка страницы')
    def check_on_logo_scooter(self):
        self.scroll_and_click_on__button(MainPageLocators.ORDER_BUTTON_TOP)
        self.click_on_logo_scooter()
        WebDriverWait(self.driver, 10).until(EC.url_changes(Urls.ORDER_PAGE))        
        return self.get_elements_text(MainPageLocators.HEADER_MAIN)

    @allure.step('Клик по лого "Яндекс" и получение текста элемента открывшейся страницы')
    def check_on_logo_yandex(self):
        self.click_on_logo_yandex()
        self.switch_to_window()
        WebDriverWait(self.driver, 10).until(EC.url_contains(Urls.DZEN))      
        return self.get_elements_text(GeneralLocators.DZEN_SEARCH)

