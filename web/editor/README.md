[Русский](#редактор) | [English](#editor)

# Редактор
Самый простой для создания эксперимента способ, однако менее гибкий, чем альтернативы. Также его преимуществом можно считать, что не требуются изменения в коде страницы и ее релиз для каждого эксперимента.
При создании эксперимента перейти в визуальный редактор и привнести необходимые изменения на страницу. Подробнее о возможностях [здесь](https://yandex.ru/support/varioqub/create.html#create__edit).

Для нашей задачи достаточно изменить путь до изображения.

В настройках эксперимента на `metrika.yandex.ru` нужно поменять для тестового варианта путь с "static/src/black_corgi.png" на "static/src/red_corgi.png". Запустив сервер можно проверить, что все работает в окне "Проверка эксперимента".

### В интерфейсе
![Снимок экрана 2024-12-16 в 16 51 03](https://github.com/user-attachments/assets/03b51300-88dc-4ef7-89cd-d07594de5ed2)

# Editor
Visual editor is the simplest method to conduct experiments, yet it is less flexible than other options. However it has some benefits apart from simplicity as website's code isn't changed and no new releases are necessary.
To start experiment open visual editor and apply changes you want. More on that you can find [here](https://yandex.ru/support/varioqub/create.html#create__edit).

For our purposes we only have to change image path.

In experiment's settings at `metrika.yandex.ru` we need to modify image path from "static/src/black_corgi.png" to "static/src/red_corgi.png" for our experimental page. Running the server you can verify everything is okay by falling into experiment's options.

### In interface
![Снимок экрана 2024-12-16 в 16 46 37](https://github.com/user-attachments/assets/1f9f7eea-8682-4705-81b4-9a0d26a36a22)
