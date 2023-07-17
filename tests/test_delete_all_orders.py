import pytest 
import requests
from requests.auth import HTTPBasicAuth
from src.baseclasses.response import Response
from configuration import SERVICE_URL, CLEAR_ORDERS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS

#Тест на удаление всех заказов
@pytest.mark.run(order=5)
@pytest.mark.delete_all_orders
def test_delete_all_categories():
    response = requests.delete(url=SERVICE_URL + CLEAR_ORDERS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS)
    test_object = Response(response)
    test_object.assert_status_code(200)
