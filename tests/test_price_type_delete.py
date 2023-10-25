import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_PRICE_TYPES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON, DELETE_ONE_PRICE_TYPE
from src.baseclasses.response import Response

# Тест на удаление одного типа цен (с передачей 1 валидного элемента)
@pytest.mark.run(order=130)
def test_delete_one_price_type_positive():
    response = requests.post(url=SERVICE_URL + DELETE_PRICE_TYPES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS, json=DELETE_ONE_PRICE_TYPE)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('200')

