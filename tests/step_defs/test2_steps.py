from pytest_bdd import scenario, given, when, then,

@given("the application is asking for user input")
def step_impl():
    raise NotImplementedError(u'Given the application is asking for user input')

@when("the 'year of birth' is entered as 1910")
def step_impl():
    raise NotImplementedError(u'STEP: 	When the "year of birth" is entered as 1910')

@then("the screen should prompt for the birth month next")
def step_impl():
    raise NotImplementedError(u'STEP: Then the screen should prompt for the birth month next')