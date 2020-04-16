import geopy
import requests
with open('API_google.txt','r') as f:
    api = f.read()
start = input("Input address start (unit, street, ward, district): ")
end = input("Input address end (unit, street, ward, district): ")


url_direction = 'https://maps.googleapis.com/maps/api/directions/json?origin='+start+'&destination='+end+'&key='+api
direction = requests.get(url_direction).json()
print(direction['routes'][0]['legs'][0]['start_location'])
for step in range(len(direction['routes'][0]['legs'][0]['steps'])):
    print(direction['routes'][0]['legs'][0]['steps'][step]['end_location'])
