import requests
from pprint import pprint
URL = "http://127.0.0.1:2224/data"

pprint(requests.get(URL).json())
