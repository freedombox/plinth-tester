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

# unlisted apps just use the app_name as module name
app_module = {
    'ntp': 'datetime',
    'wiki': 'ikiwiki',
    'tt-rss': 'ttrss',
}

app_checkbox_id = {
    'tor': 'id_tor-enabled',
}

app_config_updating_text = {
    'tor': 'Tor configuration is being updated',
}


def get_app_module(app_name):
    module = app_name
    if app_name in app_module:
        module = app_module[app_name]
    return module


def get_app_checkbox_id(app_name):
    checkbox_id = 'id_is_enabled'
    if app_name in app_checkbox_id:
        checkbox_id = app_checkbox_id[app_name]
    return checkbox_id


def install(browser, app_name):
    interface.nav_to_module(browser, get_app_module(app_name))
    install = browser.find_by_value('Install')
    if install:
        install.click()
        while browser.is_text_present('Installing') \
              or browser.is_text_present('Performing post-install operation'):
            sleep(1)
        sleep(2)


def _change_status(browser, app_name, change_status_to='enabled'):
    interface.nav_to_module(browser, get_app_module(app_name))
    checkbox = browser.find_by_id(get_app_checkbox_id(app_name))
    checkbox.check() if change_status_to == 'enabled' else checkbox.uncheck()
    browser.find_by_value('Update setup').click()
    if app_name == app_config_updating_text:
        wait_for_config_update(browser, app_name)


def enable(browser, app_name):
    _change_status(browser, app_name, 'enabled')


def disable(browser, app_name):
    _change_status(browser, app_name, 'disabled')


def wait_for_config_update(browser, app_name):
    while browser.is_text_present(app_config_updating_text['tor']):
        sleep(1)
