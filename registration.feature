## Registration Feature File 

Feature: Password must be at least 6 characters long with at least one number and at least one special character


Scenario: Registration password will meet all acceptance criteria for the moneygaming registration
    Given I am on the registration form page
    When I type 'password1@' in the password field
    And I click on the 'Submit' button
    Then get a successful login message on the homescreen
    

Scenario: Registration password will not meet any of the the acceptance criteria for moneygaming registration 
    Given I am on the registration page
    When I type 'passw' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message 
    And I will not be able to register for moneygaming

Scenario: Registration will meet the 6 character criteria, but not the number and special character 
    Given I am on the registration page
    When I type 'password' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will meet the 6 character and the number criteria, but not the special character 
    Given I am on the registration page
    when I type 'password1' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will meet the 6 character and the special character criteria, but not the number 
    Given I am on the registration page
    when I type 'password!' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will not meet the 6 character and number criteria, but will meet the special character criteria
    Given I am on the registration page
    when I type 'pw@' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will not meet the 6 digit and special character criteria, but will meet the number criteria 
    Given I am on the registration page
    when I type 'pw7' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will Not meet the 6 character criteria, but will meet the number and special character criteria
    Given I am on the registration page
    when I type 'pw7@' in the password field
    And I click on the 'Submit' button
    Then I will get an 'Invalid Password' message
    And I will not be able to register for moneygaming

Scenario: Registration password will be left blank
    Given I am on the registration page
    when I type '' in the password field
    And I click on the 'Submit' button
    Then I will get an 'This field is required' message
    And I will not be able to register for moneygaming

