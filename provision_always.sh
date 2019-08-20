#!/bin/bash

# Install latest requirements
pip3 install -r /vagrant/requirements.txt

# Get env variables and other settings
. /home/vagrant/.bashrc

# Use environment variables
. app.env

# Start Django local server
python manage.py runserver 0.0.0.0:8000  > /dev/null 2>&1 &
