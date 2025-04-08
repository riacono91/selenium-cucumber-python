Feature: Login functionality and alert handling new link page

  Scenario: Login with valid credentials and handle alert
    Given I open the login page of a new link
    When I enter valid credentials of a new link
    And I submit the login form
    Then I should see the alert with the message "You logged into a secure area!"

  Scenario: Submit login form with empty fields
    Given I open the login page of a new link
    When I submit the login form
    Then I should see the alert with the message "Your username is invalid!"

  Scenario Outline: Login with invalid credentials
    Given I open the login page of a new link
    When I enter username "<username>" and password "<password>"
    And I submit the login form
    Then I should see the alert with the message "Your username is invalid!"

  Examples:
    | username   | password     |
    | wronguser  | password123  |
    | testuser   | wrongpass    |
    | wronguser  | wrongpass    |


  Scenario: Login with invalid username
    Given I open the login page of a new link
    When I enter username "invalidusername" and password "SuperSecretPassword"
    And I submit the login form
    Then I should see the alert with the message "Your username is invalid!"