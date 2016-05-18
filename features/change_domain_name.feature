Feature: Configuration
    Configure the system.

Scenario: Change domain name
    Given I'm a logged in user
    When I go to the Configuration page
    And I fill in mydomain for the domain name
    And I press the Submit button
    Then the domain name should be mydomain
