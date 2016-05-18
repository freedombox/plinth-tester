Feature: Users and Groups
    Manage users and groups.

Scenario: Delete user
    Given I'm a logged in user
    Given the user alice exists
    When I go to the Users and Groups page
    And I press the delete user button for alice
    And I confirm to delete the user alice
    And I go to the Users tab
    Then alice should not be listed as a user
