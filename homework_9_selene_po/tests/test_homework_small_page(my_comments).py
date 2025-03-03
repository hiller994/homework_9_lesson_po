from homework_9_selene_po.models import users_date
from homework_9_selene_po.models.pages.registration_small_page import SimpleUserRegistrationPage


def test_small_form(browser_settings):
    simple_reg_page = SimpleUserRegistrationPage()
    simple_reg_page.open()

    simple_reg_page.register(users_date.guest)
    # одна строчка заменяет все ниже перечисленные. Используем функцию register(registration_small_page), в которой все шаги записаны и подставляем данные из users_date ( шаблоном которой является user.py(User))
    '''
    simple_reg_page.fill_full_name('Ignatov Andrey')
    simple_reg_page.fill_email('test-mail2025@gmail.com')
    simple_reg_page.fill_current_address('Test address 2025')
    simple_reg_page.fill_permanent_address('Test permanent address 2025')
    '''


    simple_reg_page.should_data(users_date.guest)
    # одна строчка заменяет все ниже перечисленные. Используем функцию should_data(registration_small_page), в которой все шаги записаны и подставляем данные из users_date ( шаблоном которой является user.py(User))
    '''
    browser.element('[id="output"]').should(have.text('Ignatov Andrey'))
    browser.element('[id="output"]').should(have.text('test-mail2025@gmail.com'))
    browser.element('[id="output"]').should(have.text('Test address 2025'))
    browser.element('[id="output"]').should(have.text('Test permanent address 2025'))
    '''