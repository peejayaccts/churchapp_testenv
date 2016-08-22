==============================================================
Church Management System(ChMS) - Production Environment Set-up 
==============================================================

A project of Good News Technologies, powered by PEK Team of UPITDC.

:Authors:
    Philip Sales
    Efren Sia
    Kristhian Tiu
    Jonathan Tabac

:Version: 3.0 as of August 15, 2016

Technology Stack and Version:

#. Ubuntu 16.04 LTS
#. Python 3.5
#. Mysql 5.7
#. Apache 2.2.3

How to deploy
===================

To use this project follow these steps:

#. Create Ec2 Instance 

#. Make IAM users 

#. `Initial Server set-up`_.

#. `Install MySQL`_.

#. `Install packages from Ubuntu Repositories`_.

#. `Download Django based app`_.

#. `Create the app MySQL database`_.

#. `Create the church app MySQL database`_.

#. `Sync Database with downloaded app`_. 

#. Create self-signed SSL certificate


TODO
Create Ec2 Instance 
======================================
Insert here.

Make IAM users 
======================================
Insert here.


Initial Server set-up
======================================
`References <https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04/>`_.

Steps: 

#. In your local computer, log into your AWS EC2 server as ubuntu user. 
You will need to know your server's public IP address and the path to the 
security key::

    $ ssh -i path/to/.pem ubuntu@SERVER_IP_ADDRESS 

#. Create non-root user with sudo privileges. From ubuntu user, 
switch user as root ::

    $ sudo su - root 

#. Add a your username (e.g chms_admin) with password ::

    $ adduser chms_admin 

   A prompt will appear like this, just enter password and fill the information ::

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

#. Add the created non root user with root privileges::

    $ usermod -aG sudo chms_admin 

#. Log as the non root user ::

    $ su - chms_admin 

TODO
=====

`Additional server setup <https://www.digitalocean.com/community/tutorials/additional-recommended-steps-for-new-ubuntu-14-04-servers>`_.

ALlow ufw status 8000 to check

*TODO: ADD THIS ON TEH VERY START* ::

    $ sudo ufw enable 
    $ sudo ufw allow 8000 

Install MySQL
=============

The following dependencies for environment set-up are:

- Ubuntu 14.04 LTS
- Python 3.5
- Mysql 5.6
- Apache 2.2.3

#. Install the MySQL::

    $ sudo apt-get update
    $ sudo apt-get install -y mysql-server-5.6 \
                              mysql-client-5.6 \ 
                              libmysqlclient-dev 

*note: You will be prompted to Enter MySQL root user, keep this and save it*

#. Check the version of your MySQL::
    
    $ mysql —-version

#. Check the status of your MySQL and restart::
   
    $ service mysql status
    $ sudo service mysql restart

TODO
====
mysql_secure_installation

`MySQL secure setup <https://www.digitalocean.com/community/tutorials/how-to-secure-mysql-and-mariadb-databases-in-a-linux-vps>`_.

Install packages from Ubuntu Repositories
=========================================

#. For Django with Python 3, install the dependencies using the non root user::

    $ sudo apt-get update 
    $ sudo apt-get install -y python3-pip \
                              apache2 \ 
                              libapache2-mod-wsgi3 \

#. Create Python virtual environment, install the python virtual environment 
package::

    $ sudo pip3 install virtualenv

#. Create the directory for the project::
 
    $ mkdir ~/src

#. Create a virtual environment directory for the project::
 
    $ cd ~/src
    $ virtualenv churchapp_env
    
#. Activate the python virtual environment for the project::

    $ cd ~/src
    $ source churchapp_env/bin/activate

Download Django based app 
=========================

#. Download the project from the repository to the created project folder::

    $ git clone https://<username>@bitbucket.org/churchappgroup/churchapp.git 
 
#. Install the Django app dependencies::

    $ cd ~/src/churchappp
    $ pip install -r requirements/production.txt

   *Your console will look like this*::

        $ (churchapp_env) chms_admin@SERVER_IP_ADDRESS: ~/src

Create the church app MySQL database
====================================

#. Create mysql application database and user::

    $ mysql -u root -p
    $ mysql> CREATE DATABASE GNT_ChMS_MyDB CHARACTER SET utf8;
    $ mysql> GRANT ALL ON GNT_ChMS_MyDB.* TO 'pekUrsTruly' 
             IDENTIFIED BY 'GloriaTai4ndP#k';

*note: this is the actual application database name and password*
    
Sync Database with church app 
=============================

#. Go to app source code directory::

    $ cd ~/src/churchapp/ChMS_project 

#. Run migrate to synchronize the app object data model to MySQL::

    $ python manage.py migrate

#. Collect all static files into one folder directory for easier caching of the 
django application assets::

    $ python manage.py collectstatic —-clear

*note: A prompt will look like this, type 'yes' and hit enter*
::

        You have requested to collect static files at the destination
        location as specified in your settings:::

        /home/chms_admin/src/churchapp_testenv/ChMS_project/config/settings/static

        This will overwrite existing files!
        Are you sure you want to do this?

        Type 'yes' to continue, or 'no' to cancel: 

Create a SSL Certificate on Apache (Self-Signed SSL certificate)
===============================================================

`SSL <https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-14-04`_.

#. Enable SSL module in Apache, then restart the server. ::
    
    $ sudo a2enmod ssl
    $ sudo service apache2 restart

