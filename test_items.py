import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def test_basket(browser):
    link = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    basket = len(browser.find_elements_by_xpath(r'//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'))
    assert basket > 0
    time.sleep(30)