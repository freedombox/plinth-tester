def test_plinth_login(browser):
    browser.visit('http://127.0.0.1:8000/plinth')
    browser.fill('username', 'tester')
    browser.fill('password', 'tester')
    browser.find_by_value('Login').click()
    assert browser.is_text_present('Services and Applications')
