import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import *
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import SuccessResponse, SuccessItem, SuccessStatusCode

#Тест на создание категории с передачей 1 валидного элемента
@pytest.mark.run(order=10)
def test_create_category(fixture_check_available_endpoint):
    if fixture_check_available_endpoint == True: 
        response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=ONE_CATEGORY_JSON)
        test_object = Response(response)
        # test_object.assert_status_code(200)
        test_object.assert_operation_code('201')
        test_object.validateTotalSchema(SuccessResponse)

#Тест на создание категории, которая уже существует системе

@pytest.mark.run(order=10)
def test_create_repeat_category(fixture_check_available_endpoint):
    if fixture_check_available_endpoint == True: 
        response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=REPEAT_ONE_CATEGORY_JSON)
        test_object = Response(response)
        # test_object.assert_status_code(200)
        test_object.assert_operation_code('400')

#Тест на создание нескольких категорий, одна из этих категорий уже существует (вторая в JSON файле)
@pytest.mark.run(order=10)
def test_create_validate_category_and_repeat_category(fixture_check_available_endpoint):
    if fixture_check_available_endpoint == True: 
        response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON)
        test_object = Response(response)
        # test_object.assert_status_code(200)
        test_object.assert_operation_code('201')
        test_object.assert_operation_code('400')    

#Тест на отправку создания новой категории и вторым элементом снова создание этой же категории  
@pytest.mark.run(order=10)  
def test_create_validate_category_and_repeat_himself_category(fixture_check_available_endpoint):
    if fixture_check_available_endpoint == True: 
        response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON)
        test_object = Response(response)
        # test_object.assert_status_code(200)
        test_object.assert_operation_code('201')
        test_object.assert_operation_code('400')   






