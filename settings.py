from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# BTN
BTN_LOGIN_URL = 'https://broadcasthe.net/login.php'
BTN_USERNAME = os.environ('BTN_USERNAME')
BTN_PASSWORD = os.environ('BTN_PASSWORD')
BTN_USERNAME_ID = 'username'
BTN_PASSWORD_ID = 'password'
BTN_LOGIN_BUTTON_CSS = 'input.submit'
