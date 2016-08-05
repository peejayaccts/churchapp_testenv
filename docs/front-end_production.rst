=======================================================
Church Management System(ChMS) - Front-end Installation 
=======================================================

This is a guide to setup front-end from scratch
_______________________________________________

A project of Good News Technologies, powered by PEK Team of UPITDC.

Development Tools and Version:

#. node 4.4.7 
#. npm 3.10.5 
#. bower 1.7.9
#. yo 1.8.4
#. grunt-cli v1.2.0 
#. generator-angular
#. generator-karma

How to the run front-end 
===================

To use this project follow these steps:

#. Install git, nodejs and npm 
#. Setup npm permissions
#. Install development tools 
#. Generate Angular folder structure 
#. Run Angular  


Install git, nodejs and npm 
==========================
Provided that git, nodejs and npm is already installed relative to your OS:

Run the following to make sure to install SAME version as stated above::

    $ node -v
    $ npm -v
    $ git -v

Setup npm permissions
==========================
For debian based, set npm permissions: 

The folders node_modules,bin,share are the main directory for all npm
packages::

    $ sudo chown -R $(whoami) /usr/local/lib/node_modules
    $ sudo chown -R $(whoami) /usr/local/lib/bin
    $ sudo chown -R $(whoami) /usr/local/lib/share

*note: This npm permission is set to avoid using sudo when installing npm
packages*
Install all development tools 
==========================
For debian based, the development tools will be stored in the 3 folders stated above

The following are brief description of the development tools
-----------------------------------------------------------
Grunt - automated build system (e.g auto minify):

Bower - package manager that contains dependencies (e.g Bootstrap package):

Yoeman - generates the folder structure/scaffolding automatically (e.g generator-angular):

Karma - javascript test runner: 

Install the tools on GLOBAL set-up::

    $ npm install -g grunt-cli bower yo generator-karma generator-angular 

Generate Angular folder structure 
==========================

Generate the scaffolding::

    $ cd ~/churchapp/ChMS_project/app/ 
    $ yo angular app 

Run App for development
==========================
Build and run the app using grunt-cli::
    $ grunt serve

*note: The development folder can be found in the /app/ folder*

Build the App for production 
==========================
Build and run the app using grunt-cli::

    $ grunt build 

*note: The production folder can be found in the /dist/ folder*


