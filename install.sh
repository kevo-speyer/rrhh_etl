#!/bin/bash
## This script creates a virtualenv and installs the package in the repository

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
pip install -e .
