# Параметры БД
DB_HOST: str = 'localhost'
DB_PORT: int = 27017
DB_NAME: str = 'db'
COLLECTION_NAME: str = 'issue_system'

# Параметры БД для тестов
TEST_DB_NAME: str = 'test_db'
TEST_COLLECTION_NAME: str = 'test_issue_system'

# Ключи
BODY: str = 'body'
HEADERS: str = 'headers'
HASH: str = 'hash'

# Пути
ROUTE_PROBLEMS: str = '/problems'
ROUTE_FIND: str = '/find'
ROUTE_FIND2: str = '/find2'

# URLs
URL_INDEX: str = "http://127.0.0.1:5000"
URL_PROBLEMS: str = URL_INDEX + ROUTE_PROBLEMS
URL_FIND: str = URL_INDEX + ROUTE_FIND
URL_FIND2: str = URL_INDEX + ROUTE_FIND2
