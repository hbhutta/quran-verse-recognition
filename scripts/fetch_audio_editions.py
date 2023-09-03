import requests
import json
import os

audio_editions = requests.get('https://api.alquran.cloud/v1/edition/format/audio')
audio_editions_json = audio_editions.json()

reciters = []
for d in audio_editions_json['data']:
    # Only include arabic recitations
    if d.startswith('ar'):
        reciters.append(d['identifier'])

if not os.path.isdir('data'):
    os.mkdir('data')

with open('data/reciters.json', 'w') as fp:
    json.dump(reciters, fp)
    