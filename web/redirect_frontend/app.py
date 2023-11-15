# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__, static_folder="../static")


# RUS: Базовая страница, с нее может произойти редирект
# ENG: Base page, from it we will redirect
@app.route("/redirect")
def index():
    return render_template("redirect.html")


# RUS: Тестовый вариант страницы, на которую происходит редирект
# ENG: Experimental page, we will redirect here
@app.route("/redirect/v1")
def index_v1():
    return render_template("redirect_v1.html")
