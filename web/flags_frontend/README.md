[Русский](#флаги) | [English](#flags)

# Флаги
Это самый гибкий способ подключения эксперимента на страницу. В настройке эксперимента каждой группе пользователей можно задать флаг и его значение. Для получение всех флагов для данного пользователя нужно совершить запрос к `uaas.yandex.ru`.
Стоит обратить внимание на то, что при одновременном проведение нескольких экспериментов на одной странице названия флагов могут пересекаться, а потому мы получаем список всех назначенных значений.

Так как флаги можно получить запросом к `uaas.yandex.ru`, то его можно сделать либо на серверной части, либо на стороне пользователя. Если запрос производит пользователь через `javaScript`, то существует обертка `ymab`, которая значительно упрощает работу. Подробнее об этом [https://yandex.ru/support/varioqub/objects/ymab.html](здесь).

В этом примере получим флаги с помощью `ymab` на фронтенд части.

Настройка эксперимента на `metrika.yandex.ru` должна указывать на каких страницах мы хотим получать флаги.
Зададим для тестового варианта флаг `corgi_image = red_corgi`. Запустив сервер можно проверить, что все работает в окне "Проверка эксперимента".



# Flags
This is the most flexible way to add experiments to your web page. In the experiment settings you can set pairs of key and value for each experiment group. You can retrieve this flag pairs by accessing `uaas.yandex.ru` for each user.
Take note, that it is possible to conduct several experiments on the same page, so some flags may overlap, therefore a list of values for each flag key is returned.

Fetching flags from `uaas.yandex.ru` may be done on server- or client-side. For frontend flags handling it is recommended to use a `javaScript` library with shortcuts wrapped in a `ymab` function call, more on that you can find [https://yandex.ru/support/varioqub/objects/ymab.html](here).

In this particular example we will receive flags via `ymab` shortcut.

For our purposes, experiment settings on `metrika.yandex.ru` should include pages, where we want to receive flags. We set for option `A` flag: `corgi_image = red_corgi`. Now running `flask run` in the terminal, we can verify it is working in "Проверка эксперимента" window.
