import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import *
from src.baseclasses.response import Response
import json 
@pytest.mark.diapitests

def test_create_category():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'requestId': REQUETS_ID, 'senderSystem': SENDER_SYSTEM}
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=headers, json=CREATE_ONE_CATEGORY_JSON)
    test_object = Response(response)
    test_object.assert_status_code(200)
    test_object.assert_operation_code('201')
    requests.delete(url=SERVICE_URL + CLEAR_CATEGORIES_PAGE, auth=HTTPBasicAuth('system@di-house.ru', 'Password1!'), headers=headers)




