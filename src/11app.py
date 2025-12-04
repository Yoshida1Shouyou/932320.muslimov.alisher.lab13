import random

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../client/templates",
    static_folder="../client/static",
)


@app.route("/")
def index():
    return render_template("11home.html")


@app.route("/CalcService/PassUsingJinja2")
def about():
    return render_template(
        "11calc.html",
        first_num=random.randint(0, 10),
        second_num=random.randint(0, 10),
    )
