#! /bin/bash

# Update from git
sudo git stash
sudo git pull

sudo chmod -R 777 .
sudo chmod 400 it/devKey.pem

cd code
sudo ./manage.py collectstatic
sudo ./manage.py syncdb
sudo ./manage.py migrate

cd /home/bitnami/stack
sudo ./ctlscript.sh restart apache

echo ""
echo "** Update complete **"
