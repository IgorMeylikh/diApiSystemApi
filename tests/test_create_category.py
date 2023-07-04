import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages
from requests.auth import HTTPBasicAuth

def test_getting_posts():
    res = requests.post(url=SERVICE_URL + GETTING_PRODUCTS_PAGE, auth=HTTPBasicAuth('consumer@di-house.ru', 'Password1!'))
    #response = requests.post(url=SERVICE_URL + GETTING_PRODUCTS_PAGE)
    assert res.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    print(res)
