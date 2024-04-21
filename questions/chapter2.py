import requests, pprint

url = "https://youtube.com:443"
response = requests.get(url)

pprint.pprint(response.headers)