==============================================================
Church Management System(ChMS) - Production Environment Set-up 
==============================================================

This is a guide to perform testing for back-end
_______________________________________________

A project of Good News Technologies, powered by PEK Team of UPITDC.

How to run 
===================

To use this testing follow these steps:

#. Install project dependences
#. Activate VirtualEnv and run the server 
#. Execute the testing scripts 


Install project dependences
======================================

Go to ~/churchapp/requirements directory and run the script

    $ pip install -r base.txt 

#. Activate VirtualEnv and run the server 
======================================

After activating your virtual environment. Go to ~/churchapp/ChMS_project directory and run the script

    $ python manage.py runserver

#. Execute the testing scripts 
======================================

Go to ~/churchapp/ChMS_project directory and run the script

    $ python api_functional_tests.py
    $ python functional_tests.py

*note: the expected output syntax is "OK"*
Go to ~/churchapp/ChMS_project directory and run the script

    $ python manage.py runserver

