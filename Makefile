VENV_NAME = venv
PYTHON = python3
VIRTUALENV = $(PYTHON) -m venv
PIP = $(VENV_NAME)/bin/pip
PYTHON_INTERPRETER = $(VENV_NAME)/bin/python

all: install

$(VENV_NAME)/bin/activate: requirements.txt
	@echo "Creating virtual environment..."
	$(VIRTUALENV) $(VENV_NAME)
	@echo "Upgrading pip..."
	$(PIP) install --upgrade pip
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

install: $(VENV_NAME)/bin/activate

test: $(VENV_NAME)/bin/activate
	@echo "Running tests..."
	$(PYTHON_INTERPRETER) -m unittest discover tests

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist build *.egg-info

build: clean install
	@echo "Building the package..."
	$(PYTHON_INTERPRETER) setup.py sdist bdist_wheel

publish: build
	@echo "Publishing the package..."
	twine upload dist/*

freeze:
	@echo "Freezing dependencies..."
	$(PIP) freeze > requirements.txt

.PHONY: all install test clean build publish freeze
