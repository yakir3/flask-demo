from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# routing
@app.route("/")
def index():
    return "Index Page"

# variable rules
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
