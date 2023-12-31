import pytest 
import requests
from requests.auth import HTTPBasicAuth
from src.baseclasses.response import Response
from configuration import SERVICE_URL, CLEAR_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS

#Тест на удаление всех категорий
@pytest.mark.run(order=1)
@pytest.mark.delete_all_categories
def test_delete_all_categories_positive():
    response = requests.delete(url=SERVICE_URL + CLEAR_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=INTERNAL_HEADERS)
    test_object = Response(response)
    test_object.assert_status_code(200)
