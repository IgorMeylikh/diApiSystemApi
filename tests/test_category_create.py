import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, CREATE_ONE_CATEGORY_JSON, CREATE_REPEAT_ONE_CATEGORY_JSON, CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON, CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON, CREATE_NOT_VALID_JSON, EMPTY_JSON, CREATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON, CREATE_CATEGORY_WITHOUT_NAME_JSON, CREATE_SEVERAL_CATEGORIES_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# Тест на создание категории с передачей 1 валидного элемента
@pytest.mark.run(order=10)
def test_create_category_positive():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(CreateCategorySuccessResponse)

# Тест создания нескольких категорий. Необходимо для проверки работы запроса для создания сразу нескольких категорий, 
# а также в дальнейшем необходима будет проверка по удалению сразу нескольких категорий
@pytest.mark.run(order=10)
def test_create_several_categories_positive():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_SEVERAL_CATEGORIES_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.validateTotalSchema(CreateCategorySuccessResponse)

# Тест на создание категории, которая уже существует системе
@pytest.mark.run(order=10)
# @pytest.mark.skip('Operation code 400 is not isset.')
def test_create_repeat_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_REPEAT_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест на создание нескольких категорий, одна из этих категорий уже существует (вторая в JSON файле)
@pytest.mark.run(order=10)
# @pytest.mark.skip('Operation code 400 is not isset.')
def test_create_validate_category_and_repeat_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.assert_operation_code('400')    

# Тест на отправку создания новой категории и вторым элементом снова создание этой же категории  
@pytest.mark.run(order=10)  
# @pytest.mark.skip('Operation code 400 is not isset.')
def test_create_validate_category_and_repeat_himself_category_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    test_object.assert_operation_code('400')   

# Тесты на создание категории когда JSON не валидный: лишняя запятая после ключа
@pytest.mark.run(order=10)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_create_not_valid_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_NOT_VALID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Тест отправки пустого (без items) JSON'a
@pytest.mark.run(order=10)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_create_category_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')

# Тест отправки JSON'a без обязательного categorySystemId
@pytest.mark.run(order=10)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_create_category_without_category_system_id_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')  

# Тест отправки JSON'a без обязательного name
@pytest.mark.run(order=10)  
# @pytest.mark.skip('Maybe this test is not needed.')
def test_create_category_without_category_system_id_json_negative():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=CREATE_CATEGORY_WITHOUT_NAME_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')    

# Возможно стоит написать тесты так, чтобы при формировании JSON'а на отправку туда передавались переменные, сравнение с которыми будет происходить при получении
# ответа от сервера. То есть будет сравниваться не только схема, но и конкретно какое значение вернулось в параметре. То есть передано было название переменной
# и при ответе в теле значение по данному ключу должно совпадать с переменной
# Создаём категорию, передаём JSON вида {"items":[{"categorySystemid": "meylikh_1_id","name": "meylikh_1_name"}]} , но вот эти categorySystemid и name должны быть переданы
# как переменные categorySystemidForCreate = "meylikh_1_id", nameForCreate = "meylikh_1_name" и в ответе надо смотреть, что содержимое по ключу categorySystemId равно содержимому
# переменной categorySystemidForCreate, а по ключу name переменной nameForCreate
# Это всё должно быть в тесте. Возможно поместить в метод класса, который проверяет возвращаемый ответ.
# {
# 	"responses": {
# 		"201": [
# 			{
# 				"description": "Created items.",
# 				"items": [
# 					{
# 						"categoryId": "5c5fa411-8321-4d15-b5d5-a92000979c32",
# 						"categorySystemId": "meylikh_1_id",
# 						"name": "meylikh_1_name"
# 					}
# 				]
# 			}
# 		]
# 	}
# }
# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

