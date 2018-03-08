import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi I'm here!"

@app.route("/slash", methods=["GET", "POST"])
def respond():
    if request.method == "GET":
        return "you GET-ted slash!"
    elif request.method == "POST":
        return "you POST-ed slash!"

if __name__ == '__main__':
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)))