#!/bin/bash -e

sudo ls -al /etc/apache2/sites-available/
sudo ls -al /etc/apache2/sites-enabled/
sudo a2enmod ssl
sudo service apache2 restart
sudo mkdir /etc/apache2/ssl/
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048  -keyout /etc/apache2/ssl/apache.key  -out /etc/apache2/ssl/apache.crt -subj "/C=US/ST=Virginia/L=Virginia/O=Global Security/OU=IT Department/CN=127.0.0.1"
sudo mv /etc/apache2/sites-available/default-ssl.conf  /etc/apache2/sites-available/default-ssl.conf.bak 
sudo ls -al /etc/apache2/sites-available/
sudo cp chms-default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
sudo a2ensite default-ssl.conf
sudo apachectl configtest
sudo service apache2 restart
