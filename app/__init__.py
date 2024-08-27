from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config.from_object("app.config.config")

    @app.route("/")
    def hello():
        return "<h1>hello world</h1>"

    return app
