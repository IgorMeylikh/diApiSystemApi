import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, EMPTY_JSON, DELETE_ONE_CATEGORY_JSON, DELETE_SEVERAL_CATEGORIES_JSON, DELETE_ONE_NOT_ISSET_CATEGORY_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

#Тест на удаление категории с передачей 1 валидного элемента
@pytest.mark.run(order=30)
def test_delete_one_category_positive():
    response = requests.post(url=SERVICE_URL + DELETE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=DELETE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

#Тест на удаление категории с передачей 1 валидного элемента
@pytest.mark.run(order=30)
def test_delete_one_not_isset_category_negative():
    response = requests.post(url=SERVICE_URL + DELETE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=DELETE_ONE_NOT_ISSET_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')    

#Тест на удаление нескольких категорий
@pytest.mark.run(order=30)
def test_delete_several_categories_positive():
    response = requests.post(url=SERVICE_URL + DELETE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=DELETE_SEVERAL_CATEGORIES_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на отправку пустого содержимого JSON'a
@pytest.mark.run(order=30)  
def test_delete_category_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + DELETE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')