import os

#Environment Variables to Be Set By User

SPREADSHEET_URL = os.environ.get("SPREADSHEET_URL", "") #google sheets url, must be exportable to csv
#eg: 'https://docs.google.com/spreadsheets/d/15cD7qfnnjTziWbTPWhr2Blmi-uWJ7NKlA_cjWLUM2PQ/export?format=csv'
#note the path /export?format=csv
GITHUB_OWNER = os.environ.get("GITHUB_OWNER", '') #username of github owner
REPO_NAME = os.environ.get("REPO_NAME", "")
PERMISSION = os.environ.get("PERMISSION", "")
TOKEN = os.environ.get("TOKEN", "") #personal authentication token for github account

#Environment Variables Automatically Set By main.sh Script

OWNER_URL = os.environ.get("OWNER_URL", "") #url of github account, of the form https://api.github.com/users/{username}
BASE_API_URL = os.environ.get("BASE_API_URL", "") 
CRON_TAB=os.environ.get("CRON_TAB", "")
VIRTUAL_ENV=os.environ.get("PYTHON_VIRTUAL_ENV_PATH", "")
