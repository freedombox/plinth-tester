#
# This file is part of Plinth-tester.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

Feature: Configuration
  Configure the system.

Scenario: Change hostname
  Given I'm a logged in user
  When I change the hostname to mybox
  Then the hostname should be mybox

Scenario: Change domain name
  Given I'm a logged in user
  When I change the domain name to mydomain
  Then the domain name should be mydomain

Scenario: Change language to Danish
  Given I'm a logged in user
  When I change the language to Danish
  Then Plinth language should be Danish

Scenario: Change language to German
  Given I'm a logged in user
  When I change the language to German
  Then Plinth language should be German

Scenario: Change language to Spanish
  Given I'm a logged in user
  When I change the language to Spanish
  Then Plinth language should be Spanish

Scenario: Change language to French
  Given I'm a logged in user
  When I change the language to French
  Then Plinth language should be French

Scenario: Change language to Italian
  Given I'm a logged in user
  When I change the language to Italian
  Then Plinth language should be Italian

Scenario: Change language to Norwegian Bokmål
  Given I'm a logged in user
  When I change the language to Norwegian Bokmål
  Then Plinth language should be Norwegian Bokmål

Scenario: Change language to Dutch
  Given I'm a logged in user
  When I change the language to Dutch
  Then Plinth language should be Dutch

Scenario: Change language to Polish
  Given I'm a logged in user
  When I change the language to Polish
  Then Plinth language should be Polish

Scenario: Change language to Portuguese
  Given I'm a logged in user
  When I change the language to Portuguese
  Then Plinth language should be Portuguese

Scenario: Change language to Russian
  Given I'm a logged in user
  When I change the language to Russian
  Then Plinth language should be Russian

Scenario: Change language to Swedish
  Given I'm a logged in user
  When I change the language to Swedish
  Then Plinth language should be Swedish

Scenario: Change language to Telugu
  Given I'm a logged in user
  When I change the language to Telugu
  Then Plinth language should be Telugu

Scenario: Change language to Turkish
  Given I'm a logged in user
  When I change the language to Turkish
  Then Plinth language should be Turkish

Scenario: Change language to Simplified Chinese
  Given I'm a logged in user
  When I change the language to Simplified Chinese
  Then Plinth language should be Simplified Chinese
