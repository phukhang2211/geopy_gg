import geopy
from geopy.geocoders import Nominatim

chose = input('Do you want to use OSM or GG is the basemap (type OSM or GG) ')

if chose == 'OSM':
	geolocator = Nominatim(user_agent="my app")
	location = input("Input address (unit, street, ward, district): ")
	location = geolocator.geocode(location)
	print(location.raw)
	print(location.address)
	print(location.latitude, location.longitude)
else:
	with open('API_google.txt','r') as f:
        api = f.read()
    address = input("Input address (unit, street, ward, district): ")
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+api
    resp = requests.get(url).json()
    print(resp['results'][0]['geometry']['location'])
    
