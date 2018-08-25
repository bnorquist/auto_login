from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(site):
    try:
        browser = webdriver.Chrome()
        browser.get(site.login_url)
        username_box = browser.find_element_by_id(site.username_id)
        password_box = browser.find_element_by_id(site.password_id)

        username_box.send_keys(site.credentials.username)
        password_box.send_keys(site.credentials.password)

        login_button = browser.find_element_by_css_selector(site.login_button_css)
        login_button.submit()

        verification_element = verify_logged_in(browser, site)

        if verification_element:
            print('log in verified for {}'.format(site.login_url))
            return True

    except Exception as e:
        print('failed to login {}'.format(str(e)))
        return False


def verify_logged_in(browser, site):
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, site.login_confirm_css)))
        return element
    except Exception as e:
        print('login not confirmed Exception: {}'.format(str(e)))
