import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, UPDATE_PRICES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, UPDATE_PRICE_ONE_JSON, UPDATE_PRICE_WITH_PRICE_AS_FRACTIONAL_NUMBER_DOT_JSON, UPDATE_PRICE_SEVERAL_PRICES_JSON, UPDATE_STOCK_WITH_PRICE_AS_STRING_JSON, UPDATE_PRICE_ONE_NOT_ISSET_PRODUCT_SYSTEM_ID_JSON, UPDATE_PRICE_SEVERAL_PRICES_ONE_NOT_ISSET_JSON, UPDATE_PRICE_WITHOUT_PRODUCT_SYSTEM_ID_JSON, UPDATE_PRICE_WITHOUT_PRICE_JSON, UPDATE_PRICE_WITH_PRICE_AS_LETTERS_JSON, UPDATE_PRICE_WITH_PRICE_AS_FRACTIONAL_NUMBER_COMMA_JSON, UPDATE_PRICE_WITH_PRICE_AS_SYMBOL_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на обновление цены с передачей 1 валидного элемента 
@pytest.mark.run(order=150)
def test_update_price_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_ONE_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление цены когда передано дробное число с точкой в цене
@pytest.mark.run(order=150)
def test_update_price_with_price_as_fractional_number_comma_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITH_PRICE_AS_FRACTIONAL_NUMBER_DOT_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    
# Тест на обновление нескольких цен
@pytest.mark.run(order=150)
def test_update_price_several_prices_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_SEVERAL_PRICES_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на обновление цены когда передана цена как строка, но содержащая число. "1000"
@pytest.mark.run(order=150)
def test_update_price_with_price_as_string_positive():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_STOCK_WITH_PRICE_AS_STRING_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')     

# Тест на обновление цены с передачей 1 невалидного элемента (такого GUID товара не существует)
@pytest.mark.run(order=150)
def test_update_price_not_isset_product_system_id_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_ONE_NOT_ISSET_PRODUCT_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление нескольких цен когда один из товаров не существует (такого GUID товара не существует)
@pytest.mark.run(order=150)
def test_update_price_several_prices_one_not_isset_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_SEVERAL_PRICES_ONE_NOT_ISSET_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')
    test_object.assert_operation_code('400')

# Тест на обновление цены когда в JSON не передан обязательный productSystemId
@pytest.mark.run(order=150)
def test_update_price_without_product_system_id_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITHOUT_PRODUCT_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')   

# Тест на обновление цены когда в JSON не передан обязательный price
@pytest.mark.run(order=150)
def test_update_price_without_price_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITHOUT_PRICE_JSON )
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')   
    
# Тест на обновление цены с передачей пустого JSON
@pytest.mark.run(order=150)
def test_update_price_with_empty_json_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на обновление цены когда передана буква(-ы) в цене
@pytest.mark.run(order=150)
def test_update_price_with_price_as_letter_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITH_PRICE_AS_LETTERS_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400') 
   
# Тест на обновление цены когда передано дробное число с запятой в цене
@pytest.mark.run(order=150)
def test_update_price_with_price_as_fractional_number_comma_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITH_PRICE_AS_FRACTIONAL_NUMBER_COMMA_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')    

# Тест на обновление цены когда передан какой-либо спецсимвол в параметре цены
# В будущем можно написать генерацию параметра JSON, когда спецсимвол будет подставляться из списка заранее выделенных спецсимволов.
# Пример special_characters = '/"№;%:?!@#$%&^*()'. Но, наверно, нафиг это не надо
@pytest.mark.run(order=150)
def test_update_price_with_price_as_symbol_negative():
    response = requests.post(url=SERVICE_URL + UPDATE_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=UPDATE_PRICE_WITH_PRICE_AS_SYMBOL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')   

# Тест на обновление цены у нескольких товаров, к одному из которых не передан параметр price

# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

