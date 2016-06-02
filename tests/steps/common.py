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

from pytest_bdd import given

from support.util import config


@given("I'm a logged in user")
def logged_in_user(browser):
    browser.visit(config['DEFAULT']['url'])
    login = browser.find_by_value('Login')
    if login:
        browser.fill('username', config['DEFAULT']['username'])
        browser.fill('password', config['DEFAULT']['password'])
        login.click()
    else:
        browser.find_link_by_href('/plinth/firstboot/state1/').first.click()
        browser.fill('username', config['DEFAULT']['username'])
        browser.find_by_id('id_password1').fill(config['DEFAULT']['password'])
        browser.find_by_id('id_password2').fill(config['DEFAULT']['password'])
        browser.find_by_value('Box it up!').click()
