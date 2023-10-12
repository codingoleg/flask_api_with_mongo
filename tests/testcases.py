from config import BODY, HEADERS, URL_FIND, URL_FIND2, URL_PROBLEMS

# data_0 == data_1. data_2 идентична data_0 и data_1 по значению, но не по
# порядку. BODY data_3 и HEADERS data_4 имеют одинаковое значение "ABC": "123".
data_0 = {BODY: {"a": 1, "b": "2.2", "test_data": "true"}, HEADERS: {"hello": "world", "c": "3"}}
data_1 = {BODY: {"a": 1, "b": "2.2", "test_data": "true"}, HEADERS: {"hello": "world", "c": "3"}}
data_2 = {BODY: {"b": "2.2", "a": 1, "test_data": "true"}, HEADERS: {"c": "3", "hello": "world"}}
data_3 = {BODY: {"ABC": "123", "z": "6", "test_data": "true"}, HEADERS: {"a": "5", "S": "9"}}
data_4 = {BODY: {"a": 1, "h": "600", "test_data": "true"}, HEADERS: {"a": "1", "ABC": "123"}}

query_0 = {"a": 1, "b": "2.2"}  # есть только в body
query_1 = {"S": "9"}  # есть только в headers
query_2 = {"o": "2", "S": "9"}  # "o": "2" нет нигде, "S": "9" есть в headers
query_3 = {"ABC": "123"}  # есть и в body, и в headers
query_4 = {"u": "0"}  # нет нигде

data_0_1_hash = 'b2e5857f28db5467cc742aca343912ed390c3f5452f69a8fd68f4d45bdf5cf21'
data_2_hash = 'b2e5857f28db5467cc742aca343912ed390c3f5452f69a8fd68f4d45bdf5cf21'
data_3_hash = 'c827e3b1368ee2048099d1228cc89d77dcae09e7e5bd3bae13ba40e9f773ab26'
data_4_hash = 'c1d855c5e84d949cdc9d7389e3685479819a4520defb6db44d2c617cd1d5099d'
invalid_hash = 'e6bd998c6743963d679514834033cfbae2afcabb25e9af7'  # несуществующий
