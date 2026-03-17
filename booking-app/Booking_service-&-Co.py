import os
from flask import  Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST", "PAGE1"])
def page_redirect():
    if request.method == "PAGE1":
        print("hello world")

    return render_template("frontendlanding.html")

if __name__ == "__main__":
    app.run(debug=True)
