import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON, CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON, EMPTY_JSON, CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON, CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON, CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON, CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON, CREATE_SEVERAL_PRODUCTS_WITH_OPTIONAL_JSON, CREATE_SEVERAL_PRODUCTS_WITHOUT_OPTIONAL_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание товара с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание товара с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_without_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание товара без указания обязательного productSystemId
@pytest.mark.run(order=40)
def test_create_product_without_product_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного name
@pytest.mark.run(order=40)
def test_create_product_without_name_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного sku
@pytest.mark.run(order=40)
def test_create_product_without_sku_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного type
@pytest.mark.run(order=40)
def test_create_product_without_type_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание нескольких товаров с необязательными параметрами
@pytest.mark.run(order=40)
def test_create_several_products_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание нескольких товаров без необязательных параметров
@pytest.mark.run(order=40)
def test_create_several_products_without_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITHOUT_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')    

# Написать тесты, которые будут добавлять не только с type = product, но также ещё service, work 

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

