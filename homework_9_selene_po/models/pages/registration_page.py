import os

from selene import browser, be, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('[id="userEmail"]').should(be.blank).type(value)

    def fill_gender(self,value):
        browser.element(value).click()

    def fill_mobile(self, value):
        browser.element('[id="userNumber"]').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click().element(f'[value="{month}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click().element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    '''
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        '''

    def fill_subjects(self, value):
        browser.element('[id="subjectsInput"]').set_value('his').element(f'//*[contains(text(),"{value}")]').click()

    def fill_hobbies(self,value):
        browser.element(value).click()

    def fill_picture(self, value):
        browser.element('[id="uploadPicture"]').type(os.path.abspath(value))

    def fill_current_address(self, value):
        browser.element('[id="currentAddress"]').should(be.blank).type(value)

    def fill_state(self, state):
        browser.element('[id="react-select-3-input"]').set_value('Hary').element(
            f'//*[contains(text(),"{state}")]').click()
        return self

    def fill_city(self, city):
        browser.element('[id="react-select-4-input"]').set_value('Kar').element(
            f'//*[contains(text(),"{city}")]').click()

    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address, state_and_city):
        browser.element('[id="submit"]').click()
        browser.element('[class="modal-content"]').should(be.visible)
        browser.element('[class="modal-content"]').should(have.text(full_name))  # Student Name
        browser.element('[class="modal-content"]').should(have.text(email))  # Student Email
        browser.element('[class="modal-content"]').should(have.text(gender))  # Gender
        browser.element('[class="modal-content"]').should(have.text(mobile))  # Mobile
        browser.element('[class="modal-content"]').should(have.text(date_of_birth))  # Date of Birth
        browser.element('[class="modal-content"]').should(have.text(subjects))  # Subjects
        browser.element('[class="modal-content"]').should(have.text(hobbies))  # Hobbies
        browser.element('[class="modal-content"]').should(have.text(picture))
        browser.element('[class="modal-content"]').should(have.text(address))
        browser.element('[class="modal-content"]').should(have.text(state_and_city))