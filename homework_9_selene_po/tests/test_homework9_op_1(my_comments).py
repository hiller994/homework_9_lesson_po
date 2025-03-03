import time

from selene import browser, have

from homework_9_selene_po.models.pages.registration_page import RegistrationPage


def test_practice_form(browser_settings):
    # Открываем страницу, вызывав функцию open
    registration_page = RegistrationPage()  # создаем экземпляр(объект) этого класса. Делаем этого, чтобы использовать класс
    registration_page.open()

    # Вводим Имя и Фамилию
    registration_page.fill_first_name('Andrey').fill_last_name('Ignatov')

    # Вводим почту
    registration_page.fill_email('homework5@gmail.com')

    # Выбираем гендер
    registration_page.fill_gender('[for="gender-radio-1"]')

    # Вводим номер телефона
    registration_page.fill_mobile('8800553535')

    # выбираем день рождения
    registration_page.fill_date_of_birth(1994, 10, 21)

    # выбираем предметы Subjects
    registration_page.fill_subjects('History')

    # выбираем предметы Hobbies
    registration_page.fill_hobbies('[for="hobbies-checkbox-1"]')

    # загрузка файла
    registration_page.fill_picture('../test_file/test_pic.jpg')

    # ввод адреса
    registration_page.fill_current_address('Test addres 12345')

    # выбрать страну и город
    registration_page.fill_state('Haryana').fill_city('Karnal')
    time.sleep(10)

    # итоговая проверка
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