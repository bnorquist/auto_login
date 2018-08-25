from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

BTN_USERNAME = os.environ('BTN_USERNAME')
BTN_PASSWORD = os.environ('BTN_PASSWORD')
BTN_USERNAME_ID = os.environ('BTN_USERNAME_ID')
BTN_PASSWORD_ID = os.environ('BTN_PASSWORD_ID')
