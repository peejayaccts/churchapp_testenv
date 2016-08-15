==============================================================
Church Management System(ChMS) - Production Environment Set-up 
==============================================================
A project of Good News Technologies, powered by PEK Team of UPITDC.

Technology Stack and Version:
#. Ubuntu 16.04 LTS
#. Python 3.5
#. Mysql 5.7
#. Apache 2.2.3

How to deploy
===================

To use this project follow these steps:

#. Create non-root user with sudo privilges
#. Install packages from Ubuntu Repositories
#. Create Python virtual environment
#. Start Django project
#. Configure Apache
#. Create self-signed SSL certificate


Create non-root user with sudo privilges
======================================

On Debian based, create a non root user with sudo privilges.
First, create a system-wide group (e.g developer)::

    $ sudo groupadd --system developer 

Add a your username (e.g efrenversia) with password::

    $ useradd efrenversia 
    $ passwd password 

Add the username to the group::

    $ sudo usermod -aG developer efrenversia 

Edit the sudoers file::

    $ sudo visudo
 
Grant sudo privileges to the created username,
Add the following below, then save:: 

      efrenversia ALL=(ALL:ALL) ALL

Install packages from Ubuntu Repositories
======================================
The following dependencies for environment set-up are:
#. Python 3.5
#. Mysql 5.7
#. Apache 2.2.3
#. mod_wsgi 

Install the depndencies using the created username or root user::

    $ sudo apt-get update &&  apt-get install -y \
           python3-pip \
           apache2 \ 
           libapache2-mod-wsgi3 \
           mysql

Create Python virtual environment
======================================

Install the python virtual environment package::

    $ sudo pip3 install virtualenv

Create the directory for the project::
 
    $ mkdir ~/churchapp

Create a virtual environment directory for the project::
 
    $ cd ~/churchapp
    $ virtualenv myprojectenv
    
Activate the virtual environment for the project::
    $ cd ~/churchapp
    $ source myprojectenv/bin/activate

Download Django based app 
======================================
Download the repository to the created project folder::

    $ git clone https://<username>@bitbucket.org/churchappgroup/churchapp.git --change username to your username
   
Install the Django app dependencies::

    $ pip install -r requirements/production.txt

Create Database (MySQL 5.7)
=============================
Provided that mysqlserver and mysqlclient is already installed::

    $ mysql -u root -p
    $ mysql> CREATE DATABASE <database_name> CHARACTER SET utf8;
    $ mysql> GRANT ALL ON <database_name>.* TO 'database_user' 
        IDENTIFIED BY '<password>';
    
Sync Database with downloaded app 
=============================
Go to repo/ChMS_project::

    $ cd ~/churchapp/ChMS_project 

Run migrate to syncronize the app object data model to MySQL::

    $ python manage.py migrate

Configure Apache
======================================
To set-up a web server for production, edit the apache config file::

    $ sudo nano /etc/apache2/sites-available/000-default.conf

Add the following in the config file::

    <VirtualHost *:80>

        Alias /static /home/efrenversia/churchapp/ChMS_project/ChMS/static
        <Directory /home/efreneversia/churchapp/ChMS_project/ChMS/static>
            Require all granted
        </Directory>

        <Directory /home/efrenversia/churchapp/ChMS_project/ChMS>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

        WSGIDaemonProcess churchapp python-home=/home/efrenversia/churchapp/myprojectenv python-path=/home/efrenverisa/churchapp/ChMS_project/ChMS
        WSGIProcessGroup churchapp 
        WSGIScriptAlias / /home/efrenversia/churchapp/ChMS_project/ChMS/wsgi.py

    </VirtualHost>


Restart the Apache server for the configuration to take effect::

    $ sudo systemctl restart apache2
 

*note: Go to http://127.0.0.1:8000/api/ and explore*


Create self-signed SSL certificate
======================================
TO FOLLOW


