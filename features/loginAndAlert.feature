Feature: Login functionality and alert handling new link page

  Scenario: Login with valid credentials and handle alert
    Given I open the login page of a new link
    When I enter valid credentials of a new link
    And I submit the login form
    Then I should see the alert with the message "You logged into a secure area!"
