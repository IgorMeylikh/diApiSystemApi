import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON, CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON, CREATE_SEVERAL_PRODUCTS_WITH_OPTIONAL_JSON, EMPTY_JSON, CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON, CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON, CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON, CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON, CREATE_SEVERAL_PRODUCTS_WITHOUT_OPTIONAL_JSON, CREATE_ONE_SERVICE_WITH_OPTIONAL_JSON, CREATE_ONE_WORK_WITH_OPTIONAL_JSON, CREATE_ONE_PRODUCT_IN_NOT_ISSET_CATEGORY_SYSTEM_ID_JSON, CREATE_ONE_PRODUCT_WITH_REPEAT_GUID_JSON, CREATE_ONE_PRODUCT_WITH_REPEAT_SKU_JSON, CREATE_ONE_SERVICE_WITH_JS_JSON, CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_GUID_WITH_OPTIONAL_JSON, CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_SKU_WITH_OPTIONAL_JSON, CREATE_ONE_PRODUCT_WITH_MAX_STOCK_RANGE_AS_STRING_JSON, CREATE_ONE_PRODUCT_WITH_MAX_STOCK_RANGE_IS_STRING_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание товара с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # print(test_object.response['201'])
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание товара с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_without_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание нескольких товаров с необязательными параметрами
@pytest.mark.run(order=40)
def test_create_product_several_products_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание нескольких товаров без необязательных параметров
@pytest.mark.run(order=40)
def test_create_product_several_products_without_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITHOUT_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')    
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание записи с типом service с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_service_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_SERVICE_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание записи с типом work с передачей 1 валидного элемента с указанием необязательных ключей
@pytest.mark.run(order=40)
def test_create_product_work_with_optional_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_WORK_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.

# Тест на создание товара с передачей 1 валидного элемента с указанием несуществующей категории
@pytest.mark.run(order=40)
def test_create_product_in_not_isset_category_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_IN_NOT_ISSET_CATEGORY_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара с уже добавленным ранее GUID
@pytest.mark.run(order=40)
def test_create_product_repeat_guid_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITH_REPEAT_GUID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара с уже добавленным SKU    
@pytest.mark.run(order=40)
def test_create_product_repeat_sku_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITH_REPEAT_SKU_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')

# Тест на создание нескольких товаров, один из которых с уже добавленным ранее GUID
@pytest.mark.run(order=40)
def test_create_product_several_products_one_repeat_guid_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_GUID_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    # Возможно после добавления продукта необходимо написать проверку, что продукт действительно добавлен.
    test_object.assert_operation_code('400')

# Тест на создание нескольких товаров, один из которых с уже добавленным ранее SKU
@pytest.mark.run(order=40)
def test_create_product_several_products_one_repeat_sku_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_SKU_WITH_OPTIONAL_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    
# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=10)  
def test_create_product_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного productSystemId
@pytest.mark.run(order=40)
def test_create_product_without_product_system_id_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного name
@pytest.mark.run(order=40)
def test_create_product_without_name_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного sku
@pytest.mark.run(order=40)
def test_create_product_without_sku_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание товара без указания обязательного type
@pytest.mark.run(order=40)
def test_create_product_without_type_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест с созданием товара когда в качестве одного из значений параметра передаётся JS. На примере картинки для товара
@pytest.mark.run(order=40)
def test_create_product_work_with_js_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_SERVICE_WITH_JS_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест позитивный на передачу в maxStockRange числа в виде строки.
@pytest.mark.run(order=40)
def test_create_product_max_stock_range_as_string_positive():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITH_MAX_STOCK_RANGE_AS_STRING_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')


# Тест негативный на передачу в maxStockRange строки (Пример: abcde).
@pytest.mark.run(order=40)
def test_create_product_max_stock_range_is_string_negative():
    response = requests.post(url=SERVICE_URL + CREATE_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=CREATE_ONE_PRODUCT_WITH_MAX_STOCK_RANGE_IS_STRING_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')


# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

