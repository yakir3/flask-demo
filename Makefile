# env
APP_PORT = 8080
NAME = flask-demo
VERSION = 0.1
DOCKER_REGISTRY = hub.docker.com/
DOCKER_PUSH_NAME = flask-demo


# pip env
.PHONY: requirements test

.venv:
    python3 -m venv .venv

requirements:
	#pip freeze > requirements.txt
    source .venv/bin/activate && \
        python3 -m pip install -r requirements.txt && \
        python3 -m pip install pytest

test: .venv requirements dev-requirements
    source .venv/bin/activate && \
        pytest


# poetry
.PHONY: requirements test

requirements:
    poetry install

test: requirements
    poetry run pytest
