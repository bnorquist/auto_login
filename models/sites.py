class Site(object):

    def __init__(self, login_url, credentials, login_button_css,
                 login_confirm_css, username_id='username', password_id='password'):
        self.login_url = login_url
        self.credentials = credentials
        self.username_id = username_id
        self.password_id = password_id
        self.login_button_css = login_button_css
        self.login_confirm_css = login_confirm_css


class Credentials(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
