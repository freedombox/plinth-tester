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

from pytest_bdd import scenario

from steps.common import *
from steps.users_and_groups import *
from support.util import feature


@scenario(feature('users_and_groups'), 'Create user')
def test_create_user():
    pass


@scenario(feature('users_and_groups'), 'Rename user')
def test_rename_user():
    pass


@scenario(feature('users_and_groups'), 'Delete user')
def test_delete_user():
    pass
