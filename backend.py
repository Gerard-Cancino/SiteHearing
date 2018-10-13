import requests

S = requests.Session()

URL  = "https://en.wikipedia.org/w/api.php"

miles = 5
radius = int(miles/.00621) #in meters
#COORDS = '37.7891838|-122.4033522'
COORDS = '40.7281|73.9916'
PARAMS = {
    'action':"query",
    'list':"geosearch",
    'gscoord': COORDS,
    'gsradius':radius,
    'gslimit':10,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['geosearch']
print(COORDS)
place_list = []
for place in PLACES:
    print("loop entered")
    print(place['title'], place['dist'], place['lat'], place['lon'])
#    place_list.append(place['title'])


#print(place_list[0])

