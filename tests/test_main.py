import json
import unittest

from main import app_client, collection
from testcases import *
from config import *


class TestCase(unittest.TestCase):
    def test_submit_issue(self):
        results_0 = app_client.post(URL_PROBLEMS,
                                    data=json.dumps(data_0[BODY]),
                                    headers=data_0[HEADERS])
        results_1 = app_client.post(URL_PROBLEMS,
                                    data=json.dumps(data_1[BODY]),
                                    headers=data_1[HEADERS])
        results_2 = app_client.post(URL_PROBLEMS,
                                    data=json.dumps(data_2[BODY]),
                                    headers=data_2[HEADERS])
        results_3 = app_client.post(URL_PROBLEMS,
                                    data=json.dumps(data_3[BODY]),
                                    headers=data_3[HEADERS])
        results_4 = app_client.post(URL_PROBLEMS,
                                    data=json.dumps(data_4[BODY]),
                                    headers=data_4[HEADERS])

        # Проверка статус-кодов
        self.assertEqual(results_0.status_code, 200)
        self.assertEqual(results_1.status_code, 200)
        self.assertEqual(results_2.status_code, 200)
        self.assertEqual(results_3.status_code, 200)
        self.assertEqual(results_4.status_code, 200)

        # Проверка индентичности хэшей
        self.assertEqual(results_0.text, data_0_1_hash)
        self.assertEqual(results_0.text, results_1.text)
        self.assertEqual(results_1.text, results_2.text)
        self.assertEqual(results_3.text, data_3_hash)
        self.assertEqual(results_4.text, data_4_hash)

    def test_find_issues_by_body(self):
        results_0 = app_client.post(URL_FIND, data=json.dumps(query_0))
        results_1 = app_client.post(URL_FIND, data=json.dumps(query_1))
        results_2 = app_client.post(URL_FIND, data=json.dumps(query_2))
        results_3 = app_client.post(URL_FIND, data=json.dumps(query_3))
        results_4 = app_client.post(URL_FIND, data=json.dumps(query_4))

        # Проверка статус-кодов
        self.assertEqual(results_0.status_code, 200)
        self.assertEqual(results_1.status_code, 200)
        self.assertEqual(results_2.status_code, 200)
        self.assertEqual(results_3.status_code, 200)
        self.assertEqual(results_4.status_code, 200)

    def test_find_issues_by_hash(self):
        with app_client as client:
            results_0 = client.get(URL_FIND2,
                                   query_string={'h': data_0_1_hash})
            results_2 = client.get(URL_FIND2, query_string={'h': data_2_hash})
            results_3 = client.get(URL_FIND2, query_string={'h': data_3_hash})
            results_invalid = client.get(URL_FIND2,
                                         query_string={'h': invalid_hash})

        # Проверка статус-кодов
        self.assertEqual(results_0.status_code, 200)
        self.assertEqual(results_2.status_code, 200)
        self.assertEqual(results_3.status_code, 200)
        self.assertEqual(results_invalid.status_code, 200)

    def test_delete_test_data(self):
        # Удалить тестовые данные из базы
        collection.delete_many({f"{BODY}.test_data": "true"})


if __name__ == '__main__':
    unittest.main()
