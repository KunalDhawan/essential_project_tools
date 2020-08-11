############################## Makefile Variables ##############################
CONDA_BIN = $(shell which conda)
APP_CONDA_ENV_NAME ?= "venv-lab-factorial"
ENV_FILE := "./environment.yaml"

PIP_EXTRA_INDEX_URL := $(shell echo $$PIP_EXTRA_INDEX_URL)

CONDA_BIN = $(shell which conda)
CONDA_ROOT = $(shell $(CONDA_BIN) info --base)
APP_CONDA_ENV_PREFIX = $(shell conda env list | grep $(APP_CONDA_ENV_NAME) | sort | awk '{$$1=""; print $$0}' | tr -d '*\| ')
CONDA_ACTIVATE := source $(CONDA_ROOT)/etc/profile.d/conda.sh ; conda activate $(APP_CONDA_ENV_NAME) && PATH=${APP_CONDA_ENV_PREFIX}/bin:${PATH};

APP_BUILD_ENV ?= dev
BASE_DOCKER_IMAGE_NAME := "lab_factorial"
DOCKER_IMAGE_TAG := $(APP_BUILD_ENV)-$(shell cat VERSION | head -1 | awk '{$$1=$$1};1')
DOCKER_IMAGE_TAG_LATEST := $(APP_BUILD_ENV)-latest

############################## Targets ##############################
guard-env-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

environment: guard-env-PIP_EXTRA_INDEX_URL
	$(CONDA_BIN) remove -n $(APP_CONDA_ENV_NAME) --all -y --force-remove
	$(CONDA_BIN) env update -n $(APP_CONDA_ENV_NAME) -f $(ENV_FILE)

test:
	$(CONDA_ACTIVATE) pytest  # --cov-report term --cov-report html . -vv --durations=0

input_number = 5

run:
	$(CONDA_ACTIVATE) python factorial_printing.py $(input_number)

export_environment:
	$(CONDA_BIN) env export  -n $(APP_CONDA_ENV_NAME) | grep -v "^prefix: \|^name: " > environment-exported.yaml
	echo  && \
    echo "    - --index-url=https://pypi.org/simple" >> environment-exported.yaml && \
    echo "    - --trusted-host=[pypi.org,pkgs.dev.azure.com]" >> environment-exported.yaml && \
    echo "    - --extra-index-url=\$${PIP_EXTRA_INDEX_URL}" >> environment-exported.yaml && \
    echo "    - -r file:requirements.exported.txt" >> environment-exported.yaml
	cat environment-exported.yaml
	$(CONDA_ACTIVATE)  pip freeze > requirements.exported.txt

package_docker_base_image:
	docker build \
		-t $(BASE_DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) \
		-f ./deployment/docker/Dockerfile.base \
		--build-arg PIP_EXTRA_INDEX_URL=$(PIP_EXTRA_INDEX_URL) \
		--build-arg GIT_COMMIT=$(shell git log -1 --format=%h) \

package_docker_factorial_service:
	docker build \
		-t $(FACTORIAL_DOCKER_IMAGE_NAME) \
		-f ./deployment/docker/Dockerfile.factorial_service \
		--build-arg BASE_IMAGE=$(BASE_DOCKER_IMAGE_NAME) \
		--build-arg BASE_IMAGE_TAG=$(DOCKER_IMAGE_TAG) \
		--build-arg PIP_EXTRA_INDEX_URL=$(PIP_EXTRA_INDEX_URL) \
		--build-arg GIT_COMMIT=$(shell git log -1 --format=%h) \

package:
	export_environment package_docker_base_image package_docker_factorial_service



# PS: you can over-write this variable to calculate the fatorial of any input at run time. For eg to get factorial of 7 you only need to do 'make run input_number=7'

