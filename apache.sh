#!/bin/bash -e

sudo a2enmod ssl
sudo service apache2 restart

sudo mkdir /etc/apache2/ssl/
#sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
#                -keyout /etc/apache2/ssl/apache.key \
#                -out /etc/apache2/ssl/apache.crt

sudo cp /etc/apache2/sites-available/default-ssl.conf \
        /etc/apache2/sites-available/default-ssl.conf.bak 

cat chms-default-ssl.conf > etc/apache2/sites-available/default-ssl.conf 

sudo cat /etc/apache2/sites-available/default-ssl.conf

sudo a2ensite default-ssl.conf

sudo apachectl configtest

sudo service apache2 restart



