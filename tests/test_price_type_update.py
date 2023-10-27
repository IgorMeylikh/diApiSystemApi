import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_PRICE_TYPES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, UPDATE_ONE_PRICE_TYPE, UPDATE_SEVERAL_PRICE_TYPES
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление одного вида цен
@pytest.mark.run(order=120)
def test_update_one_price_type_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_PRICE_TYPE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление нескольких видов цен
@pytest.mark.run(order=120)
def test_update_several_price_types_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_PRICE_TYPES)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление вида цен когда не передан priceTypeSystemId
# Тест на обновление вида цен когда не передан name
# Тест на обновление вида цен когда не передан currency
# Тест на обновление вида цен когда priceTypeSystemId передан как int
# Тест на обновление вида цен когда name передан как int
# Тест на обновление вида цен когда в currency передано число как string (Пример "643")
# Тест на обновление вида цен когда в currency передана строка string (Пример "ываыа")

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=120)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_update_price_type_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Может добавить ещё такие? Имеет ли смысл...
# Тест на обновление нескольких видов цен когда у одного не передан priceTypeSystemId
# Тест на обновление нескольких видов цен когда у одного не передан name
# Тест на обновление нескольких видов цен когда у одного не передан currency
# Тест на обновление нескольких видов цен когда у одного priceTypeSystemId передан как int
# Тест на обновление нескольких видов цен когда у одного name передан как int
# Тест на обновление нескольких видов цен когда у одного в currency передано число как string (Пример "643")
# Тест на обновление нескольких видов цен когда у одного в currency передана строка string (Пример "ываыа")

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

