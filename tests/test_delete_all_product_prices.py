import pytest 
import requests
from requests.auth import HTTPBasicAuth
from src.baseclasses.response import Response
from configuration import SERVICE_URL, CLEAR_PRICES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS

#Тест на удаление всех цен
@pytest.mark.run(order=4)
@pytest.mark.delete_all_prices
def test_delete_all_prices_positives():
    response = requests.delete(url=SERVICE_URL + CLEAR_PRICES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS)
    test_object = Response(response)
    test_object.assert_status_code(200)
