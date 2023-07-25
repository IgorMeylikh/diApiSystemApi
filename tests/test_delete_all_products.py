import pytest 
import requests
from requests.auth import HTTPBasicAuth
from src.baseclasses.response import Response
from configuration import SERVICE_URL, CLEAR_PRODUCTS_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS

#Тест на удаление всех продуктов
@pytest.mark.run(order=2)
@pytest.mark.delete_all_products
def test_delete_all_products_positive():
    response = requests.delete(url=SERVICE_URL + CLEAR_PRODUCTS_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS)
    test_object = Response(response)
    test_object.assert_status_code(200)
