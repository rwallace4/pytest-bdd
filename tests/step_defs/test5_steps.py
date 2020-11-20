from pytest_bdd import scenario, given, when, then,

@given("the application is asking for user input")
def step_impl():
    raise NotImplementedError(u'Given the application is asking for user input')

@when("the 'birth year' is entered as 1910 and the 'birth month' is 4")
def step_impl():
    raise NotImplementedError(u'STEP: 	When the "birth year" is entered as 1910 and the "birth month" is 4')

@then("the retirement age should be calculated")
def step_impl():
    raise NotImplementedError(u'STEP: Then the retirement age should be calculated')