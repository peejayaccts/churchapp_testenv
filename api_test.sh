#!/bin/sh

set -ev

python api_functional_tests.py
python functional_tests.py
