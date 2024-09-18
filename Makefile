APP_PORT = 8080
APP_NAME = flask-demo
VERSION = 0.1
DOCKER_REGISTRY = hub.docker.com/yakirinp


# # Option1: pip env
# .PHONY: requirements test

# .venv:
#     python3 -m venv .venv

# requirements:
# 	#pip freeze > requirements.txt
#     source .venv/bin/activate && \
#         python3 -m pip install -r requirements.txt && \
#         python3 -m pip install pytest

# test: .venv requirements dev-requirements
#     source .venv/bin/activate && \
#         pytest


# Option2: poetry env
.PHONY: requirements test

.venv:
	poetry config virtualenvs.in-project true
	poetry env use `which python3.12`

requirements:
	poetry config virtualenvs.in-project true --local
	poetry install

test: .venv requirements
	echo heretest
	# poetry run pytest
