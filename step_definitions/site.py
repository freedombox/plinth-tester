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

from pytest_bdd import parsers, then

from support import site


@then(parsers.parse('the {site_name:w} site should be available'))
def site_should_be_available(browser, site_name):
    assert site.is_available(browser, site_name)


@then(parsers.parse('the {site_name:w} site should not be available'))
def site_should_not_be_available(browser, site_name):
    assert not site.is_available(browser, site_name)
