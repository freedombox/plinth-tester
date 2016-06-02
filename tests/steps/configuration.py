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

from support import nav_to_sys_module, submit


@when('I go to the Configuration page')
def go_to_configuration(browser):
    nav_to_sys_module(browser, 'config')


@when(parsers.parse('I change the hostname to {hostname:w}'))
def change_hostname(browser, hostname):
    browser.find_by_id('id_configuration-hostname').fill(hostname)
    submit(browser)


@when(parsers.parse('I change the domain name to {domain:w}'))
def change_domain_name(browser, domain):
    browser.find_by_id('id_configuration-domainname').fill(domain)
    submit(browser)


def select_language(browser, language_code):
    browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="' \
        + language_code + '"]'
    ).first.click()


@when('I change the language to Danish')
def change_language_to_danish(browser):
    select_language(browser, 'da')
    submit(browser)


@when('I change the language to German')
def change_language_to_german(browser):
    select_language(browser, 'de')
    submit(browser)


@when('I change the language to Spanish')
def change_language_to_spanish(browser):
    select_language(browser, 'es')
    submit(browser)


@when('I change the language to French')
def change_language_to_french(browser):
    select_language(browser, 'fr')
    submit(browser)


@when('I change the language to Italian')
def change_language_to_italian(browser):
    select_language(browser, 'it')
    submit(browser)


@when('I change the language to Norwegian Bokmål')
def change_language_to_norwegian_bokmål(browser):
    select_language(browser, 'nb')
    submit(browser)


@when('I change the language to Dutch')
def change_language_to_dutch(browser):
    select_language(browser, 'nl')
    submit(browser)


@when('I change the language to Polish')
def change_language_to_polish(browser):
    select_language(browser, 'pl')
    submit(browser)


@when('I change the language to Portuguese')
def change_language_to_portuguese(browser):
    select_language(browser, 'pt')
    submit(browser)


@when('I change the language to Russian')
def change_language_to_russian(browser):
    select_language(browser, 'ru')
    submit(browser)


@when('I change the language to Swedish')
def change_language_to_swedish(browser):
    select_language(browser, 'sv')
    submit(browser)


@when('I change the language to Telugu')
def change_language_to_telugu(browser):
    select_language(browser, 'te')
    submit(browser)


@when('I change the language to Turkish')
def change_language_to_turkish(browser):
    select_language(browser, 'tr')
    submit(browser)


@when('I change the language to Simplified Chinese')
def change_language_to_simplified_chinese(browser):
    select_language(browser, 'zh-hans')
    submit(browser)


@then(parsers.parse('the hostname should be {hostname:w}'))
def hostname_should_be(browser, hostname):
    assert(browser.find_by_id('id_configuration-hostname').value == hostname)


@then(parsers.parse('the domain name should be {domain:w}'))
def domain_name_should_be(browser, domain):
    assert(browser.find_by_id('id_configuration-domainname').value == domain)


@then('Plinth language should be Danish')
def plinth_language_should_be_danish(browser):
    assert(browser.title == 'Generel Konfiguration')


@then('Plinth language should be German')
def plinth_language_should_be_german(browser):
    assert(browser.title == 'Allgemeine Konfiguration')


@then('Plinth language should be Spanish')
def plinth_language_should_be_spanish(browser):
    assert(browser.title == 'Configuración general')


@then('Plinth language should be French')
def plinth_language_should_be_french(browser):
    assert(browser.title == 'Configuration générale')


@then('Plinth language should be Italian')
def plinth_language_should_be_italian(browser):
    assert(browser.title == 'General Configuration')


@then('Plinth language should be Norwegian Bokmål')
def plinth_language_should_be_norwegian_bokmål(browser):
    assert(browser.title == 'Generelt oppsett')


@then('Plinth language should be Dutch')
def plinth_language_should_be_dutch(browser):
    assert(browser.title == 'Algemene Instellingen')


@then('Plinth language should be Polish')
def plinth_language_should_be_polish(browser):
    assert(browser.title == 'Ustawienia główne')


@then('Plinth language should be Portuguese')
def plinth_language_should_be_portuguese(browser):
    assert(browser.title == 'Configuração Geral')


@then('Plinth language should be Russian')
def plinth_language_should_be_russian(browser):
    assert(browser.title == 'Общие настройки')


@then('Plinth language should be Swedish')
def plinth_language_should_be_swedish(browser):
    assert(browser.title == 'Allmän Konfiguration')


@then('Plinth language should be Telugu')
def plinth_language_should_be_telugu(browser):
    assert(browser.title == 'సాధారణ ఆకృతీకరణ')


@then('Plinth language should be Turkish')
def plinth_language_should_be_turkish(browser):
    assert(browser.title == 'Genel Yapılandırma')


@then('Plinth language should be Simplified Chinese')
def plinth_language_should_be_simplified_chinese(browser):
    assert(browser.title == '常规配置')
