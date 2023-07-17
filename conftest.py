import pytest
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CREATE_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS
from src.enums.global_enums import GlobalErrorMessages

#Фикстура проверки доступности сервиса с валидными логином, паролем, заголовками
@pytest.fixture()
def fixture_check_available_endpoint():
    response = requests.post(url=SERVICE_URL + CREATE_CATEGORIES_PAGE, auth=HTTPBasicAuth(INTERNAL_LOGIN, INTERNAL_PASSWORD), headers=HEADERS, json={})
    if response.status_code == GlobalErrorMessages.OK_STATUS.value:
        return True
    else:
        assert response.status_code == GlobalErrorMessages.OK_STATUS.value, 'Нет доступа к ресурсу по переданным логину, паролю и заголовкам'
        return False
        