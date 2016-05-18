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

from pytest_bdd import scenario, parsers, when, then

from test_common import *


@scenario(feature('change_hostname'), 'Change hostname')
def test_change_hostname():
    pass


@scenario(feature('change_domain_name'), 'Change domain name')
def test_change_domain_name():
    pass


@scenario(feature('change_language'), 'Change language to Danish')
def test_change_language_to_danish():
    pass


@scenario(feature('change_language'), 'Change language to German')
def test_change_language_to_german():
    pass


@scenario(feature('change_language'), 'Change language to Spanish')
def test_change_language_to_spanish():
    pass


@scenario(feature('change_language'), 'Change language to French')
def test_change_language_to_french():
    pass


@scenario(feature('change_language'), 'Change language to Italian')
def test_change_language_to_italian():
    pass


@scenario(feature('change_language'), 'Change language to Norwegian Bokmål')
def test_change_language_to_norwegian_bokmål():
    pass


@scenario(feature('change_language'), 'Change language to Dutch')
def test_change_language_to_dutch():
    pass


@scenario(feature('change_language'), 'Change language to Polish')
def test_change_language_to_polish():
    pass


@scenario(feature('change_language'), 'Change language to Portuguese')
def test_change_language_to_portuguese():
    pass


@scenario(feature('change_language'), 'Change language to Russian')
def test_change_language_to_russian():
    pass


@scenario(feature('change_language'), 'Change language to Swedish')
def test_change_language_to_swedish():
    pass


@scenario(feature('change_language'), 'Change language to Telugu')
def test_change_language_to_telugu():
    pass


@scenario(feature('change_language'), 'Change language to Turkish')
def test_change_language_to_turkish():
    pass


@scenario(feature('change_language'), 'Change language to Simplified Chinese')
def test_change_language_to_simplified_chinese():
    pass


@when('I go to the Configuration page')
def go_to_configuration(browser):
    browser.find_link_by_href('/plinth/sys/').first.click()
    browser.find_link_by_href('/plinth/sys/config/').first.click()


@when(parsers.parse('I fill in {hostname:w} for the hostname'))
def fill_hostname(browser, hostname):
    browser.find_by_id('id_configuration-hostname').fill(hostname)


@when(parsers.parse('I fill in {domain:w} for the domain name'))
def fill_hostname(browser, domain):
    browser.find_by_id('id_configuration-domainname').fill(domain)


@when('I select Danish language')
def select_language_danish(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="da"]'
    ).first
    lang.click()


@when('I select German language')
def select_language_german(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="de"]'
    ).first
    lang.click()


@when('I select Spanish language')
def select_language_spanish(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="es"]'
    ).first
    lang.click()


@when('I select French language')
def select_language_french(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="fr"]'
    ).first
    lang.click()


@when('I select Italian language')
def select_language_italian(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="it"]'
    ).first
    lang.click()


@when('I select Norwegian Bokmål language')
def select_language_norwegian_bokmål(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="nb"]'
    ).first
    lang.click()


@when('I select Dutch language')
def select_language_dutch(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="nl"]'
    ).first
    lang.click()


@when('I select Polish language')
def select_language_polish(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="pl"]'
    ).first
    lang.click()


@when('I select Portuguese language')
def select_language_portuguese(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="pt"]'
    ).first
    lang.click()


@when('I select Russian language')
def select_language_russian(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="ru"]'
    ).first
    lang.click()


@when('I select Swedish language')
def select_language_swedish(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="sv"]'
    ).first
    lang.click()


@when('I select Telugu language')
def select_language_telugu(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="te"]'
    ).first
    lang.click()


@when('I select Turkish language')
def select_language_turkish(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="tr"]'
    ).first
    lang.click()


@when('I select Simplified Chinese language')
def select_language_simplified_chinese(browser):
    lang = browser.find_by_xpath(
        '//select[@id="id_configuration-language"]//option[@value="zh-hans"]'
    ).first
    lang.click()


@when('I press the Submit button')
def submit_form(browser):
    browser.find_by_value('Submit').click()


@then(parsers.parse('the hostname should be {hostname:w}'))
def hostname_is_new_value(browser, hostname):
    assert(browser.find_by_id('id_configuration-hostname').value == hostname)


@then(parsers.parse('the domain name should be {domain:w}'))
def domain_name_is_new_value(browser, domain):
    assert(browser.find_by_id('id_configuration-domainname').value == domain)


@then('the Configuration page title should be in Danish')
def configuration_page_title_is_in_danish(browser):
    assert(browser.title == 'Generel Konfiguration')


@then('the Configuration page title should be in German')
def configuration_page_title_is_in_german(browser):
    assert(browser.title == 'Allgemeine Konfiguration')


@then('the Configuration page title should be in Spanish')
def configuration_page_title_is_in_spanish(browser):
    assert(browser.title == 'Configuración general')


@then('the Configuration page title should be in French')
def configuration_page_title_is_in_french(browser):
    assert(browser.title == 'Configuration générale')


@then('the Configuration page title should be in Italian')
def configuration_page_title_is_in_italian(browser):
    assert(browser.title == 'General Configuration')


@then('the Configuration page title should be in Norwegian Bokmål')
def configuration_page_title_is_in_norwegian_bokmål(browser):
    assert(browser.title == 'Generelt oppsett')


@then('the Configuration page title should be in Dutch')
def configuration_page_title_is_in_dutch(browser):
    assert(browser.title == 'Algemene Instellingen')


@then('the Configuration page title should be in Polish')
def configuration_page_title_is_in_polish(browser):
    assert(browser.title == 'Ustawienia główne')


@then('the Configuration page title should be in Portuguese')
def configuration_page_title_is_in_portuguese(browser):
    assert(browser.title == 'Configuração Geral')


@then('the Configuration page title should be in Russian')
def configuration_page_title_is_in_russian(browser):
    assert(browser.title == 'Общие настройки')


@then('the Configuration page title should be in Swedish')
def configuration_page_title_is_in_swedish(browser):
    assert(browser.title == 'Allmän Konfiguration')


@then('the Configuration page title should be in Telugu')
def configuration_page_title_is_in_telugu(browser):
    assert(browser.title == 'సాధారణ ఆకృతీకరణ')


@then('the Configuration page title should be in Turkish')
def configuration_page_title_is_in_turkish(browser):
    assert(browser.title == 'Genel Yapılandırma')


@then('the Configuration page title should be in Simplified Chinese')
def configuration_page_title_is_in_simplified_chinese(browser):
    assert(browser.title == '常规配置')
