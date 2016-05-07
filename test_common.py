import configparser
from pytest_bdd import given


config = configparser.ConfigParser()
config.read('config.ini')


@given("I'm a logged in user")
def logged_in_user(browser):
    browser.visit(config['DEFAULT']['url'])
    first_boot = browser.find_link_by_href('/plinth/firstboot/state1/')
    if first_boot:
        first_boot.first.click()
        browser.fill('username', config['DEFAULT']['username'])
        browser.find_by_id('id_password1').fill(config['DEFAULT']['password'])
        browser.find_by_id('id_password2').fill(config['DEFAULT']['password'])
        browser.find_by_value('Box it up!').click()
    else:
        browser.fill('username', config['DEFAULT']['username'])
        browser.fill('password', config['DEFAULT']['password'])
        browser.find_by_value('Login').click()
