import configparser
from pytest_bdd import scenario, when, then

from test_common import *


config = configparser.ConfigParser()
config.read('config.ini')


@scenario('create_user.feature', 'Create user')
def test_create_user():
    pass


@given("the new user doesn't exist")
def new_user_does_not_exist(browser):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/users/').first.click()
    delete_link = browser.find_link_by_href(
        '/plinth/sys/users/' + config['UsersAndGroups']['username'] \
        + '/delete/')
    if delete_link:
        delete_link.first.click()
        browser.find_by_value(
            'Delete ' + config['UsersAndGroups']['username']).click()


@when('I go to the Users and Groups page')
def go_to_users_and_groups(browser):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/users/').first.click()


@when('I go to the Create User tab')
def go_to_create_user(browser):
    browser.find_link_by_href('/plinth/sys/users/create/').first.click()


@when('I fill in a username')
def fill_username(browser):
    browser.find_by_id('id_username').fill(
        config['UsersAndGroups']['username'])


@when('I fill in a password')
def fill_password(browser):
    browser.find_by_id('id_password1').fill(
        config['UsersAndGroups']['password'])


@when('I fill in a password confirmation')
def fill_password_confirmation(browser):
    browser.find_by_id('id_password2').fill(
        config['UsersAndGroups']['password'])


@when('I press the create user button')
def create_user(browser):
    browser.find_by_value('Create User').click()


@when('I go to the Users tab')
def go_to_create_user(browser):
    browser.find_link_by_href('/plinth/sys/users/').first.click()


@then('the new user should be listed')
def new_user_is_listed(browser):
    assert browser.is_text_present(config['UsersAndGroups']['username'])
