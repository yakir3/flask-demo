[![Python](https://img.shields.io/badge/Python-3.12.2-red)](https://www.python.org/downloads/release/python-3109/)
[![Flask](https://img.shields.io/badge/flask-3.0.3-blue)](https://flask.palletsprojects.com/en/3.0.x/)

## Dependencies 

### Mysql
```bash
mkdir ./volume

docker run --name flask-demo \
  -e MYSQL_ROOT_PASSWORD=root_pwd \
  -e MYSQL_DATABASE=flask-demo \
  -p 3306:3306 \
  -v $(pwd)/volume/mysql_data:/var/lib/mysql \
  -d mysql:5.7 --character-set-server=utf8mb4
```

## Start project

### Pip
```bash
# Create Virtualenv
python3 -m venv .venv


# Install denpendencies
python3 -m pip install pytest
python3 -m pip install -r requirements.txt


# Init db and config
flask --app flaskexample init-db


# Start for dev
source .venv/bin/activate
export FLASK_ENV=development
flask [--app flaskexample] run [--debug] [--host=0.0.0.0] [--port=5000]


# Start for prod
source .venv/bin/activate
export FLASK_ENV=production
uwsgi --ini uwsgi.ini
uwsgi --reload logs/uwsgi.pid
uwsgi --stop logs/uwsgi.pid
```

### Poetry
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$PATH:/root/.local/bin"
#echo PATH="$PATH:/root/.local/bin" >> ~/.bashrc


# Create Virtualenv
poetry config virtualenvs.in-project true
poetry env use `which python3.12`


# Install denpencies
poetry add Flask
poetry install


# Init db and config
flask --app flaskexample init-db


# Start for dev
poetry shell
export FLASK_ENV=development
flask [--app flaskexample] run [--debug --host=0.0.0.0:5000]


# Start for prod
poetry shell
export FLASK_ENV=production
uwsgi --ini uwsgi.ini
uwsgi --reload logs/uwsgi.pid
uwsgi --stop logs/uwsgi.pid
```

## Make the Project Installable

```bash
# Build and publish
poetry build
poetry config pypi-token.pypi pypi-token-xxxxx
poetry publish


# Install
# option1
pip install dist/flaskexample-0.1.0-py3-none-any.whl
# option2
pip install flaskexample
# option3
poetry add flaskexample
```
