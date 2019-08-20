#!/bin/bash

apt-get -y update

# Install system requirements
#apt-get -y install python3-setuptools
#easy_install3 pip  # will be a Python3 pip
apt-get -y install python3-pip libpq-dev

# Install requirements into agro env
pip3 install -r /vagrant/requirements.txt

# Install git
apt-get -f install # take care of "unmet dependencies"
apt-get -y install git

# Install postgres
apt-get -y install postgresql postgresql-contrib

# Setup postgres user, db, and perms
-u postgres bash -c "psql -c \"CREATE ROLE blogger SUPERUSER LOGIN PASSWORD '1arrfgtaah0ae1';\""
-u postgres createdb blogdb
-u postgres bash -c "psql -c \"ALTER ROLE blogger SET client_encoding TO 'utf8';\""
-u postgres bash -c "psql -c \"ALTER ROLE blogger SET timezone TO 'UTC';\""
-u postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE blogdb TO blogger;\""

# Add Virtualenv settings to .bashrc so they load on every vagrant up
cat > /home/vagrant/.bashrc <<INIT
    cd /vagrant
INIT
