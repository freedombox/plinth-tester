Feature: Users and Groups
    Manage users and groups.

Scenario: Create user
    Given I'm a logged in user
    Given the user alice doesn't exist
    When I go to the Users and Groups page
    And I go to the Create User tab
    And I fill in alice for the username
    And I fill in secret for the password
    And I fill in secret for the password confirmation
    And I press the create user button
    And I go to the Users tab
    Then alice should be listed as a user
