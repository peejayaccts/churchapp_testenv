#!/bin/bash -e

sudo a2enmod ssl

sudo cp /etc/apache2/sites-available/default-ssl.conf \
        /etc/apache2/sites-available/default-ssl.conf.bak 

cat chms-default-ssl.conf > etc/apache2/sites-available/default-ssl.conf 

sudo cat /etc/apache2/sites-available/default-ssl.conf

sudo a2ensite default-ssl.conf

sudo apachectl configtest

sudo service apache2 restart



