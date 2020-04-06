# hello.py (root dir of repo)

from flask import Flask

app = Flask(__name__)

# route: a URL path to visit

@app.route("/")
def hello_world():
    print("VISITED HELLO PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED ABOUT PAGE")
    return "About me!"