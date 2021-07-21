import requests
import json

BASE_URL = 'http://127.0.0.1:5000'
ROUTE = '/video/1'

response = requests.delete(BASE_URL+ROUTE)

print(response.json())