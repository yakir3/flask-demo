from flask import Flask
from markupsafe import escape
from myapp import myapp

app = Flask(__name__)

# Registry blueprint
app.register_blueprint(myapp, url_prefix='/myapp')

@app.route("/")
def index():
    return "Index Page"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
