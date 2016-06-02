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

from pytest_bdd import scenario

from steps.common import *
from steps.configuration import *
from support import feature


@scenario(feature('configuration'), 'Change hostname')
def test_change_hostname():
    pass


@scenario(feature('configuration'), 'Change domain name')
def test_change_domain_name():
    pass


@scenario(feature('configuration'), 'Change language to Danish')
def test_change_language_to_danish():
    pass


@scenario(feature('configuration'), 'Change language to German')
def test_change_language_to_german():
    pass


@scenario(feature('configuration'), 'Change language to Spanish')
def test_change_language_to_spanish():
    pass


@scenario(feature('configuration'), 'Change language to French')
def test_change_language_to_french():
    pass


@scenario(feature('configuration'), 'Change language to Norwegian Bokmål')
def test_change_language_to_norwegian_bokmål():
    pass


@scenario(feature('configuration'), 'Change language to Dutch')
def test_change_language_to_dutch():
    pass


@scenario(feature('configuration'), 'Change language to Polish')
def test_change_language_to_polish():
    pass


@scenario(feature('configuration'), 'Change language to Portuguese')
def test_change_language_to_portuguese():
    pass


@scenario(feature('configuration'), 'Change language to Russian')
def test_change_language_to_russian():
    pass


@scenario(feature('configuration'), 'Change language to Swedish')
def test_change_language_to_swedish():
    pass


@scenario(feature('configuration'), 'Change language to Telugu')
def test_change_language_to_telugu():
    pass


@scenario(feature('configuration'), 'Change language to Turkish')
def test_change_language_to_turkish():
    pass


@scenario(feature('configuration'), 'Change language to Simplified Chinese')
def test_change_language_to_simplified_chinese():
    pass
