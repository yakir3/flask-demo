import os

from flask import Flask, render_template

# error handler
def page_not_found(e):
  return render_template('404.html'), 404

def internal_server_error(e):
  return render_template('500.html'), 500


# logging
import logging
from flask.logging import default_handler

class CustomFormatter(logging.Formatter):
    def format(self, record):
        # record.levelname = record.levelname.lower()
        return super().format(record)
formatter = CustomFormatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)

# default logging handler
default_handler.setLevel(logging.INFO)
default_handler.setFormatter(formatter)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskexample.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # initial database
    from . import db
    db.init_app(app)

    # register blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # error handler
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, page_not_found)

    # logging
    # app.logger.addHandler(default_handler)

    return app