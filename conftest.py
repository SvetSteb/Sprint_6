from selenium import webdriver
import pytest
from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
