import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, CLEAR_CATEGORIES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, HEADERS

#Тест на удаление всех цен
# @pytest.mark.run(order=4)