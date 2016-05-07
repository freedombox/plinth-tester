import configparser
from pytest_bdd import given


config = configparser.ConfigParser()
config.read('config.ini')


@given("I'm a logged in user")
def logged_in_user(browser):
    browser.visit(config['DEFAULT']['url'])
    browser.fill('username', config['DEFAULT']['username'])
    browser.fill('password', config['DEFAULT']['password'])
    browser.find_by_value('Login').click()
