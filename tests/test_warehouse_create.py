import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, CREATE_ONE_WAREHOUSE, CREATE_SEVERAL_WAREHOUSES, CREATE_ISSET_WAREHOUSE_SYSTEM_ID, CREATE_SEVERAL_ONE_ISSET_WAREHOUSE_SYSTEM_ID, CREATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_SYSTEM_ID, CREATE_ONE_WAREHOUSE_WITHOUT_NAME, CREATE_ONE_WAREHOUSE_WAREHOUSE_SYSTEM_ID_AS_INT
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание одного склада
@pytest.mark.run(order=80)
def test_create_warehouse_one_warehouse_positive():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание нескольких складов
@pytest.mark.run(order=80)
def test_create_warehouse_several_warehouses_positive():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_WAREHOUSES)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание одного склада, уже существующего в системе
@pytest.mark.run(order=80)
def test_create_warehouse_isset_warehouse_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ISSET_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание нескольких складов, один из них уже есть в системе
@pytest.mark.run(order=80)
def test_create_warehouse_several_one_isset_warehouse_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_ONE_ISSET_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.assert_operation_code('400')

# Тест на создание нескольких складов, все есть в системе    
@pytest.mark.run(order=80)
def test_create_warehouse_several_isset_warehouses_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_ONE_ISSET_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')
    # Возможно в тесты стоит дописать проверку каких кодов не должно быть в ответе, а то пройдёт 201 как успешная, 
    # но ещё там 400 каким-то образом. Или наоборот проверяем, что только 400, а окажется, что один из добавляемых элементов прошёл успешно, хотя не должен был

# Тест на создание одного склада, без указания идентификатора
@pytest.mark.run(order=80)
def test_create_warehouse_one_warehouse_without_warehouse_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание одного склада, без указания имени
@pytest.mark.run(order=80)
def test_create_warehouse_one_warehouse_without_name_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WAREHOUSE_WITHOUT_NAME)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=80)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_create_warehouse_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')      

# Тест на создание одного склада, где идентификатор склада передан как число
@pytest.mark.run(order=80)
def test_create_warehouse_one_warehouse_warehouse_system_id_is_int():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WAREHOUSE_WAREHOUSE_SYSTEM_ID_AS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse
