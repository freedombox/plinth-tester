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

Feature: Users and Groups
  Manage users and groups.

Scenario: Create user
  Given I'm a logged in user
  Given the user alice doesn't exist
  When I go to the Users and Groups page
  And I create a user named alice with password secret
  Then alice should be listed as a user

Scenario: Rename user
  Given I'm a logged in user
  Given the user alice exists
  Given the user bob doesn't exist
  When I go to the Users and Groups page
  And I rename the user alice to bob
  Then alice should not be listed as a user
  Then bob should be listed as a user

Scenario: Delete user
  Given I'm a logged in user
  Given the user alice exists
  When I go to the Users and Groups page
  And I delete the user alice
  Then alice should not be listed as a user
