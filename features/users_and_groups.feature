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
    And I press the Create User button
    And I go to the Users tab
    Then alice should be listed as a user

Scenario: Rename user
    Given I'm a logged in user
    Given the user alice exists
    Given the user bob doesn't exist
    When I go to the Users and Groups page
    And I select the user alice
    And I fill in bob for the username
    And I press the Save Changes button
    And I go to the Users tab
    Then alice should not be listed as a user
    Then bob should be listed as a user

Scenario: Delete user
    Given I'm a logged in user
    Given the user alice exists
    When I go to the Users and Groups page
    And I press the delete user button for alice
    And I confirm to delete the user alice
    And I go to the Users tab
    Then alice should not be listed as a user
