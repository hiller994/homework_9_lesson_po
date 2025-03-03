import time
from homework_9_selene_po.models.pages.registration_page import RegistrationPage


def test_practice_form(browser_settings):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Andrey').fill_last_name('Ignatov')
    registration_page.fill_email('homework5@gmail.com')
    registration_page.fill_gender('[for="gender-radio-1"]')
    registration_page.fill_mobile('8800553535')
    registration_page.fill_date_of_birth(1994,10, 21)
    registration_page.fill_subjects('History')
    registration_page.fill_hobbies('[for="hobbies-checkbox-1"]')
    registration_page.fill_picture('../test_file/test_pic.jpg')
    registration_page.fill_current_address('Test addres 12345')
    registration_page.fill_state('Haryana').fill_city('Karnal')

    registration_page.should_registered_user_with(
        'Andrey Ignatov',
        'homework5@gmail.com',
        'Male',
        '8800553535',
        '21 November,1994',
        'History',
        'Sport',
        'test_pic.jpg',
        'Test addres 12345',
        'Haryana Karnal'
    )