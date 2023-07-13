import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CLEAR_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS

#Тест на удаление всех категорий
@pytest.mark.run(order=1)
@pytest.mark.delete_all_categories
def test_delete_all_categories(fixture_check_available_endpoint):
    if fixture_check_available_endpoint == True:
        requests.delete(url=SERVICE_URL + CLEAR_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS)