======================================================
Church Management System(ChMS) - Front-end Installation 
=====================================================

A project of Good News Technologies, powered by PEK Team of UPITDC.

Development Tools and Version
#. node 4.4.7 
#. npm 3.10.5 
#. bower
#. yo 
#. grunt 
#. generator-angular
#. generator-karma

How to run front-end 
===================

To use this project follow these steps:

#. Install nodejs and npm 
#. Setup npm permissions
#. Install development tools 
#. Generate Angular folder structure 
#. Run Angular  



Install nodejs and npm 
==========================
Install nodejs and npm relative to your OS 

Check the SPECIFIC version::
    $ node -v
    $ npm -v

Setup npm permissions
==========================
For debian based, set npm permissions. 
The folders node_modules,bin,share are the main directory for all npm
packages::

    $ sudo chown -R $(whoami) /usr/local/lib/node_modules
    $ sudo chown -R $(whoami) /usr/local/lib/bin
    $ sudo chown -R $(whoami) /usr/local/lib/share

Install all development tools 
==========================
For debian based, the tools will be stored in the 3 folders stated above

The following are brief description of the development tools
-----------------------------------------------------------
Grunt: automated build system (e.g auto minify)
Bower: package manager that contains dependencies (e.g Bootstrap package)
Yoeman: generates the folder structure/scaffolding automatically
        (generator-angular)
Karma: javascript test runner 

Install the tools on GLOBAL set-up::
    $ npm install -g grunt-cli bower yo gnerator-karma generator-angular 

Generate Angular folder structure 
==========================

Generate the scaffolding::
    $ cd ~/churchapp/ChMS_project/app/ 
    $ yo angular app 

Run App for development
==========================
Build and run the app using grunt-cli::
    $ grunt serve

The development folder can be found in the /app/ folder

Build the App for production 
==========================
Build and run the app using grunt-cli::
    $ grunt build 

The production folder can be found in the /dist/ folder


