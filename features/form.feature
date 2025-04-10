Feature: Interact with form fields (input, dropdown, radio)

  Scenario: Successful login form submission
    Given I open the login page
    When I enter valid credentials
    And I submit the form
    Then I should see the confirmation message "Form submitted"

  Scenario: Enter text in the input field
    Given I open the login page
    When I enter "Hello, Selenium!" in the text field
    And I submit the form
    Then I should see the confirmation message "Form submitted"

  Scenario: Select an option from the dropdown
    Given I open the login page
    When I select "Two" from the dropdown
    And I submit the form
    Then I should see the confirmation message "Form submitted"

  Scenario: Click on a radio button
    Given I open the login page
    When I select the radio button "Default radio"
    And I submit the form
    Then I should see the confirmation message "Form submitted"
