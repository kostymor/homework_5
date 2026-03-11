import pytest
from selene import browser, have
from selene.support.shared import config
from time import sleep

@pytest.fixture(scope='function', autouse=True)
def setup():
    config.browser = 'chrome'
    config.timeout = 10
    config.window_width = 1920
    config.window_height = 1080
    yield
    browser.quit()

def test_work_5():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('name')

    browser.element('#lastName').type('lastname')

    browser.element('#userEmail').type('user_email@example.com')

    browser.element('#gender-radio-1').click()

    browser.element('#userNumber').type('9999999999')

    #Заполнение календаря
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('//option[text()="2000"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('//option[text()="January"]').click()
    browser.element('.react-datepicker__day').click()

    browser.element('.subjects-auto-complete__input').type('M').press_enter()

    browser.element('#hobbies-checkbox-1').click()

    browser.element("#currentAddress").type('TEST')

    browser.element('#react-select-3-input').click().press_enter()

    browser.element('#react-select-4-input').click().press_enter()

    browser.element('#submit').click()

    browser.all('.table-responsive td').should(
        have.exact_texts(
            'Student Name', 'name lastname',
            'Student Email', 'user_email@example.com',
            'Gender', 'Male',
            'Mobile', '9999999999',
            'Date of Birth', '26 December,1999',
            'Subjects', 'Maths',
            'Hobbies', 'Sports',
            'Picture', '',
            'Address', 'TEST',
            'State and City', 'NCR Delhi'
        )
    )



