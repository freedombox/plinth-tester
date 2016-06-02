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

from pytest_bdd import parsers, given, when, then

from support import interface


@given(parsers.parse("the user {name:w} doesn't exist"))
def new_user_does_not_exist(browser, name):
    interface.nav_to_sys_module(browser, 'users')
    delete_link = browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/delete/')
    if delete_link:
        delete_link.first.click()
        browser.find_by_value(
            'Delete ' + name).click()


@given(parsers.parse('the user {name:w} exists'))
def test_user_exists(browser, name):
    interface.nav_to_sys_module(browser, 'users')
    user_link = browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/edit/')
    if not user_link:
        create_user(browser, name, 'secret')


@when('I go to the Users and Groups page')
def go_to_users_and_groups(browser):
    interface.nav_to_sys_module(browser, 'users')


@when(parsers.parse(
    'I create a user named {name:w} with password {password:w}'))
def create_user(browser, name, password):
    interface.nav_to_sys_module(browser, 'users')
    browser.find_link_by_href('/plinth/sys/users/create/').first.click()
    browser.find_by_id('id_username').fill(name)
    browser.find_by_id('id_password1').fill(password)
    browser.find_by_id('id_password2').fill(password)
    browser.find_by_value('Create User').click()


@when(parsers.parse('I rename the user {old_name:w} to {new_name:w}'))
def rename_user(browser, old_name, new_name):
    interface.nav_to_sys_module(browser, 'users')
    browser.find_link_by_href(
        '/plinth/sys/users/' + old_name + '/edit/').first.click()
    browser.find_by_id('id_username').fill(new_name)
    browser.find_by_value('Save Changes').click()


@when(parsers.parse('I delete the user {name:w}'))
def delete_user(browser, name):
    interface.nav_to_sys_module(browser, 'users')
    browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/delete/').first.click()
    browser.find_by_value('Delete ' + name).click()


@then(parsers.parse('{name:w} should be listed as a user'))
def new_user_is_listed(browser, name):
    interface.nav_to_sys_module(browser, 'users')
    assert browser.is_text_present(name)


@then(parsers.parse('{name:w} should not be listed as a user'))
def new_user_is_not_listed(browser, name):
    interface.nav_to_sys_module(browser, 'users')
    assert not browser.is_text_present(name)
