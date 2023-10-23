import pytest 
import requests
from requests.auth import HTTPBasicAuth
from configuration import SERVICE_URL, DELETE_WAREHOUSES_PAGE, INTERNAL_LOGIN, INTERNAL_PASSWORD, INTERNAL_HEADERS, EMPTY_JSON
from src.baseclasses.response import Response


