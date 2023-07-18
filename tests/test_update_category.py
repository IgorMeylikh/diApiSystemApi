import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, ONE_CATEGORY_JSON, REPEAT_ONE_CATEGORY_JSON, VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON, VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import SuccessResponse, SuccessItem, SuccessStatusCode

#Тест на создание категории с передачей 1 валидного элемента
@pytest.mark.run(order=10)
def test_create_category_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(SuccessResponse)