import requests
import wikipedia

###
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
###




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

x = wikipedia.summary(place_list[0], sentences = 3)
print(x)
synthesize_text(x)
