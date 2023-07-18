import requests
import urllib.parse
import json


resource_url = 'https://www.mapquestapi.com/directions/v2/route?'

with open('key.txt', 'r') as k:
    key = k.read()
    
route_from = str(input()).capitalize()
route_to = str(input()).capitalize()

url = resource_url + urllib.parse.urlencode({'key': key, 'from': route_from, 'to': route_to})

json_data = requests.get(url).json()
json_object = json.dumps(json_data, indent=4)

with open('output_map.json', 'a') as f:
    f.write(json_object)

print(str(int(json_data['route']['distance'])) + 'km')
print(json_data['route']['formattedTime'])
