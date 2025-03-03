from homework_9_selene_po.models import users_date
from homework_9_selene_po.models.pages.registration_small_page import SimpleUserRegistrationPage


def test_small_form(browser_settings):
    simple_reg_page = SimpleUserRegistrationPage()
    simple_reg_page.open()

    simple_reg_page.register(users_date.guest)
    simple_reg_page.should_data(users_date.guest)
