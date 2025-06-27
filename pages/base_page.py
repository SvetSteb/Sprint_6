import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:

    @allure.step('Получить и инициализировать драйвер')
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Ожидание и получение элемента')
    def wait_for_visibiliti_of_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    

    @allure.step('Ожидание кликабельности, клик по элементу')
    def wait_for_and_click_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Получение текста элемента')
    def get_elements_text(self, locator):
        text = self.wait_for_visibiliti_of_element(locator).text
        return text


    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_visibiliti_of_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Прокрутить до элемента и кликнуть')
    def scroll_and_click_on__button(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_and_click_element(locator)


    @allure.step('Заполнение поля данными')
    def send_keys(self, locator, text):
        self.wait_for_visibiliti_of_element(locator).send_keys(text)


    @allure.step('Заполнение поля данными и нажатие Enter')
    def send_keys_enter(self, locator, text):
        self.wait_for_visibiliti_of_element(locator).send_keys(text + Keys.ENTER)

    def switch_to_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])