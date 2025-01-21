import requests
from requests import get

ipAdd = get('https://api.ipify.org')
print(ipAdd)
url = 'https://get.geojs.io/v1/ip/geo/'
geo_requests = requests.get(url)
geo_data = geo_requests.json()


    