import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS, EMPTY_JSON
from src.baseclasses.response import Response
from src.pydantic_schemas.create_category_pydantic import CreateCategorySuccessResponse, CreateCategorySuccessItem, CreateCategorySuccessStatusCode



# Тест на отправку пустого содержимого JSON'a
@pytest.mark.run(order=20)  
def test_delete_category_without_items_json_negative():
    response = requests.post(url=SERVICE_URL + DELETE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json=EMPTY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('400')