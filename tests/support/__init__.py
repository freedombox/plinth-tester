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


config = configparser.ConfigParser()
config.read('config.ini')


def feature(name):
    return '../features/' + name + '.feature'


def login(browser, url, username, password):
    browser.visit(url)
    login = browser.find_by_value('Login')
    if login:
        browser.fill('username', username)
        browser.fill('password', password)
        login.click()
    else:
        browser.find_link_by_href('/plinth/firstboot/state1/').first.click()
        browser.fill('username', username)
        browser.find_by_id('id_password1').fill(password)
        browser.find_by_id('id_password2').fill(password)
        browser.find_by_value('Box it up!').click()


def nav_to_sys_module(browser, module):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/' + module + '/').first.click()


def submit(browser):
    browser.find_by_value('Submit').click()
