
# IP Look UP

from urllib import request
import json

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))
except Exception as e:
    print(e)
else:
    print('You are near: {city}, {region}, {country}'.format(**data)) 
    # since the data is stored as a dictionary, I can use the double splat operator on line 12 
    # to treat the key value pairs in the dictionary as named arguments to the format function.
    print('     Lat/Lng: {}E'.format(data['loc'].replace(',','N, ')))
