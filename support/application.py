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

from time import sleep

from support import interface


app_module = {
    'xmpp': 'xmpp',
    'wiki': 'ikiwiki',
}


def install(browser, app_name):
    interface.nav_to_apps_module(browser, app_module[app_name])
    install = browser.find_by_value('Install')
    if install:
        install.click()
        while browser.is_text_present('Installing'):
            sleep(1)
        sleep(2)


def enable(browser, app_name):
    interface.nav_to_apps_module(browser, app_module[app_name])
    browser.find_by_id('id_is_enabled').check()
    browser.find_by_value('Update setup').click()


def disable(browser, app_name):
    interface.nav_to_apps_module(browser, app_module[app_name])
    browser.find_by_id('id_is_enabled').uncheck()
    browser.find_by_value('Update setup').click()
