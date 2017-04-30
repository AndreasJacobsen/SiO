# file:features/steps/step_add_member.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('a member form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_signup/')


@when('i fill in "foo","bar","fb@gmail.com","female","1990-02-01","2017-01-01","2017-06-03"')
# @when('i fill in and register the form')
def step_impl(context):
    # br = context.browser
    # context.browser('/cover/')
    # context.browser.select_form(nr=0)
    # context.browser.form['username'] = 'foo'
    # context.browser.form['password'] = 'bar'
    # context.browser.submit()

    # context.browser.visit('/')
    # username_field = context.browser.find_by_id('username')
    # password_field = context.browser.find_by_id('password')
    # username_field.send_keys('foo')
    # password_field.send_keys('bar')
    # submit_button = context.browser.find_by_id('submit')
    # submit_button.click()

    br = context.browser
    br.get(context.base_url + '/member_signup/')

    # Checks for Cross-Site Request Forgery protection input
    # assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('first_name').send_keys('foo')
    br.find_element_by_name('last_name').send_keys('bar')
    br.find_element_by_name('email').send_keys('fb@gmail.com')
    br.find_element_by_name('gender').send_keys('female')
    br.find_element_by_name('date_of_birth').send_keys('1990-02-01')
    br.find_element_by_name('reg_date').send_keys('2017-01-01')
    br.find_element_by_name('end_date').send_keys('2017-06-03')


@when('register the member form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@when('cancel the member form')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('cancel').click()


# @then('i will see a success message')
@then('i will see the new member added')
def step_impl(context):
    # br = context.browser
    # response = br.response()
    # assert response.code == 200
    # assert br.geturl().endswith('/dashboard/')

    # assert context.browser.response.code == 200
    # assert context.browser.endswith('/dashboard/')

    br = context.browser

    # Checks success status
    # assert br.current_url.endswith('/dashboard/')
    br.get(context.base_url + '/member_overview/')
    # br.find_element_by_name('message')


@then('i will be redirected to overview of all members')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/member_overview/')



