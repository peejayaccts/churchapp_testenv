#!/bin/sh

set -ev

cd $CI_HOME/ChMS_project
python api_functional_tests.py
python functional_tests.py
