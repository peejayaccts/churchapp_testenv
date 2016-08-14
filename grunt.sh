#!/bin/bash

set -ev

cd $CI_HOME/ChMS_project/src
grunt test
