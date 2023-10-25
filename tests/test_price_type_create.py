import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_PRICE_TYPES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, CREATE_ONE_PRICE_TYPE_WITH_OPTIONAL, CREATE_ONE_PRICE_TYPE_WITHOUT_OPTIONAL, CREATE_SEVERAL_PRICE_TYPES_WITH_OPTIONAL
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание одного вида цен с передачей необязательных параметров
@pytest.mark.run(order=110)
def test_create_one_price_type_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_OPTIONAL)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание одного вида цен без необязательных параметров
@pytest.mark.run(order=110)
def test_create_one_price_type_without_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITHOUT_OPTIONAL)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание нескольких видов цен с передачей обязательных и необязательных параметров
@pytest.mark.run(order=110)
def test_create_several_price_types_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_PRICE_TYPES_WITH_OPTIONAL)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')   

# Тест на создание одного вида цен когда priceTypeSystemId не передан
# Тест на создание одного вида цен когда name не передан
# Тест на создание одного вида цен когда currency не передан
# Тест на создание одного вида цен когда priceTypeSystemId передан как int 
# Тест на создание одного вида цен когда name передан как int 
# Тест на создание одного вида цен когда currency передан как string
# Тест на создание одного вида цен когда priceTypeSystemId передан пустым
# Тест на создание одного вида цен когда name передан пустым 
# Тест на создание одного вида цен когда currency передан пустым
# Тест на создание одного вида цен когда currency передан дробным числом
    

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=110)  
def test_create_price_type_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  


    # Здесь бы добавить ещё проверку, что в ответе нет 200, 201 статусов по созданию складов.  

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

