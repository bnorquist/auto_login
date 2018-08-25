# auto_login
log in to sites to maintain activity

# setup
On OSX: 

`brew install chromedriver`

then inside the project folder: 

`pipenv install`

# usage
create .env file using the template with site username/password

then in the settings file fill out variables they are currently set for BTN

after running `pipenv shell` run `python main.py` or setup a cronjob to run it regularly
 
