import configparser
from pytest_bdd import scenario, given, when, then


config = configparser.ConfigParser()
config.read('config.ini')


@scenario('change_hostname.feature', 'Change hostname')
def test_change_hostname():
    pass


@scenario('change_domain_name.feature', 'Change domain name')
def test_change_domain_name():
    pass


@given("I'm a logged in user")
def logged_in_user(browser):
    browser.visit(config['DEFAULT']['url'])
    browser.fill('username', config['DEFAULT']['username'])
    browser.fill('password', config['DEFAULT']['password'])
    browser.find_by_value('Login').click()


@when('I go to the Configuration page')
def go_to_configuration(browser):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/config/').first.click()


@when('I fill in a hostname')
def fill_hostname(browser):
    browser.find_by_id('id_configuration-hostname').fill(
        config['Configuration']['hostname'])


@when('I fill in a domain name')
def fill_hostname(browser):
    browser.find_by_id('id_configuration-domainname').fill(
        config['Configuration']['domainname'])


@when('I press the submit button')
def submit_form(browser):
    browser.find_by_value('Submit').click()


@then('the hostname should match the new value')
def hostname_is_new_value(browser):
    assert(browser.find_by_id('id_configuration-hostname').value \
           == config['Configuration']['hostname'])


@then('the domain name should match the new value')
def domain_name_is_new_value(browser):
    assert(browser.find_by_id('id_configuration-domainname').value \
           == config['Configuration']['domainname'])
