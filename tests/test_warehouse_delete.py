import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, DELETE_ONE_WAREHOUSE, DELETE_SEVERAL_WAREHOUSES, DELETE_ONE_NOT_ISSET_WAREHOUSE,  DELETE_SEVERAL_WAREHOUSES_ONE_NOT_ISSSET
from src.baseclasses.response import Response

# Тест на удаление одного склада (с передачей 1 валидного элемента)
@pytest.mark.run(order=100)
def test_delete_one_product_positive():
    response = requests.post(url=SERVICE_URL + DELETE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_ONE_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на удаление нескольких складов (все существуют)
@pytest.mark.run(order=100)
def test_delete_warehouse_several_warehouses_positive():
    response = requests.post(url=SERVICE_URL + DELETE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_SEVERAL_WAREHOUSES)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')    

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=100)  
def test_delete_warehouse_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + DELETE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')      

# Тест удаления несуществующего склада
@pytest.mark.run(order=100)  
def test_delete_warehouse_not_isset():
    response = requests.post(url=SERVICE_URL + DELETE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_ONE_NOT_ISSET_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Тест на удаление нескольких складов, один не существует
@pytest.mark.run(order=100)
def test_delete_warehouse_several_one_not_isset_negative():
    response = requests.post(url=SERVICE_URL + DELETE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_SEVERAL_WAREHOUSES_ONE_NOT_ISSSET)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  
    test_object.assert_operation_code('200')  