import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, GETTING_STOCKS_PAGE, EXTERNAL_LOGIN, EXTERNAL_PASSWORD, EXTERNAL_HEADERS, EMPTY_JSON, GET_STOCKS_JSON, GET_STOCKS_TWO_ITEM_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode

# !!!!!!! Эти тесты могут падать, если изменятся productId. Поэтому необходимо написать либо предварительные тесты, чтобы узнать productId остатков, которые доступны и их количество
# А лучше при создании номенклатур собирать коллекцию productId, из которой затем формировать JSON'ы.
# Возможно понадобится установка лимитов путём запуска WebUI и выставления лимитов для тестового контрагента. Надо поискать выставляются ли где лимиты для контрагента через API 

# Тест на получение остатка с передачей 1 валидного элемента 
# !!!!!!! В данный тест надо дописать проверку возвращаемых данных. Необходимо проверять правильные ли данные в ответе, а также верно ли запрашиваемое количество с тем,
# что задумано для теста
@pytest.mark.run(order=100)
def test_get_stocks_positive():
    response = requests.post(url=SERVICE_URL + GETTING_STOCKS_PAGE, auth=HTTPBasicAuth(EXTERNAL_LOGIN, EXTERNAL_PASSWORD), headers=EXTERNAL_HEADERS, json=GET_STOCKS_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

# Тест на получение остатка с передачей 2 валидных элементов 
# !!!!!!! В данный тест надо дописать проверку возвращаемых данных. Необходимо проверять правильные ли данные в ответе, а также верно ли запрашиваемое количество с тем,
# что задумано для теста
@pytest.mark.run(order=100)
def test_get_stocks_positive():
    response = requests.post(url=SERVICE_URL + GETTING_STOCKS_PAGE, auth=HTTPBasicAuth(EXTERNAL_LOGIN, EXTERNAL_PASSWORD), headers=EXTERNAL_HEADERS, json=GET_STOCKS_TWO_ITEM_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')    

# Тест на отправку пустого содержимого JSON'a
@pytest.mark.run(order=100)
def test_get_stocks_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + GETTING_STOCKS_PAGE, auth=HTTPBasicAuth(EXTERNAL_LOGIN, EXTERNAL_PASSWORD), headers=EXTERNAL_HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('500')


# Необходимо в тесты добавить сравнение эталонной и возвращаемой схем JSON
# Для этого для каждого вида запроса, возвращающего свой ответ, написать класс Pydantic, который будет описывать схему ответа JSON
# По типу как это сделано у теста создания категории класс CreateCategorySuccessResponse

