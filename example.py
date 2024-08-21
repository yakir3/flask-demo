from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# Routing
@app.route("/")
def index():
    return "Index Page"

# Variable Rules
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

# HTTP Methods
from flask import request
@app.route("/login", methods=["GET", "post"])
def login():
    if request.method == "POST":
        return "post request"
    else:
        return "other request"

# Static Files
#url_for('static', filename='style.css')

# Rendering Templates
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# File Uploads
from flask import request
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...

# Cookies
from flask import request
@app.route('/')
def index():
    username = request.cookies.get('username')
# Storing cookies
from flask import make_response
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

# Redirects and Errors
from flask import abort, redirect, url_for
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
from flask import render_template
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# Response
# 1. render template && make_response
# 2. APIs with JSON
# 3. Sessions

# Logging
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
