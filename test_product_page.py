import pytest
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By



def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_not_element_present(By.CSS_SELECTOR, ".alert-success")  # Передаем 'how' и 'what'

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(By.CSS_SELECTOR, ".alert-success")  # Передаем 'how' и 'what'

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_disappeared(By.CSS_SELECTOR, ".alert-success")  # Передаем 'how' и 'what'
