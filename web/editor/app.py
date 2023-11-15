# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__, static_folder="../static")


# RUS: Страница будет изменена у пользователя благодаря ymab, мы отдаем изначальную
# ENG: The original page is sent, it will be altered by ymab on client-side
@app.route("/editor")
def index():
    return render_template("editor.html")
