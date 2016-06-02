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

from pytest_bdd import parsers, when, then

from support import system


@when(parsers.parse('I change the hostname to {hostname:w}'))
def change_hostname_to(browser, hostname):
    system.set_hostname(browser, hostname)


@when(parsers.parse('I change the domain name to {domain:w}'))
def change_domain_name_to(browser, domain):
    system.set_domain_name(browser, domain)


@when('I change the language to Danish')
def change_language_to_danish(browser):
    system.set_language(browser, 'da')


@when('I change the language to German')
def change_language_to_german(browser):
    system.set_language(browser, 'de')


@when('I change the language to Spanish')
def change_language_to_spanish(browser):
    system.set_language(browser, 'es')


@when('I change the language to French')
def change_language_to_french(browser):
    system.set_language(browser, 'fr')


@when('I change the language to Norwegian Bokmål')
def change_language_to_norwegian_bokmål(browser):
    system.set_language(browser, 'nb')


@when('I change the language to Dutch')
def change_language_to_dutch(browser):
    system.set_language(browser, 'nl')


@when('I change the language to Polish')
def change_language_to_polish(browser):
    system.set_language(browser, 'pl')


@when('I change the language to Portuguese')
def change_language_to_portuguese(browser):
    system.set_language(browser, 'pt')


@when('I change the language to Russian')
def change_language_to_russian(browser):
    system.set_language(browser, 'ru')


@when('I change the language to Swedish')
def change_language_to_swedish(browser):
    system.set_language(browser, 'sv')


@when('I change the language to Telugu')
def change_language_to_telugu(browser):
    system.set_language(browser, 'te')


@when('I change the language to Turkish')
def change_language_to_turkish(browser):
    system.set_language(browser, 'tr')


@when('I change the language to Simplified Chinese')
def change_language_to_simplified_chinese(browser):
    system.set_language(browser, 'zh-hans')


@then(parsers.parse('the hostname should be {hostname:w}'))
def hostname_should_be(browser, hostname):
    assert(system.get_hostname(browser) == hostname)


@then(parsers.parse('the domain name should be {domain:w}'))
def domain_name_should_be(browser, domain):
    assert(system.get_domain_name(browser) == domain)


@then('Plinth language should be Danish')
def plinth_language_should_be_danish(browser):
    assert(system.check_language(browser, 'da') == True)


@then('Plinth language should be German')
def plinth_language_should_be_german(browser):
    assert(system.check_language(browser, 'de') == True)


@then('Plinth language should be Spanish')
def plinth_language_should_be_spanish(browser):
    assert(system.check_language(browser, 'es') == True)


@then('Plinth language should be French')
def plinth_language_should_be_french(browser):
    assert(system.check_language(browser, 'fr') == True)


@then('Plinth language should be Norwegian Bokmål')
def plinth_language_should_be_norwegian_bokmål(browser):
    assert(system.check_language(browser, 'nb') == True)


@then('Plinth language should be Dutch')
def plinth_language_should_be_dutch(browser):
    assert(system.check_language(browser, 'nl') == True)


@then('Plinth language should be Polish')
def plinth_language_should_be_polish(browser):
    assert(system.check_language(browser, 'pl') == True)


@then('Plinth language should be Portuguese')
def plinth_language_should_be_portuguese(browser):
    assert(system.check_language(browser, 'pt') == True)


@then('Plinth language should be Russian')
def plinth_language_should_be_russian(browser):
    assert(system.check_language(browser, 'ru') == True)


@then('Plinth language should be Swedish')
def plinth_language_should_be_swedish(browser):
    assert(system.check_language(browser, 'sv') == True)


@then('Plinth language should be Telugu')
def plinth_language_should_be_telugu(browser):
    assert(system.check_language(browser, 'te') == True)


@then('Plinth language should be Turkish')
def plinth_language_should_be_turkish(browser):
    assert(system.check_language(browser, 'tr') == True)


@then('Plinth language should be Simplified Chinese')
def plinth_language_should_be_simplified_chinese(browser):
    assert(system.check_language(browser, 'zh-hans') == True)
