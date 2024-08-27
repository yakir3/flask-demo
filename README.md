[![Python](https://img.shields.io/badge/Python-3.12.2-red)](https://www.python.org/downloads/release/python-3109/)
[![Flask](https://img.shields.io/badge/flask-3.0.3-blue)](https://flask.palletsprojects.com/en/3.0.x/)

### Docker start mysql
```bash
mkdir ./volume

docker run --name flask-demo \
  -e MYSQL_ROOT_PASSWORD=root_pwd \
  -e MYSQL_DATABASE=flask-demo \
  -p 3306:3306 \
  -v $(pwd)/volume/mysql_data:/var/lib/mysql \
  -d mysql:5.7 --character-set-server=utf8mb4
```

### Python pip env
```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
python3 -m pip install pytest
```

### Python poetry env
```bash
# Install Python3
https://www.python.org/downloads/release/python-3109/


# Install Poetry
curl -sSL https://install.python-poetry.org | python -
export PATH="$PATH:/root/.local/bin"
#echo PATH="$PATH:/root/.local/bin" >> ~/.bashrc


# Create Virtualenv
#poetry init
poetry config virtualenvs.in-project true
poetry env use `which python3.12`


# Install denpencies
#poetry add Flask
poetry install
```

### How To Use
#### Init
```bash
# Create dirs
mkdir ./logs ./static ./templates

# config
mv config.py.default config.py
```

#### Start project
##### Option1: pip
```bash
source .venv/bin/activate
export FLASK_APP=manage.py

# for dev
export FLASK_ENV=development
flask [--app app] run [--debug] [--host=0.0.0.0] [--port=5000]
# for prod
export FLASK_ENV=production
uwsgi --ini uwsgi.ini
# uwsgi --reload logs/uwsgi.pid
# uwsgi --stop logs/uwsgi.pid
```

##### Option2: poetry
```bash
poetry shell
export FLASK_APP=manage.py

# for dev
export FLASK_ENV=development
flask [--app app] run [--debug --host=0.0.0.0:5000]
# for prod
export FLASK_ENV=production
uwsgi --ini uwsgi.ini
# uwsgi --reload logs/uwsgi.pid
# uwsgi --stop logs/uwsgi.pid
```
