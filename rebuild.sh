#!/bin/bash
# This runs on the production server: fetches new code,
# installs needed packages, and restarts the server.

export project_name=django_template

# get new source code onto the server
git pull origin master
# activate our virtual env:
source /home/$project_name/.virtualenvs/$project_name/bin/activate
# install all of our packages:
pip install -r requirements.txt
echo "Going to reboot the webserver"
API_TOKEN=$1 pa_reload_webapp.py $project_name.pythonanywhere.com
touch reboot
