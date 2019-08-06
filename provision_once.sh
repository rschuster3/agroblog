#!/bin/bash

apt-get -y update

# Install npm and node
apt-get -y install nodejs
apt-get -y install npm

# Install system requirements
#apt-get -y install python3-setuptools
#easy_install3 pip  # will be a Python3 pip
apt-get -y install python-pip

# Install requirements into agro env
pip install -r /vagrant/requirements.txt

# Install git
apt-get -f install # take care of "unmet dependencies"
apt-get -y install git

# Add Virtualenv settings to .bashrc so they load on every vagrant up
cat > /home/vagrant/.bashrc <<INIT
    cd /vagrant
INIT
