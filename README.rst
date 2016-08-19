================================================
Church Management System(ChMS) - Django Back-end
================================================

A project of Good News Technologies, powered by PEK Team of UPITDC.

To use this project follow these steps:

#. Create your working environment (virtuanenv, or venv)
#. Clone this repo
#. Installation of Dependencies
#. Create Database
#. Sync Database with Repo
#. Create superuser
#. Run Server and Test

Working Environment 
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

We recommend to put your virtual environment on a separate directory such as ~/venv or C:/venv

Example: Using venv Only
------------------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::
    $ cd ~/virtual_env
    $ python3 -m venv chms_venv 
    $ source chms_venv/bin/activate

Clone this repo
===================

To get a copy of the project, provided that you have access to the repository.
run the following command::

    $ git clone https://<username>@bitbucket.org/churchappgroup/churchapp.git --change username to your username

Installation of Python Dependencies (Python 3.5)
=============================

Depending on where you are installing dependencies:

Initially(First run)::

    $ pip install -r requirements/base.txt

When you have other packages customized for your machine::

    $ pip install -r requirements/local_<user>.txt

Production::

    $ pip install -r requirements/production.txt

Create Database (MySQL 5.7)
=============================
Provided that mysqlserver and mysqlclient is already installed:

Initially(First run)::

    $ mysql -u root -p
    $ mysql> CREATE DATABASE GNT_ChMS_MyDB CHARACTER SET utf8;
    $ mysql> GRANT ALL ON GNT_ChMS_MyDB.* TO 'pekUrsTruly' IDENTIFIED BY 'GloriaTai4ndP#k';
    
*note: these instructions show creation of database called "GNT_ChMS_MyDB".  You
can replace this name with the database name you want to use. you can also change the username.*
        

Sync Database with Repo
=============================
Go to repo/ChMS_project.
run migrate::

    $ python manage.py migrate

Create superuser
=============================
Go to repo/ChMS_project.
run::

    $ python manage.py createsuperuser

*note: Follow the instructions. Take note of the user and password entered here which
will be used in authenticating the api.*

Collect all static files
=============================
Go to repo/ChMS_project.
run::

    $ python manage.py collectstatic 
        
Run Server and Test
=============================
Your repo and database are now ready.
run::

    $ python manage.py runserver

if you want to use your own settings on config/settings/local_<user>.txt
run::

    $ python manage.py runserver --settings=config.settings.local_<user>

   
*note: Go to http://127.0.0.1:8000/api/ and explore*
        
