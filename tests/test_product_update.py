import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление товара с передачей 1 валидного элемента с указанием необязательных ключей
# @pytest.mark.run(order=40)
# def test_update_product_with_optional_positive():
#     response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('201')

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

