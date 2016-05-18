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

from pytest_bdd import scenario, parsers, given, when, then

from test_common import *


@scenario(feature('create_user'), 'Create user')
def test_create_user():
    pass


@scenario(feature('rename_user'), 'Rename user')
def test_rename_user():
    pass


@scenario(feature('delete_user'), 'Delete user')
def test_delete_user():
    pass


@given(parsers.parse("the user {name:w} doesn't exist"))
def new_user_does_not_exist(browser, name):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/users/').first.click()
    delete_link = browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/delete/')
    if delete_link:
        delete_link.first.click()
        browser.find_by_value(
            'Delete ' + name).click()


@given(parsers.parse('the user {name:w} exists'))
def test_user_exists(browser, name):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/users/').first.click()
    user_link = browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/edit/')
    if not user_link:
        browser.find_link_by_href('/plinth/sys/users/create/').first.click()
        browser.find_by_id('id_username').fill(name)
        browser.find_by_id('id_password1').fill('secret')
        browser.find_by_id('id_password2').fill('secret')
        browser.find_by_value('Create User').click()


@when('I go to the Users and Groups page')
def go_to_users_and_groups(browser):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/users/').first.click()


@when('I go to the Users tab')
def go_to_create_user(browser):
    browser.find_link_by_href('/plinth/sys/users/').first.click()


@when(parsers.parse('I select the user {name:w}'))
def select_user(browser, name):
    browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/edit/').first.click()


@when('I press the Save Changes button')
def save_changes(browser, name):
    browser.find_by_value('Save Changes').click()


@when(parsers.parse('I press the delete user button for {name:w}'))
def delete_user(browser, name):
    browser.find_link_by_href(
        '/plinth/sys/users/' + name + '/delete/').first.click()


@when(parsers.parse('I confirm to delete the user {name:w}'))
def confirm_delete_user(browser, name):
    browser.find_by_value('Delete ' + name).click()


@when('I go to the Create User tab')
def go_to_create_user(browser):
    browser.find_link_by_href('/plinth/sys/users/create/').first.click()


@when(parsers.parse('I fill in {name:w} for the username'))
def fill_username(browser, name):
    browser.find_by_id('id_username').fill(name)


@when(parsers.parse('I fill in {password:w} for the password'))
def fill_password(browser, password):
    browser.find_by_id('id_password1').fill(password)


@when(parsers.parse(
    'I fill in {password:w} for the password confirmation'))
def fill_password_confirmation(browser, password):
    browser.find_by_id('id_password2').fill(password)


@when('I press the Create User button')
def create_user(browser):
    browser.find_by_value('Create User').click()


@then(parsers.parse('{name:w} should be listed as a user'))
def new_user_is_listed(browser, name):
    assert browser.is_text_present(name)


@then(parsers.parse('{name:w} should not be listed as a user'))
def new_user_is_listed(browser, name):
    assert not browser.is_text_present(name)
