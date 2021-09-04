from accessories import CRON_TAB, VIRTUAL_ENV, FREQUENCY_IN_MINUTES, REPO_NAME
from pathlib import Path
from crontab import CronTab

dir_path = str(Path().absolute())  #Path of current working directory 
command = 'source ' + dir_path + '/.env' + ' && ' + 'cd ' + dir_path + ' && '+ VIRTUAL_ENV + ' add_users.py'
with CronTab(user=True) as cron:
    job = cron.new(command=command, comment = "Cron Job That Automatically Adds Collaborators to Github Repo: " + str(REPO_NAME) + " every " + str(FREQUENCY_IN_MINUTES) + " minute(s)")
    job.minute.every(FREQUENCY_IN_MINUTES)
    #cron.remove_all() #uncomment line to remove all cron jobs once you feel satisfied
    #remember to run this script again using source main.sh




