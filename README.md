# flask_api_with_mongo

## Installation
1. Клонируйте репозиторий:
```bash
git clone https://github.com/codingoleg/flask_api_with_mongo.git
```
2. Перейдите в него:
```bash
cd .\flask_api_with_mongo\
```
+ При необходимости отредактируйте config.py.
+ Соберите образ docker-compose.
```bash
docker-compose up
```

## Usage
Доступные URL:
1. http://127.0.0.1:5000/problems [POST]\
Добавляет запись (body и headers). Возвращает хэш записи (text).
2. http://127.0.0.1:5000/find [POST] \
Ищет и возвращает все записи (json) по любому из значений, указанных в body
запроса. Поиск происходит и в body, и в headers.
4. http://127.0.0.1:5000/find2 [GET] \
Ищет и возвращает все записи (json) по заданному хэшу и аргументу 'h'. \
Пример запроса: http://127.0.0.1:5000/find2?h=6asd65weasd354w2iu4has

POST-запросы без заголовка Content-Length приняты не будут.

## License
GNU GPLv3 