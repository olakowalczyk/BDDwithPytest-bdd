from pages.form import FormPage
from pytest_bdd import scenarios, given, when, then


scenarios('../features/form.feature')


@given('the form page is displayed')
def form(browser):
    form = FormPage(browser)
    form.load()
    return form


@when('new "<firstname>" is entered to the form')
def enter_firstname(form, firstname):
    form.enter_firstname(firstname)


@when('new "<lastname>" is entered to the form')
def enter_lastname(form, lastname):
    form.enter_lastname(lastname)


@then('the form contains new user "<firstname>"')
def form_has_firstname(form, firstname):
    assert form.firstname_input_value() == firstname


@then('the form contains new user "<lastname>"')
def form_has_lastname(form, lastname):
    assert form.lastname_input_value() == lastname


@when('initial values from firstname are cleared')
def clear_form(form):
    form.clear_form()


@then('the form fields are empty')
def form_is_empty(form):
    assert form.firstname_input_value() == ''
    assert form.lastname_input_value() == ''


@when('submit button is clicked')
def submit_form(form):
    form.submit()


@then('the form contains initial values')
def form_has_initial_firstname(form):
    assert form.firstname_input_value() == 'Mickey'
    assert form.lastname_input_value() == 'Mouse'