#. Create the SSL certificate and store it in a directory::
    
    $ sudo mkdir /etc/apache2/ssl
    $ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt

  *for references* ::

        * openssl: This is the basic command line tool provided by OpenSSL to create and manage certificates, keys, signing requests, etc.

        * req: This specifies a subcommand for X.509 certificate signing request (CSR) management. X.509 is a public key infrastructure standard that SSL adheres to for its key and certificate managment. Since we are wanting to create a new X.509 certificate, this is what we want.

        * -x509: This option specifies that we want to make a self-signed certificate file instead of generating a certificate request.

        * -nodes: This option tells OpenSSL that we do not wish to secure our key file with a passphrase. Having a password protected key file would get in the way of Apache starting automatically as we would have to enter the password every time the service restarts.

        * -days 365: This specifies that the certificate we are creating will be valid for one year.

        * -newkey rsa:2048: This option will create the certificate request and a new private key at the same time. This is necessary since we didn't create a private key in advance. The rsa:2048 tells OpenSSL to generate an RSA key that is 2048 bits long.

        * -keyout: This parameter names the output file for the private key file that is being created.

        * -out: This option names the output file for the certificate that we are generating.

#. When you hit "ENTER", you will be asked a number of questions.
The most important item that is requested is the line that reads 
"Common Name (e.g. server FQDN or YOUR name)". You should enter the domain 
name you want to associate with the certificate, or the server's public 
IP address if you do not have a domain name. 

The questions portion looks something like this ::

        Country Name (2 letter code) [AU]:Your Country
        State or Province Name (full name) [Some-State]:Your State
        Locality Name (eg, city) []:Your Locality
        Organization Name (eg, company) [Internet Widgits Pty Ltd]:Your Company
        Organizational Unit Name (eg, section) []:Department of Kittens
        Common Name (e.g. server FQDN or YOUR name) []:your_domain.com
        Email Address []:your_email@domain.com

#. Configure the Apache to Use SSL, use the **default-ssl.conf** for the 
Apache virtual host configuration file.  Open the file with root privileges::

    $ sudo nano /etc/apache2/sites-available/default-ssl.conf

With all comments removed, the file will look like this ::

        <IfModule mod_ssl.c>
            <VirtualHost _default_:443>
                ServerAdmin webmaster@localhost
                DocumentRoot /var/www/html
                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined
                SSLEngine on
                SSLCertificateFile /etc/ssl/certs/ssl-cert-snakeoil.pem
                SSLCertificateKeyFile /etc/ssl/private/ssl-cert-snakeoil.key
                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>
                BrowserMatch "MSIE [2-6]" \
                                nokeepalive ssl-unclean-shutdown \
                                downgrade-1.0 force-response-1.0
                BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown
            </VirtualHost>
        </IfModule>

Add (if not existing ) or edit the file to look like this, 
then save and exit the file. ::

        <IfModule mod_ssl.c>
            <VirtualHost _default_:443>
                ServerAdmin `**admin@example.com**``
                **ServerName your_domain.com**
                **ServerAlias www.your_domain.com**
                DocumentRoot **/var/www/html**
                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                **Alias /static /home/chms_admin/src/churchapp/ChMS_project/ChMS/static**
                **<Directory /home/chms_admin/src/churchapp/ChMS_project/ChMS/static>**
                    **Require all granted**
                **</Directory>**

                **<Directory /home/chms_admin/src/churchapp/ChMS_project/ChMS>**
                    **<Files wsgi.py>**
                        **Require all granted**
                    **</Files>**
                **</Directory>**

                **WSGIDaemonProcess churchapp python-home=/home/chms_admin/src/churchapp/churchapp_env python-path=/home/chms_admin/src/churchapp/ChMS_project/ChMS**
                **WSGIProcessGroup churchapp**
                **WSGIScriptAlias / /home/chms_admin/src/churchapp/ChMS_project/ChMS/wsgi.py**

                SSLEngine on
                SSLCertificateFile **/etc/apache2/ssl/apache.crt**
                SSLCertificateKeyFile **/etc/apache2/ssl/apache.key**
                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>
                BrowserMatch "MSIE [2-6]" \
                                nokeepalive ssl-unclean-shutdown \
                                downgrade-1.0 force-response-1.0
                BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown
            </VirtualHost>
        </IfModule>

This part here::

                **Alias /static /home/chms_admin/src/churchapp/ChMS_project/ChMS/static**
                **<Directory /home/chms_admin/src/churchapp/ChMS_project/ChMS/static>**
                    **Require all granted**
                **</Directory>**

                **<Directory /home/chms_admin/src/churchapp/ChMS_project/ChMS>**
                    **<Files wsgi.py>**
                        **Require all granted**
                    **</Files>**
                **</Directory>**

                **WSGIDaemonProcess churchapp python-home=/home/chms_admin/src/churchapp/churchapp_env python-path=/home/chms_admin/src/churchapp/ChMS_project/ChMS**
                **WSGIProcessGroup churchapp**
                **WSGIScriptAlias / /home/chms_admin/src/churchapp/ChMS_project/ChMS/wsgi.py**

is how we configure the WSGI pass in Apache. Client connections that Apache 
receives will be translated into the WSGI format that the Django application 
expects using the mod_wsgi module.

#. Activate the SSL enabled site configuration, the restart the Apache to load the new file ::

    $ sudo a2ensite default—ssl.conf
    $ sudo service apache2 restart

#. Test your set-up in your browser ::

    $ https://server_domain_name_or_IP_address

*note: You will get a warning that your browser cannot verify the identity of 
your server because it has not been signed by one of the certificate 
authorities that it trusts. Just hit the “Proceed anyway” button*




