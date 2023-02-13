# Сайт риэлторского агентства

Сайт находится в разработке, поэтому доступна только страница со списком квартир и админка для наполнения БД.

## Запуск

- Скачайте код
- Установите актуальную версию poetry в `UNIX`-подобных дистрибутивах с помощью команды:
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```
или в `Windows Powershell`:
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```
Добавьте к переменной окружения `$PATH` команду poetry:
```sh
source $HOME/.poetry/bin
```
Установите виртуальное окружение в директории с проектом командой:
```sh
poetry config virtualenvs.in-project true
```
Установите все зависимости (для установки без dev зависимостей можно добавить аргумент `--no-dev`):
```sh
poetry install
```
Активируйте виртуальное окружение командой: 
```sh
source .venv/bin/activate
```

- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

    Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.

Для генерации значения переменной окружения `SECRET_KEY` можно воспользоваться функцией встроенного модуля `secrets`:

```python3
import secrets
secret_token = secrets.token_urlsafe(nbytes=64)
```

## Запуск линтеров

```sh
isort . && flake8 . && mypy .
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
