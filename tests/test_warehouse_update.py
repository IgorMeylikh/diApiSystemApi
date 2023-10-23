import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, UPDATE_ONE_WAREHOUSE, UPDATE_SEVERAL_WAREHOUSES, UPDATE_ONE_NOT_ISSET_WAREHOUSE, UPDATE_SEVERAL_WAREHOUSES_ONE_NOT_ISSET, UPDATE_WAREHOUSE_SYSTEM_ID_IS_INT, UPDATE_ONE_WAREHOUSE_NAME_WAREHOUSE_IS_INT, UPDATE_SEVERAL_WAREHOUSES_ONE_WAREHOUSE_SYSTEM_ID_IS_INT, UPDATE_SEVERAL_WAREHOUSES_ONE_WAREHOUSE_NAME_IS_INT, UPDATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_SYSTEM_ID, UPDATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_NAME, UPDATE_SEVERAL_WAREHOUSES_ONE_WITHOUT_WAREHOUSE_SYSTEM_ID, UPDATE_SEVERAL_WAREHOUSES_ONE_WITHOUT_WAREHOUSE_NAME
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление одного склада
@pytest.mark.run(order=90)
def test_update_warehouse_one_warehouse_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление нескольких складов
@pytest.mark.run(order=90)
def test_update_warehouse_several_warehouses_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление одного несуществующего склада
@pytest.mark.run(order=90)
def test_update_warehouse_one_not_isset_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_NOT_ISSET_WAREHOUSE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких складов, один не существует
@pytest.mark.run(order=90)
def test_update_warehouse_several_warehouses_one_not_isset_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES_ONE_NOT_ISSET)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')    

# Тест на обновление склада когда идентификатор как число
@pytest.mark.run(order=90)
def test_update_warehouse_warehouse_system_id_is_int_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_WAREHOUSE_SYSTEM_ID_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление склада когда имя как число
@pytest.mark.run(order=90)
def test_update_warehouse_name_warehouse_is_int_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_WAREHOUSE_NAME_WAREHOUSE_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких складов когда у одного идентификатор как число
@pytest.mark.run(order=90)
def test_update_several_warehouses_one_warehouse_system_id_is_int_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES_ONE_WAREHOUSE_SYSTEM_ID_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких складов когда у одного имя как число
@pytest.mark.run(order=90)
def test_update_several_warehouses_one_warehouse_name_is_int_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES_ONE_WAREHOUSE_NAME_IS_INT)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление склада когда не передан идентификатор
@pytest.mark.run(order=90)
def test_update_warehouse_withous_warehouse_system_id_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление склада когда не передано имя
@pytest.mark.run(order=90)
def test_update_warehouse_without_warehouse_name_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_ONE_WAREHOUSE_WITHOUT_WAREHOUSE_NAME)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких складов когда у одного не передан идентификатор
@pytest.mark.run(order=90)
def test_update_several_warehouses_one_without_warehouse_system_id_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES_ONE_WITHOUT_WAREHOUSE_SYSTEM_ID)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких складов когда у одного не передано имя
@pytest.mark.run(order=90)
def test_update_several_warehouses_one_without_warehouse_name_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_SEVERAL_WAREHOUSES_ONE_WITHOUT_WAREHOUSE_NAME)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест когда передан пустой запрос
@pytest.mark.run(order=90)  
def test_update_warehouse_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

