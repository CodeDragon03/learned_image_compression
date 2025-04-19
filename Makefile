#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = learned_image_compression
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Install Python dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	


## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 src
	isort --check --diff src
	black --check src

## Format source code with black
.PHONY: format
format:
	isort src
	black src


## Set up Python interpreter environment
.PHONY: create_environment
create_environment:
	pipenv --python $(PYTHON_VERSION)
	@echo ">>> New pipenv created. Activate with:\npipenv shell"
	



#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Process the raw dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) -m src.dataset

## Generate features from processed data
.PHONY: features
features: data
	$(PYTHON_INTERPRETER) -m src.features

## Create visualization plots
.PHONY: plots
plots: data
	$(PYTHON_INTERPRETER) -m src.plots

## Train the compression model
.PHONY: train
train: features
	$(PYTHON_INTERPRETER) -m src.modeling.train

## Run model predictions
.PHONY: predict
predict: train
	$(PYTHON_INTERPRETER) -m src.modeling.predict

## Run complete pipeline
.PHONY: pipeline
pipeline: data features plots train predict
	@echo "Full pipeline completed successfully"


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
