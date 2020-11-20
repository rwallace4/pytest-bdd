Feature: Utilizing Retirement Calculator
As a user, entering scenarios into the retirement calculator

Scenario: Entering data into the retirement calculator
	Given the application is asking for user input
	When the 'year of birth' is entered as "1910"
	Then the screen should prompt for the birth month next