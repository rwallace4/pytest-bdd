Feature: Utilizing Retirement Calculator
As a user, entering scenarios into the retirement calculator

Scenario: Entering data into the retirement calculator
	Given the application is asking for user input
	When the "month of birth" is entered as 15
	Then the screen should show an error message
