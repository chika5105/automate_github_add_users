from accessories import CRON_TAB, VIRTUAL_ENV
from pathlib import Path
from crontab import CronTab

dir_path = str(Path().absolute())  #Path of current working directory 
command = 'source ' + dir_path + '/.env' + ' && ' + 'cd ' + dir_path + ' && '+ VIRTUAL_ENV + ' add_users.py'
with CronTab(user=True) as cron:
    job = cron.new(command=command, comment = "Cron Job that automatically adds collaborators to github repo every 5 minutes")
    job.minute.every(1)
    #cron.remove_all() #uncomment line to remove all cron jobs once you feel satisfied
    #remember to run this script again using source main.sh




