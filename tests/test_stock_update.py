import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, UPDATE_ONE_PRODUCT_WITH_OPTIONAL_JSON, UPDATE_SEVERAL_PRODUCTS_JSON, UPDATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON, EMPTY_JSON, UPDATE_ONE_PRODUCT_ONLY_NAME_JSON, UPDATE_ONE_PRODUCT_ONLY_SKU_JSON, UPDATE_ONE_PRODUCT_ONLY_TYPE_JSON, UPDATE_ONE_PRODUCT_ONLY_CATEGORY_SYSTEM_ID_JSON, UPDATE_ONE_PRODUCT_ONLY_PREVIEW_LINK_JSON, UPDATE_PRODUCT_NOT_VALID_JSON, UPDATE_PRODUCT_NOT_ISSET_PRODUCT_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление товара с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=80)
def test_update_product_with_optional_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление нескольких продуктов
@pytest.mark.run(order=80)
def test_update_product_several_products_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_SEVERAL_PRODUCTS_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200') 

# Тест на обновление товара с передачей только name из необязательных
@pytest.mark.run(order=80)
def test_update_product_with_only_name_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_ONLY_NAME_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление товара с передачей только sku из необязательных
@pytest.mark.run(order=80)
def test_update_product_with_only_sku_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_ONLY_SKU_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление товара с передачей только type из необязательных
@pytest.mark.run(order=80)
def test_update_product_with_only_type_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_ONLY_TYPE_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление товара с передачей только categorySystemId из необязательных
@pytest.mark.run(order=80)
def test_update_product_with_only_category_system_id_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_ONLY_CATEGORY_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление товара с передачей только categorySystemId из необязательных
@pytest.mark.run(order=80)
def test_update_product_with_only_preview_link_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_ONLY_PREVIEW_LINK_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    
# Тест на обновление товара с передачей 1 валидного элемента без указания хотя бы одного необязательного параметра
@pytest.mark.run(order=80)
def test_update_product_without_optional_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Тест на обновление товара с передачей пустого JSON
@pytest.mark.run(order=80)
def test_update_product_with_empty_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тесты на обновление продукта когда JSON не валидный: лишняя запятая после ключа
@pytest.mark.run(order=80)
def test_update_product_not_valid_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_PRODUCT_NOT_VALID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')          

# Тесты на обновление несуществующего продукта
@pytest.mark.run(order=80)
def test_update_product_not_isset_product_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_PRODUCT_NOT_ISSET_PRODUCT_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')   

# Тест на обновление нескольких продуктов, когда один из них не существует

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

