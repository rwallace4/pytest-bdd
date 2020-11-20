Feature: Utilizing Retirement Calculator
As a user, entering scenarios into the retirement calculator

Scenario: Entering data into the retirement calculator
	Given the application is asking for user input
	When the "year of birth" is entered as 1850
	Then the screen should show an error message
