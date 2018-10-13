from django.contrib.auth.models import User
from rest_framework import viewsets
from project.api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view()
def places_at(request):
    import requests
    import wikipedia
    from django.conf import settings
    from uuid import uuid4
    from rest_framework.reverse import reverse_lazy

    coords = request.query_params["coords"]

    if coords == "":
        return Response(status=400)

    s = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"

    radius = 2                    # miles
    radius = int(radius/.00621)   # meters
    params = {
        'action':"query",
        'list':"geosearch",
        'gscoord': coords,
        'gsradius': radius,
        'gsglobe': "earth",
        'gslimit': 10,
        'format': "json",
        "gsprop": "type",
        "gsprimary": "primary",
        'type':"landmark"
    }

    data = s.get(url=url, params=params).json()

    places = data['query']['geosearch']
    summary = wikipedia.summary(places[4]["title"], sentences=3)

    def to_speech(text, path):
        """Synthesizes speech from the input string of text."""
        from google.cloud import texttospeech
        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.types.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE
        )

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3
        )

        response = client.synthesize_speech(input_text, voice, audio_config)

        # The response's audio_content is binary.
        with path.open('wb') as out:
            out.write(response.audio_content)

    audiofilename = str(uuid4()) + ".mp3"
    audiofilepath = settings.MEDIA_ROOT / audiofilename
    to_speech(summary, audiofilepath)

    return Response({"audio": request.build_absolute_uri(settings.MEDIA_URL + audiofilename)})
