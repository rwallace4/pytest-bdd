from pytest_bdd import scenario, given, when, then,

@given("the application is asking for user input")
def step_impl():
    raise NotImplementedError(u'Given the application is asking for user input')

@when("the 'birth year; is entered as 2000 and the 'birth month' is 1")
def step_impl():
    raise NotImplementedError(u'STEP: When the "birth year" is entered as 2000 and the "birth month" is 1')

@then("the retirement age should be calculated")
def step_impl():
    raise NotImplementedError(u'STEP: the retirement age should be calculated')