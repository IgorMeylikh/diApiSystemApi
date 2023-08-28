import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, GETTING_PRODUCTS_PAGE, EXTERNAL_LOGIN, EXTERNAL_PASSWORD, EXTERNAL_HEADERS, EMPTY_JSON, GET_ALL_PRODUCTS
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на получение всех товаров
@pytest.mark.run(order=70)
def test_get_products_positive():
    response = requests.post(url=SERVICE_URL + GETTING_PRODUCTS_PAGE, auth=HTTPBasicAuth(EXTERNAL_LOGIN, EXTERNAL_PASSWORD), headers=EXTERNAL_HEADERS, json=GET_ALL_PRODUCTS)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на отправку пустого содержимого JSON'a
@pytest.mark.run(order=70)
def test_get_products_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + GETTING_PRODUCTS_PAGE, auth=HTTPBasicAuth(EXTERNAL_LOGIN, EXTERNAL_PASSWORD), headers=EXTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')