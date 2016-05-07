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

import configparser
from pytest_bdd import scenario, when, then

from test_common import *


config = configparser.ConfigParser()
config.read('config.ini')


@scenario('change_hostname.feature', 'Change hostname')
def test_change_hostname():
    pass


@scenario('change_domain_name.feature', 'Change domain name')
def test_change_domain_name():
    pass


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
