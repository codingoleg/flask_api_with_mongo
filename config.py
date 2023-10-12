# Параметры Flask
FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5000

# Параметры БД
# DB_HOST должен быть таким же, как название сервиса в docker-compose.yml
# Либо DB_HOST = 'localhost' для локального запуска.
DB_HOST: str = 'mongodb'
DB_PORT: int = 27017
DB_NAME: str = 'db'
COLLECTION_NAME: str = 'issue_system'

# Названия ключей
BODY: str = 'body'
HEADERS: str = 'headers'
HASH: str = 'hash'

# Пути
ROUTE_PROBLEMS: str = '/problems'
ROUTE_FIND: str = '/find'
ROUTE_FIND2: str = '/find2'

# URLs
URL_INDEX: str = f"http://{FLASK_HOST}:{FLASK_PORT}"
URL_PROBLEMS: str = URL_INDEX + ROUTE_PROBLEMS
URL_FIND: str = URL_INDEX + ROUTE_FIND
URL_FIND2: str = URL_INDEX + ROUTE_FIND2
