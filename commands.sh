#!/usr/bin/env bash

# Create venv
python -m venv .venv

# Source venv
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install required python packages
pip install -r requirements.txt

# Run the webapp
az webapp up --sku F1 -n udacity-ci-cd-project-webapp

# Display logs of the webapp
az webapp log tail