import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_PRICES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, EMPTY_JSON, UPDATE_PRICE_ONE_JSON, UPDATE_PRICE_SEVERAL_PRICES_JSON, UPDATE_PRICE_ONE_NOT_ISSET_PRODUCT_SYSTEM_ID_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление цены с передачей 1 валидного элемента 
@pytest.mark.run(order=90)
def test_update_price_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_PRICE_ONE_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# # Тест на обновление нескольких цен
@pytest.mark.run(order=90)
def test_update_price_several_prices_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_PRICE_SEVERAL_PRICES_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# # Тест на обновление цены с передачей 1 невалидного элемента (такого GUID товара не существует)
@pytest.mark.run(order=90)
def test_update_price_not_isset_product_system_id_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_PRICE_ONE_NOT_ISSET_PRODUCT_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# # Тест на обновление нескольких остатков когда один из товаров (productSystemId) не существует 
# @pytest.mark.run(order=80)
# def test_update_stock_several_one_not_isset_product_system_id_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_SEVERAL_STOCKS_ONE_NOT_ISSET_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление остатка без передачи обязательного количества (quantity)
# @pytest.mark.run(order=80)
# def test_update_stock_without_quantity_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_ONE_WITHOUT_QUANTITY_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление остатка без передачи обязательного id склада (warehouseId)
# @pytest.mark.run(order=80)
# def test_update_stock_without_warehouse_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_ONE_WITHOUT_WAREHOUSE_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление остатка без передачи обязательного productSystemId
# @pytest.mark.run(order=80)
# def test_update_stock_without_product_system_id_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_ONE_WITHOUT_PRODUCT_SYSTEM_ID_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление нескольких остатков без передачи у одного и них обязательного количества (quantity)
# @pytest.mark.run(order=80)
# def test_update_stock_several_without_quantity_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_SEVERAL_STOCKS_SECOND_WITHOUT_QUANTITY_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление нескольких остатков без передачи у одного и них обязательного id склада (warehouseId)
# @pytest.mark.run(order=80)
# def test_update_stock_several_without_warehouse_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_SEVERAL_STOCKS_SECOND_WITHOUT_WAREHOUSE_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление нескольких остатков без передачи у одного и них обязательного productSystemId
# @pytest.mark.run(order=80)
# def test_update_stock_several_without_product_system_id_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_SEVERAL_STOCKS_SECOND_WITHOUT_PRODUCT_SYSTEM_ID_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление остаткв с передачей пустого JSON
@pytest.mark.run(order=90)
def test_update_price_with_empty_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# # Тест на обновление остатка когда передан несуществующий склад (warehouseId)
# @pytest.mark.run(order=80)
# def test_update_stock_with_not_isset_warehouse_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_WITH_NOT_ISSET_WAREHOUSE_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')

# # Тест на обновление остатка когда передана буква в количестве товара (quantity)
# @pytest.mark.run(order=80)
# def test_update_stock_with_not_isset_warehouse_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_WITH_QUANTITY_NOT_DIGIT_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')    

# # Тест на обновление остатка когда передано дробное число в количестве товара (quantity)
# @pytest.mark.run(order=80)
# def test_update_stock_with_not_isset_warehouse_negative():
#     response = requests.post(url=SERVICE_URL + UPDATE_STOCKS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=UPDATE_STOCK_WITH_QUANTITY_FRACTIONAL_JSON)
#     test_object = Response(response)
#     test_object.assert_status_code(200)
#     test_object.assert_operation_code('400')   

# Тест на обновление цены у товара, который принадлежит другой учётной системе

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

