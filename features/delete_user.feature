Feature: Users and Groups
    Manage users and groups.

Scenario: Delete user
    Given I'm a logged in user
    Given the test user exists
    When I go to the Users and Groups page
    And I press the delete user button
    And I confirm to delete the user
    And I go to the Users tab
    Then the test user should not be listed
