Feature: Configuration
    Configure the system.

Scenario: Change hostname
    Given I'm a logged in user
    When I go to the Configuration page
    And I fill in a hostname
    And I press the submit button
    Then the hostname should match the new value
