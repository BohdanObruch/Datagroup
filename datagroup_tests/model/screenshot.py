from datetime import datetime
import pytz
from selene import browser
from datagroup_tests.controls.utils import resource


def get_kiev_time():
    kiev_timezone = pytz.timezone('Europe/Kiev')
    kiev_time = datetime.now(kiev_timezone)
    return kiev_time


def creating_and_saving_a_screenshot():
    current_datetime = get_kiev_time().strftime('%d.%m.%y_%H.%M')
    screenshot_filename = f'screenshot_{current_datetime}.png'

    browser.driver.save_screenshot(resource(screenshot_filename))


