import pymongo
import hashlib
import json
from flask import Flask, request
from config import *

app = Flask(__name__)
app_client = app.test_client()

db_client = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
current_db = db_client[DB_NAME]
collection = current_db[COLLECTION_NAME]

# Создаем отдельный индекс хэша для быстрого поиска
collection.create_index(HASH)


def generate_hash(json_data) -> str:
    json_string = json.dumps(json_data, sort_keys=True)
    hash_object = hashlib.sha256(json_string.encode())
    return hash_object.hexdigest()


@app.route(ROUTE_PROBLEMS, methods=['POST'])
def submit_issue() -> json:
    # Преобразуем headers и body запроса в отдельные словари
    headers = {key.lower(): value.lower() for key, value in request.headers}
    body = json.loads(request.data.lower())

    # Создаем словарь для инцидента. Хэшируем его и добавляем к нему же
    row = {HEADERS: headers, BODY: body}
    row[HASH] = generate_hash(row)

    collection.insert_one(row)
    return row[HASH]


@app.route(ROUTE_FIND, methods=['POST'])
def find_issues_by_body() -> json:
    """Ищет и возвращает все записи по любому из значений запроса body."""
    query = json.loads(request.data.lower())
    results = []
    for key, value in query.items():
        search_in_body = {f"{BODY}.{key}": value}
        search_in_headers = {f"{HEADERS}.{key}": value}
        found = collection.find(
            filter={'$or': [search_in_body, search_in_headers]},
            projection={'_id': False}
        )
        for row in found:
            results.append(row)
    return results


@app.route(ROUTE_FIND2)
def find_issues_by_hash() -> json:
    """Ищет и возвращает все записи по заданному хэшу и аргументу 'h'."""
    if request.args.get('h'):
        search_in_hash = {HASH: request.args['h']}
        found = collection.find(
            filter=search_in_hash,
            projection={'_id': False}
        )
        results = [row for row in found]
        return results
    return []


if __name__ == '__main__':
    app.run(debug=True)
