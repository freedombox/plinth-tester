Feature: Users and Groups
    Manage users and groups.

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
