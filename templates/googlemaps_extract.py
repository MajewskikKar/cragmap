import requests

r = requests.get('https://www.8a.nu/crags/sportclimbing/poland/dolina-szklarki/')
r = r.text
print(r)
