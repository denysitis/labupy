.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv"
	pip install pipenv
	@echo "Installing python 3.8"
    pipenv --python 3.8
    @echo "Installing requests, ntplib, pytest"
    pipenv install requests
    pipenv install ntplib
    pipenv install pytest

test:
	@echo "Start tests."
	pipenv run pytest tests/tests.py > results.txt

run:
	@echo "Run Python app."
	pipenv run python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt"
    	git add results.txt
    	git commit -m "add file in lab2 results.txt"
    	git push