[Русский](#редирект) | [English](#redirect)

# Редирект
Если для проведения эксперимента существует достаточно много изменений, что реализовать их в коде одной страницы крайне неудобно, то можно подключить тесты с помощью редиректа. Для этого нам нужно подготовить по странице для каждой опции в эксперименте.

Здесь имеем базовую страницу `/redirect`, а обновленная лежит по пути `/redirect/v1`, при переходе на базовую может произойти редирект, при попадании в иную группу эксперимента.

Настройка эксперимента на `metrika.yandex.ru` должна включать лишь страницу с которой хотим настроить редирект, а ссылка для редиректа в нашем случае будет `redirect/v1`. Запустив сервер можно проверить, что все работает в окне "Проверка эксперимента".

# Redirect
Redirect is preferable if page changes dramatically or you already have new page for experiments up and running. Prepare in advance a page for every experiment's group.

In this example we have a base page at `/redirect`, and an alternative at `/redirect/v1`, when user enters a base page there is a chance he will be redirected, depending on the experiment group he is in.

Setup an experiment at `metrika.yandex.ru` as follows: url filter should only cover base page, otherwise there could be multiple redirects. In our case redirect path is `redirect/v1`. After starting the server we can verify everything on experiment's settings page.
