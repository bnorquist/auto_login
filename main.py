from models.sites import Site, Credentials
from scripts.login import login
import settings


if __name__ == '__main__':

    btn = Site(
        login_url=settings.BTN_LOGIN_URL,
        password_id=settings.BTN_PASSWORD_ID,
        username_id=settings.BTN_USERNAME_ID,
        login_button_css=settings.BTN_LOGIN_BUTTON_CSS,
        login_confirm_css=settings.BTN_LOGIN_CONFIRM_CSS,
        credentials=Credentials(
            username=settings.BTN_USERNAME,
            password=settings.BTN_PASSWORD,
        )
    )

    login(site=btn)
