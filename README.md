[![Python](https://img.shields.io/badge/Python-3.12.2-red)](https://www.python.org/downloads/release/python-3109/)
[![Flask](https://img.shields.io/badge/flask-3.0.3-blue)](https://flask.palletsprojects.com/en/3.0.x/)

### Docker start mysql
```shell
mkdir ./volume

docker run --name flask-demo \
  -e MYSQL_ROOT_PASSWORD=root_pwd \
  -e MYSQL_DATABASE=flask-demo \
  -p 3306:3306 \
  -v $(pwd)/volume/mysql_data:/var/lib/mysql \
  -d mysql:5.7 --character-set-server=utf8mb4
```

### Poetry Virtualenv Init
```shell
# Install Python3
https://www.python.org/downloads/release/python-3109/


# Install Poetry
curl -sSL https://install.python-poetry.org | python -
export PATH="$PATH:/root/.local/bin"
#echo PATH="$PATH:/root/.local/bin" >> ~/.bashrc


# Create Virtualenv
poetry init
poetry env use `which python3.12`


# Install denpencies
poetry add Flask
poetry install

# Project init
# Create dirs
mkdir ./logs ./static ./templates
# Init config
cp config/config.yaml.default config/config.yaml
```

### Virtualenv start project
```shell
# Option 1
# for dev
poetry shell
python manage.py migrate
flask [--app app] run [--debug --host=0.0.0.0:5000]


# for prod
export PROJECT_ENV=prod
poetry shell
uwsgi --ini uwsgi.ini
# uwsgi --reload logs/uwsgi.pid
# uwsgi --stop logs/uwsgi.pid


# Option 2
# for dev
poetry run python manage.py makemigrations
poetry run python manage.py migrate
#poetry run python manage.py collectstatic --noinput
poetry run python manage.py runserver 0.0.0.0:8888

# for prod
export PROJECT_ENV=prod
poetry run python manage.py makemigrations
poetry run python manage.py migrate
#poetry run python manage.py collectstatic --noinput
poetry run uwsgi --ini uwsgi.ini
# poetry run uwsgi --reload logs/uwsgi.pid
# poetry run uwsgi --stop logs/uwsgi.pid
#tail -f logs/uwsgi.log
```
