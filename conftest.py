import pytest
import requests
from requests.auth import HTTPBasicAuth
from configuration import *

#Фикстура проверки доступности сервиса с валидными логином, паролем, заголовками
@pytest.fixture
def fixture_check_available_endpoint():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json={})
    assert response.status_code == 200, 'Ошибка статус кода'
    if response.status_code == 200:
        return True
    else:
        return False