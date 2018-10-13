import requests
import wikipedia

S = requests.Session()

URL  = "https://en.wikipedia.org/w/api.php"

miles = 2
radius = int(miles/.00621) #in meters
#COORDS = '37.7891838|-122.4033522'
COORDS = '40.7281|-73.9916'
PARAMS = {
    'action':"query",
    'list':"geosearch",
    'gscoord': COORDS,
    'gsradius': radius,
    'gsglobe': "earth",
    'gslimit':10,
    'format':"json",
    "gsprop": "type",
    "gsprimary": "primary",
    'type':"landmark"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA['query']['geosearch']
print(COORDS)

place_list = []
for place in PLACES:   
    print(place['title'], place['dist']*.00621)
    place_list.append(place['title'])

print(wikipedia.summary(place_list[0], sentences = 3))

