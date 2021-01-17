
Инструкция:

1. Необходимо скачать и установить последнюю версию python 3

https://www.python.org

2. Для работы сервера нужно установить следующие библиотеки, используя pip:

pip install flask

pip install flask_wtf

pip install wtforms

3. Клонировать/скачать репозиторий identidock, используя ssh/http/zip:

ssh: git@github.com:aksenof/identidock.git

http: https://github.com/aksenof/identidock.git

zip: https://github.com//aksenof/identidock/archive/master.zip

4. Запустить сервер из коммандной строки:

python 'путь к проекту'/app.py

5. Открыть в браузере (желательно google chrome или opera) страницу:

127.0.0.1:5000 или 127.0.0.1:5000/index

ввести username в поле ввода и нажать кнопку ОК

6. Откроется страница 127.0.0.1:5000/user/username

где будет автоматически мгенерированный аватар по username
