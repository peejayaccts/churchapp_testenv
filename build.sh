#!/bin/sh

set -ev

cd ..
cd ChMS_project/
python api_functional_tests.py
python functional_tests.py
