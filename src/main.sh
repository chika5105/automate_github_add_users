#!/bin/bash
source .env #export environment variables
source authenticate.sh
python_path=`which python3`
if [ -z "${python_path}" ]; #python path is empty string or unset
then
    echo 'No python3 installation found. Searching for Homebrew....';
    homebrew = `which brew`
    if [ -z "${homebrew}" ];
    then
        echo 'Homebrew client not found, Installing Homebrew....'
        echo 'You will be prompted for your password'
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        echo "Successfully installed Homebrew"
    else
        echo "Found Homebrew Client at " $homebrew

    fi
    echo "Installing Python3 "
    brew install python3
    echo "Successfully installed Python3"

else
    echo 'Found Installed Python Path. Using Python Path:'  $python_path;
fi
pip3=`which pip3`

if [ -z "${pip3}" ];
then
    echo 'Pip3 Not Found, installing pip3.......';
    echo 'You will be prompted for your password';
    curl -O https://bootstrap.pypa.io/get-pip.py
    sudo $python_path get-pip.py
else
    echo 'Found Pip3 install client:' $pip3;
    
fi
virtual_env=$VIRTUAL_ENV
if [ -z "${virtual_env}" ]; #we aren't currently in a virtual env
then
    #make a new virtual environment called automate_github_users
    mkvirtualenv automate_github_add_users
    workon automate_github_add_users
else
    echo 'Found virtual environment :' $virtual_env;
    
fi
export PYTHON_VIRTUAL_ENV_PATH=$python_path


#install required dependencies in environment
pip3 install -r requirements.txt

#get cron_tab path
export CRON_TAB=`which crontab`
echo "Found cron_tab file at " $CRON_TAB
echo "Granting Write Permissions To File, You will be prompted for your password"
sudo chmod +x $CRON_TAB
#run schedule_python_script.py
echo "Running the Cron job scheduler Python Script"
$python_path schedule_python_script.py
echo "Done! Enjoy!"

