import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, UPDATE_ONE_CATEGORY_JSON, UPDATE_ONE_NOT_ISSET_CATEGORY_JSON, UPDATE_NOT_REQUIRED_JSON, UPDATE_NOT_VALID_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

#Тест на обновление категории с передачей 1 валидного элемента
@pytest.mark.run(order=20)
def test_update_category_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    test_object.validateTotalSchema(CreateCategorySuccessResponse)

# Тесты на обновление категории когда JSON не валидный: отсутствуют обязательные ключи.
@pytest.mark.run(order=20)
def test_update_not_required_param_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_NOT_REQUIRED_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тесты на обновление категории когда JSON не валидный: лишняя запятая после ключа
@pytest.mark.run(order=20)
@pytest.mark.skip('Maybe this test is not needed.')
def test_update_not_valid_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_NOT_VALID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тесты на обновление несуществующей категории
@pytest.mark.run(order=20)
@pytest.mark.skip('Operation code 400 is not isset.')
def test_update_not_isset_category_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_NOT_ISSET_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Написать тесты когда не отправлен нужный ключ в JSON'e

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse
