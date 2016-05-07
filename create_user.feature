Feature: Users and Groups
    Manage users and groups.

Scenario: Create user
    Given I'm a logged in user
    Given the new user doesn't exist
    When I go to the Users and Groups page
    And I go to the Create User tab
    And I fill in a username
    And I fill in a password
    And I fill in a password confirmation
    And I press the create user button
    And I go to the Users tab
    Then the new user should be listed
