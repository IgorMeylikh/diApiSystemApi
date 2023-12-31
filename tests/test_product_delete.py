import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, DELETE_ONE_PRODUCT_JSON, DELETE_SEVERAL_PRODUCTS_JSON, DELETE_ONE_NOT_ISSET_PRODUCT_JSON, DELETE_SEVERAL_PRODUCTS_ONE_PRODUCT_NOT_ISSET_JSON
from src.baseclasses.response import Response

# Тест на удаление одного товара (с передачей 1 валидного элемента)
@pytest.mark.run(order=60)
def test_delete_one_product_positive():
    response = requests.post(url=SERVICE_URL + DELETE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_ONE_PRODUCT_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    # Возможно после удаление продукта необходимо написать проверку, что продукт действительно удалён.

# Тест на удаление нескольких товаров (с передачей нескольких валидных элементов)
@pytest.mark.run(order=60)
def test_delete_one_product_positive():
    response = requests.post(url=SERVICE_URL + DELETE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_SEVERAL_PRODUCTS_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    # Возможно после удаление продукта необходимо написать проверку, что продукт действительно удалён.

# Тест на удаление несуществующего по GUID товара с передачей 1 валидного элемента
@pytest.mark.run(order=60)
def test_delete_one_not_isset_product_negative():
    response = requests.post(url=SERVICE_URL + DELETE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_ONE_NOT_ISSET_PRODUCT_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')    

# Тест на удаление нескольких товаров, один из них не существует
@pytest.mark.run(order=60)
def test_delete_several_products_one_product_not_isset_negative():
    response = requests.post(url=SERVICE_URL + DELETE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_SEVERAL_PRODUCTS_ONE_PRODUCT_NOT_ISSET_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    test_object.assert_operation_code('400')
    # Возможно после удаление продукта необходимо написать проверку, что продукт действительно удалён.

# Тест на отправку пустого содержимого JSON'a
@pytest.mark.run(order=60)  
def test_delete_product_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + DELETE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')