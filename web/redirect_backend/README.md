[Русский](#редирект-на-флагах) | [English](#redirect-via-flags)

# Редирект на флагах
С помощью обработки флагов мы можем самостоятельно реализовать редирект, который удобнее для нашего сервера. Добавим флаг, значения которого в экспериментах будет указанием того, на какую страницу нужно совершить редирект.
Основной сложностью здесь является необходимость на всех страницах, на которые совершается редирект отправить `metrika.yandex.ru` техническое поле `experiments`. Для этого в примере устанавливается вспомогательная куки, которая считывается при редиректе и удаляется.

Настройка эксперимента на `metrika.yandex.ru` должна содержать флаг `redir`, значение которого указывает на страницу.
В этом примере нужно установить флаг `redir = test_index`.

### В интерфейсе
![Снимок экрана 2024-12-16 в 16 30 03](https://github.com/user-attachments/assets/7700b0e0-c335-4aa1-bcad-7852e3ba7d47)


# Redirect via flags
It is possible to manually redirect user on server side. We can store information about redirect paths in flag's value to avoid changing code later. Alas, one problem arises. on every destination page it is important to send Metrika information about ongoing experiments.
In this example we tackle this problem with temporary cookie which stores experiments string value.

Setup experiment at `metrika.yandex.ru` you need to add flag like `redir` and it's value to be indication for destination page upon redirect.
In our particular case: `redir = test_index`.

### In interface
![Снимок экрана 2024-12-16 в 16 30 41](https://github.com/user-attachments/assets/8f131aec-4f15-4376-957e-12983e3895e1)
