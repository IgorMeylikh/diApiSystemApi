import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CLEAR_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import SuccessResponse, SuccessItem, SuccessStatusCode

#Тест на удаление всех категорий
def test_delete_all_categories(fixture_check_available_endpoint):
    requests.delete(url=SERVICE_URL + CLEAR_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS)