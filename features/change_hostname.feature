Feature: Configuration
    Configure the system.

Scenario: Change hostname
    Given I'm a logged in user
    When I go to the Configuration page
    And I fill in mybox for the hostname
    And I press the Submit button
    Then the hostname should be mybox
