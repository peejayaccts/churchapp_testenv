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

#. Access server using root login
#. Create non-root user with sudo privilges
#. Install packages from Ubuntu Repositories
#. Create Python virtual environment
#. Start Django project
#. Configure Apache
#. Create self-signed SSL certificate


Access server using root login
======================================
To log into your AWS EC2 server, you will need to know your server's public IP
address::

    local $ ssh -i path/to/.pem ubuntu@SERVER_IP_ADDRESS 

Create non-root user with sudo privilges
======================================

Switch user as root::

    $ sudo su - root 

Create a non root user:
Add a your username (e.g chms_admin) with password::

    $ adduser chms_admin 

A prompt will appear like this, just enter password and fill the information::

    Adding user \`chms_admin' ...
    Adding new group \`chms_admin' (1001) ...
    Adding new user \`chms_admin' (1001) with group \`chms_admin' ...
    Creating home directory \`/home/chms_admin' ...
    Copying files from \`/etc/skel' ...
    Enter new UNIX password: 
    Retype new UNIX password: 
    passwd: password updated successfully 
    hanging the user information for chms_admin
    Enter the new value, or press ENTER for the default
    Full Name []: 
    Room Number []: 
    Work Phone []: 
    Home Phone []: 
    Other []: 
    Is the information correct? [Y/n] Y

Add the non root user with root privileges::

    $ usermod -aG sudo chms_admin 

Log as the non root user ::

    $ su - chms_admin 

*Edit the sudoers file::

    $ sudo visudo
 
Grant sudo privileges to the created username,
Add the following below, then save:: 

      chms_admin ALL=(ALL:ALL) ALL*

Install packages from Ubuntu Repositories
======================================
The following dependencies for environment set-up are:
#. Python 3.5
#. Mysql 5.7
#. Apache 2.2.3
#. mod_wsgi 

Install the MySQL::

    $ sudo apt-get update && apt-get install -y  mysql-server

*note: You will be promtped to Enter MySQL root user*


Install the depndencies using the created username or root user::

    $ sudo apt-get update 
    $ sudo apt-get install -y \
           python3-pip \
           apache2 \ 
           libapache2-mod-wsgi3 \

Install MySQL 5.5 server::

    $ sudo apt-get install -y mysql-server-5.6 \
           mysql-client-5.6 \ 
           libmysqlclient-dev 

Create Python virtual environment
======================================

Install the python virtual environment package::

    $ sudo pip3 install virtualenv

Create the directory for the project::
 
    $ mkdir ~/churchapp

Create a virtual environment directory for the project::
 
    $ cd ~/churchapp
    $ virtualenv churchapp_env
    
Activate the virtual environment for the project::
    $ cd ~/churchapp
    $ source churchapp_env/bin/activate

Download Django based app 
======================================
Download the repository to the created project folder::

    $ git clone https://<username>@bitbucket.org/churchappgroup/churchapp.git --change username to your username
   
*note: change this to ftp*

Install the Django app dependencies::

    $ pip install -r requirements/production.txt

Create Database (MySQL 5.7)
=============================

Create mysql user::

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

ALlow ufw status 8000 to check

*TODO: ADD THIS ON TEH VERY START*
    $ sudo ufw enable 
    $ sudo ufw allow 8000 

Configure Apache
======================================
To set-up a web server for production, edit the apache config file::

    $ sudo nano /etc/apache2/sites-available/000-default.conf

Add the following in the config file::

    <VirtualHost *:80>

        Alias /static /home/chms_admin/churchapp/ChMS_project/ChMS/static
        <Directory /home/efreneversia/churchapp/ChMS_project/ChMS/static>
            Require all granted
        </Directory>

        <Directory /home/chms_admin/churchapp/ChMS_project/ChMS>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>

        WSGIDaemonProcess churchapp python-home=/home/chms_admin/churchapp/churchapp_env python-path=/home/efrenverisa/churchapp/ChMS_project/ChMS
        WSGIProcessGroup churchapp 
        WSGIScriptAlias / /home/chms_admin/churchapp/ChMS_project/ChMS/wsgi.py

    </VirtualHost>


Restart the Apache server for the configuration to take effect::

    $ sudo systemctl restart apache2
 

*note: Go to http://127.0.0.1:8000/api/ and explore*


Create self-signed SSL certificate
======================================
TO FOLLOW


