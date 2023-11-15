# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__, static_folder="../static")


# RUS: Отдаем страницу, на которой скрипт на странице обработает флаги и отобразит нужный вариант страницы
# ENG: Just send HTML, where js code would fetch flags and apply changes
@app.route("/flags")
def index():
    return render_template("frontend.html")
