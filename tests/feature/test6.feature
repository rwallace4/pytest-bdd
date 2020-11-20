Feature: Utilizing Retirement Calculator
As a user, entering scenarios into the retirement calculator

Scenario: Entering data into the retirement calculator
	Given the application is asking for user input
	When the "birth year" is entered as 2000 and the "birth month" is 1
	Then the retirement age should be calculated
	And displayed on the screen as 67 and 0 months, in January of 2067