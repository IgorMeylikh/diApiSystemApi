import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import *
from src.enums.global_enums import GlobalErrorMessages

@pytest.mark.diapitests
def test_getting_posts():
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'requestId': REQUETS_ID, 'senderSystem': SENDER_SYSTEM}
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth('system@di-house.ru', 'Password1!'), headers=headers, json={})
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value + ' Response status code: ' + str(response.status_code)
    print(response.status_code)
    print(response.json())
 

