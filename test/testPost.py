import requests
import json

BASE_URL = 'http://127.0.0.1:5000'
ROUTE = '/video'

data = {
	'url' : 'https://www.youtube.com/watch?v=tJwPlePkPXU',
	'judul' : 'Modul 1 - Pengenalan HTML',
	'pemateri' : 'Heldi',
	'matakuliah' : 'Pemrograman Berbasis Web',
	'semester' : '4'
}

response = requests.post(BASE_URL+ROUTE,
	data = json.dumps(data),
	headers={'Content-Type' : 'application/json'})

print(response.json())