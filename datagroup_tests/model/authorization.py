from selene import browser, be
from tests.conftest import dotenv
from datagroup_tests.helpers.locator import *

login = dotenv.get('LOGIN')
password = dotenv.get('PASSWORD')
base_url = dotenv.get('BASE_URL')


def authorization_on_the_site():
    browser.element(login_tub_locator).click()

    browser.element(login_locator).type(login)
    browser.element(password_locator).type(password)
    browser.element(submit).click()


def display_dashboard():
    browser.element(title_block_locator).with_(timeout=10).should(be.visible)
    browser.element(loader).with_(timeout=10).should(be.not_.visible)
