# coding: utf-8

import requests

from flask import Flask, render_template, make_response, request
from collections import defaultdict

app = Flask(__name__, static_folder="../static")


# RUS: Переводим сырые флаги в удобный нам формат
# ENG: Preprocess received flags
def process_flags(splitter_flags):
    # RUS: При пересечении имен флагов между экспериментами может иметься несколько значений
    # ENG: As stated earlier flags may overlap, hence we have a list of values
    flags = defaultdict(list)

    for flag_info in splitter_flags:
        key = flag_info["n"]
        value = flag_info["v"]

        # RUS: Тип является вспомогательным полем, необходимым для работы ymab, самостоятельно стоит обрабатывать лишь "flag"
        # ENG: flag type is relevant to ymab method, manually you should handle only "flag" type
        flag_type = flag_info["t"]
        if flag_type == "flag":
            flags[key].append(value)

    return flags


def split_user(request, icookie):
    query = {
        # RUS: Имя счетчика
        # ENG: counter name
        "client_id": "metrika.<YOUR_COUNTER_ID>",

        # RUS: Полный путь страницы с cgi параметрами, по нему произойдет разбиение, должен подходить под заданный в url-филтры
        # ENG: Full path with cgi parameters, used to assign experiments, should fit url-filters
        "url": request.url,

        # RUS: Помогает опознать пользователя, чтобы он всегда оказывался в одной группе эксперимента
        # ENG: Identifies user, sp he will be in the same group during experiment
        "i": icookie,

        # RUS: Позволяет передавать собственные поля для разбиения. Используется в расширенной версии
        # ENG: Custom filters for the user. It isn't accessible in free version
        "client_feature": {}
    }

    try:
        # RUS: Получаем эксперименты, в которые попал пользователь и соответствующие им флаги
        # ENG: Fetching flags for the user directly
        splitter_response = requests.get(
            "https://uaas.yandex.ru/v1/exps",
            params=query,
            timeout=2  # RUS: Задержка ответа, которую ваш сервис может себе позволить
                       # ENG: Max waiting time that your service may have
        )
        splitter_response.raise_for_status()

        splitter_data = splitter_response.json()
    except Exception as e:
        # RUS: Здесь также стоит залогировать ошибку, чтобы обнаружить проблемы в ходе эксперимента
        # ENG: Exceptions should be logged here to track errors in experiment

        # RUS: Из-за сбоев сети ответ может не дойти, а потому нужно везде предусмотреть значения по умолчанию
        # ENG: Due to some internet connection issues, flags may never be received, set default values, so your site wont break
        splitter_data = {
            "flags": {},
            "i": icookie,
            "experiments": "",
        }

    # RUS: Флаги стоит воспринимать как сигналы к изменениям на странице
    # ENG: Flags should be perceived as signals to change your site
    flags = process_flags(splitter_data["flags"])

    # RUS: Обновленная куки, которую стоит установить при следующем походе в uaas
    # ENG: Updated cookie for the next uaas request
    icookie = splitter_data["i"]

    # RUS: Техническое поле метрики, чтобы отметить в какую группу попал пользователь
    # ENG: Metrika's technical field, registers user's experiments
    experiments = splitter_data["experiments"]

    return (experiments, icookie, flags)


# RUS: Данное имя нужно для совместимости с другими методами подключения
# ENG: This specific cookie should be set for compatibility with other methods
COOKIE_NAME = "_ymab_param"


@app.route("/flags")
def index():
    # RUS: Если пользователь не новичок, то используем старую, чтобы группа не была назначена заново
    # ENG: Will be empty if the user is new and experiment should be assigned, otherwise remembers experiments from last visit
    icookie = request.cookies.get(COOKIE_NAME)
    if icookie is None:
        icookie = ""

    experiments, new_icookie, flags = split_user(request, icookie)

    print("""
            log received flags: {},
            if it contains corgi_image: red_corgi then we will send html page with it
            else return default variant
        """.format(flags))

    if "red_corgi" == flags["corgi_image"][-1]: # last value is from latest experiment
        # RUS: Тестовая страница
        # ENG: Experimental page
        response = make_response(render_template("backendB.html", experiments=experiments))

    # RUS: Всегда нужно устанавливать отображение по умолчанию, так как эксперимент может быть не запущен
    # ENG: Ensure default variant exists in case of experiment being inactive -->
    else:
        # RUS: Обычная страница
        # ENG: Base page
        response = make_response(render_template("backendA.html", experiments=experiments))

    # RUS: Также можно передать флаги в шаблон jinja и в нем внести необходимые изменения
    # ENG: Also you may change the page using jinja templates passing flags to it
    # response = make_response(render_template("backend.html", experiments=experiments, **flags))

    # RUS: Задаем icookie пользователю при изменении, чтобы в следующий раз показалась такая же страница
    # ENG: If icookie was updated, then rewrite it
    if icookie != new_icookie:
        response.set_cookie(
            COOKIE_NAME,
            new_icookie,
            path="/",
            max_age=365 * 24 * 60 * 60, # one year
            # domain="example.com"
        )

    return response
