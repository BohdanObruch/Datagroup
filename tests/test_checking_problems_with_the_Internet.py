from datagroup_tests.model.notifications_block import checking_the_display_of_the_notifications_block
from tests.conftest import opened_page_website
from datagroup_tests.model.authorization import (authorization_on_the_site,
                                                 display_dashboard)


def test_receiving_a_daily_bonus(setup_browser):
    opened_page_website()

    authorization_on_the_site()

    display_dashboard()

    checking_the_display_of_the_notifications_block()
