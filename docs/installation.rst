===========================================
Church Management System(ChMS) - Production 
===========================================
A project of Good News Technologies, powered by PEK Team of UPITDC.

To use this project follow these steps:

Technology Stack and Version
 Ubuntu 16.04 LTS
 Python 3.5
 Mysql 5.7
 Apache 2.2.3

How to deploy
===================

To use this project follow these steps:

#. Create non-root user with sudo privilges
#. Install dependencies and packages
#. Create Python virtual environment
#. Start Django project
#. Configure Apache
#. Create self-signed SSL certificate


Create non-root user with sudo privilges
======================================

    $ sudo groupadd --system <groupname> 

    $ useradd <username> 
    $ passwd <username>

    $ sudo usermod -aG <groupname> <username> 

    $ sudo visudo
      <username>   ALL=(ALL:ALL) ALL

Install dependencies and packages
======================================
    $ sudo apt-get update &&  apt-get install -y \
      python3-pip \
      apache2 \ 
      libapache2-mod-wsgi3 \
      mysql

 
Create Python virtual environment
======================================

    $ sudo pip3 install virtualenv
    $ mkdir ~/churchapp
    $ cd ~/churchapp

    $ virtualenv myprojectenv
    $ source myprojectenv/bin/activate

Download Django based app 
======================================
    $ git clone https://<username>@bitbucket.org/churchappgroup/churchapp.git --change username to your username
   
    $ pip install -r requirements/production.txt

Create Database (MySQL 5.7)
=============================
Provided that mysqlserver and mysqlclient is already installed:

    $ mysql -u root -p
    $ mysql> CREATE DATABASE <database_name> CHARACTER SET utf8;
    $ mysql> GRANT ALL ON <database_name>.* TO 'database_user' 
        IDENTIFIED BY '<password>';
    
Sync Database with downloaded app 
=============================
Go to repo/ChMS_project.
run migrate::

    $ python manage.py migrate

Configure Apache
======================================
    $ sudo nano /etc/apache2/sites-available/000-default.conf

    <VirtualHost *:80>

        Alias /static /home/sammy/myproject/static
        <Directory /home/sammy/myproject/static>
            Require all granted
        </Directory>

        <Directory /home/sammy/myproject/myproject>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

        WSGIDaemonProcess myproject python-home=/home/sammy/myproject/myprojectenv python-path=/home/sammy/myproject
        WSGIProcessGroup myproject
        WSGIScriptAlias / /home/sammy/myproject/myproject/wsgi.py

    </VirtualHost>

    $ sudo systemctl restart apache2
 

Create self-signed SSL certificate
======================================

