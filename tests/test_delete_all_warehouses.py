import pytest 
import requests
from requests.auth import HTTPBasicAuth
from src.baseclasses.response import Response
from configuration import SERVICE_URL, CLEAR_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS

#Тест на удаление всех заказов
@pytest.mark.run(order=6)
@pytest.mark.delete_all_warehouses
def test_delete_all_warehouses_positive():
    response = requests.delete(url=SERVICE_URL + CLEAR_WAREHOUSES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS)
    test_object = Response(response)
    test_object.assert_status_code(200)
