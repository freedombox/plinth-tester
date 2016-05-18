Feature: Configuration
    Configure the system.

Scenario: Change language to Danish
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Danish language
    And I press the Submit button
    Then the Configuration page title should be in Danish

Scenario: Change language to German
    Given I'm a logged in user
    When I go to the Configuration page
    And I select German language
    And I press the Submit button
    Then the Configuration page title should be in German

Scenario: Change language to Spanish
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Spanish language
    And I press the Submit button
    Then the Configuration page title should be in Spanish

Scenario: Change language to French
    Given I'm a logged in user
    When I go to the Configuration page
    And I select French language
    And I press the Submit button
    Then the Configuration page title should be in French

Scenario: Change language to Italian
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Italian language
    And I press the Submit button
    Then the Configuration page title should be in Italian

Scenario: Change language to Norwegian Bokmål
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Norwegian Bokmål language
    And I press the Submit button
    Then the Configuration page title should be in Norwegian Bokmål

Scenario: Change language to Dutch
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Dutch language
    And I press the Submit button
    Then the Configuration page title should be in Dutch

Scenario: Change language to Polish
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Polish language
    And I press the Submit button
    Then the Configuration page title should be in Polish

Scenario: Change language to Portuguese
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Portuguese language
    And I press the Submit button
    Then the Configuration page title should be in Portuguese

Scenario: Change language to Russian
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Russian language
    And I press the Submit button
    Then the Configuration page title should be in Russian

Scenario: Change language to Swedish
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Swedish language
    And I press the Submit button
    Then the Configuration page title should be in Swedish

Scenario: Change language to Telugu
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Telugu language
    And I press the Submit button
    Then the Configuration page title should be in Telugu

Scenario: Change language to Turkish
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Turkish language
    And I press the Submit button
    Then the Configuration page title should be in Turkish

Scenario: Change language to Simplified Chinese
    Given I'm a logged in user
    When I go to the Configuration page
    And I select Simplified Chinese language
    And I press the Submit button
    Then the Configuration page title should be in Simplified Chinese
