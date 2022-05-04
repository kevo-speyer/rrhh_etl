SHELL := /bin/bash
.ONESHELL: 

.PHONY: install
install: venv
	source ./venv/bin/activate
	pip install -r requirements.txt
	pip install -e .
    
venv:
	python3 -m venv venv
