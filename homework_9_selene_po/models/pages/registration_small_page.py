from selene import browser, have
from selene.support.conditions import be

from homework_9_selene_po.models.user import User


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('[id="userName"]')
        self.email = browser.element('[id="userEmail"]')
        self.currentAddress = browser.element('[id="currentAddress"]')
        self.permanentAddress = browser.element('[id="permanentAddress"]')
        self.submit_button = browser.element('[id="submit"]')
        self.output = browser.element('[id="output"]')

    def open(self):
        browser.open('/text-box')
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_full_name(self, value):
        self.full_name.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def fill_current_address(self, value):
        self.currentAddress.should(be.blank).type(value)

    def fill_permanent_address(self, value):
        self.permanentAddress.should(be.blank).type(value)

    def submit(self):
        self.submit_button.click()

    def register(self, user: User): # Берем данные юзера из класса User в файле user.py
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        #описываем шаги
        pass

    def should_data(self, user: User):
        self.submit()
        self.output.should(have.text(user.full_name))  # 'Ignatov Andrey'
        self.output.should(have.text(user.email))  # 'test-mail2025@gmail.com'
        self.output.should(have.text(user.current_address))  # 'Test address 2025'
        self.output.should(have.text(user.permanent_address))  # 'Test permanent address 2025'