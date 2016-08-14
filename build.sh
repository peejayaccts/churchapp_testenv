#!/bin/sh

set -ev

cd ..
python api_functional_tests.py
python functional_tests.py
