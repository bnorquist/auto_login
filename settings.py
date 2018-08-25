from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# BTN
BTN_LOGIN_URL = 'https://broadcasthe.net/login.php'
BTN_USERNAME = os.getenv('BTN_USERNAME')
BTN_PASSWORD = os.getenv('BTN_PASSWORD')
BTN_USERNAME_ID = 'username'
BTN_PASSWORD_ID = 'password'
BTN_LOGIN_BUTTON_CSS = 'input.submit'
BTN_LOGIN_CONFIRM_CSS = 'a.username'
