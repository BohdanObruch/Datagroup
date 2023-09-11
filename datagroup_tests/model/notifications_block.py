from selene import browser, be

from datagroup_tests.helpers.locator import *
from datagroup_tests.model.screenshot import creating_and_saving_a_screenshot


def checking_the_display_of_the_notifications_block():
    if browser.element(alert_block).with_(timeout=10).should(be.not_.visible):
        pass
    else:
        creating_and_saving_a_screenshot()
