import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, CREATE_ONE_WAREHOUSE, CREATE_SEVERAL_WAREHOUSES
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание одного склада
@pytest.mark.run(order=80)
def test_create_warehouse_one_warehouse():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание нескольких складов
@pytest.mark.run(order=80)
def test_create_warehouse_several_warehouses():
    response = requests.post(url=SERVICE_URL + CREATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_WAREHOUSES)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание одного склада, уже существующего в системе
# Тест на создание нескольких складов, один из них уже есть в системе
# Тест на создание нескольких складов, все есть в системе    


# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

