Feature: Login Functionality

  Scenario: Successful login form submission
    Given I open the login page
    When I enter valid credentials
    And I submit the form
    Then I should see the confirmation message "Form submitted"
