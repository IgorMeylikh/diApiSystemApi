import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
    print(response)
