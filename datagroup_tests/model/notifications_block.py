import time
from selene import browser, be, have
from datagroup_tests.helpers.locator import *
from datagroup_tests.model.screenshot import creating_and_saving_a_screenshot


def checking_the_display_of_the_notifications_block():
    if browser.element(alert_block).with_(timeout=10).matching(be.visible):
        if browser.element(alert_block).matching(have.text('По вашому будинку аварія послуги Інтернет')
                                            .or_(have.text('Аварія на Вашій ділянці'))):
            creating_and_saving_a_screenshot()
            assert False, 'По вашому будинку аварія послуги Інтернет'
        else:
            pass
    elif browser.element(alert_block).with_(timeout=10).matching(be.not_.visible):
        pass
    else:
        pass