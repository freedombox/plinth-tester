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

from support import config


# unlisted sites just use '/' + site_name as url
site_url = {
    'wiki': '/ikiwiki',
}


def get_site_url(site_name):
    url = '/' + site_name
    if site_name in site_url:
        url = site_url[site_name]
    return url


def is_available(browser, site_name):
    browser.visit(config['DEFAULT']['url'] + get_site_url(site_name))
    sleep(2)
    browser.reload()
    return browser.title != '404 Not Found'
