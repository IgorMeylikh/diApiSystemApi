import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, CREATE_ONE_SUBCATEGORY_JSON, CREATE_REPEAT_ONE_SUBCATEGORY_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_subcategory_pydantic import CreateSubcategorySuccessResponse, CreateSubcategorySuccessStatusCode, CreateSubcategorySuccessItem

# Тест на создание подкатегории с передачей 1 валидного элемента
@pytest.mark.run(order=15)
def test_create_subcategory_positive():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_SUBCATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(CreateSubcategorySuccessResponse)    

# Тест на создание подкатегории, которая уже существует системе
@pytest.mark.run(order=15)
@pytest.mark.skip('Operation code 400 is not isset')
def test_create_repeat_subcategory_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_REPEAT_ONE_SUBCATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')    

# Тест на создание подкатегории с указанием несуществующей родительской категории.
# На текущий момент отправка запроса возвращает валидный результат, но по факту не добавляется категория



