import pytest
from selenium import webdriver

from data.login_data import login_data_success
from pages.login import LoginPage


@pytest.fixture(scope='class')
def browser():
    """管理浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def login(browser):
    index_page = LoginPage(browser).get().login_success(login_data_success[0]['username'], login_data_success[0]['pwd'])
    return index_page