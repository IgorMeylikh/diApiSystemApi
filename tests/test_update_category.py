import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, UPDATE_ONE_CATEGORY_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

#Тест на обновление категории с передачей 1 валидного элемента
@pytest.mark.run(order=15)
def test_create_category_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(CreateCategorySuccessResponse)

# Тесты на обновление категории когда JSON не валидный: отсутствуют обязательные ключи; лишняя запятая после ключа и т.д.
# Тесты на обновление несуществующей категории
