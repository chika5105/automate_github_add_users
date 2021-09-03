from requests import put, get
from pandas import read_csv
from accessories import *
import logging
from datetime import datetime

def add_users():
    with open('logs.txt', 'a') as logs:
        logs.write('\n' + 'Cron Job Run on ' + str(datetime.now()))
        try:
            response_data = read_csv(SPREADSHEET_URL)
        except Exception as e:
            logs.write('\n' + 'Error!' + str(e))
        else:
            authorization = f'token {TOKEN}'
            headers = {
                "Accept": "application/vnd.github.v3+json",
                "Authorization" : authorization,
                }
            try:
                for grouped_response in (zip(response_data['Your Github username'], response_data['Course Access required'])):
                    username,course = grouped_response
                    if course == 'Software Engineering (CS162)':
                        api_url = BASE_API_URL + str(username)
                        params = {
                            "owner": GITHUB_OWNER,
                            "repo": REPO_NAME,
                            "username": username,
                            'permission': PERMISSION
                        }
                        try:
                            #check if user has already been added
                            get_api_response = get(api_url, headers=headers)
                            logging.info(print("Response for get user status is ", get_api_response.status_code))
                            logs.write('\n'+"Response for get user status of " + str(username) + " is " + str(get_api_response.status_code))
                            if get_api_response.status_code == 404: #user is not a collaborator
                                put_api_response = put(api_url, headers=headers, json = params)
                                if put_api_response.status_code == 201:
                                    logging.info(print("Successfuly Sent Collaboration Request To " + str(username)))
                                    logs.write('\n'+"Successfuly Sent Collaboration Request To " + str(username))
                                else:
                                    logging.error(print('Failed to Send Collaboration Request To ' + str(username) + 'statusCode: '+ str(put_api_response.status_code)))
                                    logs.write('\n'+'Failed to Send Collaboration Request To ' + str(username) + 'statusCode: '+ str(put_api_response.status_code))
                        except Exception as e:
                            logging.error(print('Error!', e))
                            logs.write('\n' + 'Error!' + str(e))
            except KeyError as e:
                logging.error(print('Key Error!', e))
                logs.write('\n' + 'KeyError!' + str(e))


add_users()