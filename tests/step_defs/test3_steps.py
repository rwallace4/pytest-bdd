from pytest_bdd import scenario, given, when, then,

@given("the application is asking for user input")
def step_impl():
    raise NotImplementedError(u'Given the application is asking for user input')

@when("the 'month of birth' is entered as 15")
def step_impl():
    raise NotImplementedError(u'STEP: When the "month of birth" is entered as 15')

@then("the screen should show an error message")
def step_impl():
    raise NotImplementedError(u'STEP: Then the screen should show an error message')