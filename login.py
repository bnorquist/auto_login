from selenium import webdriver
import settings


def login(login_url, username, password, username_id, password_id):
    browser = webdriver.Chrome()
    browser.get(login_url)
    username_box = browser.find_element_by_id(username_id)
    password_box = browser.find_element_by_id(password_id)

    username_box.send_keys(username)
    password_box.send_keys(password)

    login_button = browser.find_element_by_css_selector(settings.BTN_LOGIN_BUTTON_CSS)
    login_button.submit()


if __name__ == '__main__':
    login(login_url=settings.BTN_LOGIN_URL,
          username=settings.BTN_USERNAME,
          password=settings.BTN_PASSWORD,
          password_id=settings.BTN_PASSWORD_ID,
          username_id=settings.BTN_USERNAME_ID)
