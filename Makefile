############################## Makefile Variables ##############################
CONDA_BIN = $(shell which conda)
APP_CONDA_ENV_NAME ?= "venv-lab-factorial"
ENV_FILE := "./environment.yaml"

CONDA_BIN = $(shell which conda)
CONDA_ROOT = $(shell $(CONDA_BIN) info --base)
APP_CONDA_ENV_PREFIX = $(shell conda env list | grep $(APP_CONDA_ENV_NAME) | sort | awk '{$$1=""; print $$0}' | tr -d '*\| ')
CONDA_ACTIVATE := source $(CONDA_ROOT)/etc/profile.d/conda.sh ; conda activate $(APP_CONDA_ENV_NAME) && PATH=${APP_CONDA_ENV_PREFIX}/bin:${PATH};

############################## Targets ##############################
environment:
	$(CONDA_BIN) remove -n $(APP_CONDA_ENV_NAME) --all -y --force-remove
	$(CONDA_BIN) env update -n $(APP_CONDA_ENV_NAME) -f $(ENV_FILE)

test:
	$(CONDA_ACTIVATE) pytest  # --cov-report term --cov-report html . -vv --durations=0

input_number = 5

run:
	$(CONDA_ACTIVATE) python factorial_printing.py $(input_number)

# PS: you can over-write this variable to calculate the fatorial of any input at run time. For eg to get factorial of 7 you only need to do 'make run input_number=7'
