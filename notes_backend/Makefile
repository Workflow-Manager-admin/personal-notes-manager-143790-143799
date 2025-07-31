.PHONY: lint format imports check

lint:
	flake8 app

format:
	black app
	isort app

imports:
	isort app

check:
	flake8 app
	black --check app
	isort --check app

requirements-dev:
	pip install -r requirements.txt
	pip install black isort
