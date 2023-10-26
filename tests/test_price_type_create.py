import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_PRICE_TYPES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, CREATE_ONE_PRICE_TYPE_WITH_OPTIONAL, CREATE_ONE_PRICE_TYPE_WITHOUT_OPTIONAL, CREATE_SEVERAL_PRICE_TYPES_WITH_OPTIONAL, CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_AS_STRING, CREATE_ONE_PRICE_TYPE_WITHOUT_PRICE_TYPE_SYSTEM_ID, CREATE_ONE_PRICE_TYPE_WITHOUT_NAME, CREATE_ONE_PRICE_TYPE_WITHOUT_CURRENCY, CREATE_ONE_PRICE_TYPE_WITH_PRICE_TYPE_SYSTEM_ID_IS_INT, CREATE_ONE_PRICE_TYPE_WITH_NAME_IS_INT, CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_IS_STRING, CREATE_ONE_PRICE_TYPE_WITH_PRICE_TYPE_SYSTEM_ID_IS_EMPTY, CREATE_ONE_PRICE_TYPE_WITH_NAME_IS_EMPTY, CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_IS_EMPTY
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

# Тест на создание одного вида цен где currency передано числом в виде строки
@pytest.mark.run(order=110)
def test_create_one_price_type_with_name_as_string_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_AS_STRING)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание одного вида цен когда priceTypeSystemId не передан
@pytest.mark.run(order=110)
def test_create_one_price_type_without_price_type_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITHOUT_PRICE_TYPE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда name не передан
@pytest.mark.run(order=110)
def test_create_one_price_type_without_name_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITHOUT_NAME)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда currency не передан
@pytest.mark.run(order=110)
def test_create_one_price_type_without_currency_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITHOUT_CURRENCY)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')
    
# Тест на создание одного вида цен когда priceTypeSystemId передан как int 
@pytest.mark.run(order=110)
def test_create_one_price_type_with_price_type_system_id_is_int_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_PRICE_TYPE_SYSTEM_ID_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда name передан как int 
@pytest.mark.run(order=110)
def test_create_one_price_type_with_name_is_int_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_NAME_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда currency передан как string (Именно "ываыа", не "643")
@pytest.mark.run(order=110)
def test_create_one_price_type_with_currency_is_int_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_IS_STRING)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда priceTypeSystemId передан пустым
@pytest.mark.run(order=110)
def test_create_one_price_type_with_price_type_system_id_is_empty_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_PRICE_TYPE_SYSTEM_ID_IS_EMPTY)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда name передан пустым 
@pytest.mark.run(order=110)
def test_create_one_price_type_with_name_is_empty_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_NAME_IS_EMPTY)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда currency передан пустым
@pytest.mark.run(order=110)
def test_create_one_price_type_with_currency_is_empty_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRICE_TYPE_WITH_CURRENCY_IS_EMPTY)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного вида цен когда currency передан дробным числом
    

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=110)  
def test_create_price_type_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  


    

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

