import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, CREATE_ONE_CATEGORY_JSON, CREATE_REPEAT_ONE_CATEGORY_JSON, CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON, CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON, CREATE_NOT_REQUIRED_JSON, CREATE_NOT_VALID_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

#Тест на создание категории с передачей 1 валидного элемента
@pytest.mark.run(order=10)
def test_create_category_positive():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(CreateCategorySuccessResponse)

#Тест на создание категории, которая уже существует системе
@pytest.mark.run(order=10)
@pytest.mark.skip('Operation code 400 is not isset')
def test_create_repeat_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_REPEAT_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

#Тест на создание нескольких категорий, одна из этих категорий уже существует (вторая в JSON файле)
@pytest.mark.run(order=10)
@pytest.mark.skip('Operation code 400 is not isset')
def test_create_validate_category_and_repeat_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.assert_operation_code('400')    

#Тест на отправку создания новой категории и вторым элементом снова создание этой же категории  
@pytest.mark.run(order=10)  
@pytest.mark.skip('Operation code 400 is not isset')
def test_create_validate_category_and_repeat_himself_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.assert_operation_code('400')   

# Тесты на создание категории когда JSON не валидный: отсутствуют обязательные ключи.
@pytest.mark.run(order=10)  
def test_create_not_required_param_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_NOT_REQUIRED_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')   
# Тесты на создание категории когда JSON не валидный: лишняя запятая после ключа
@pytest.mark.run(order=10)  
def test_create_not_valid_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_NOT_VALID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

