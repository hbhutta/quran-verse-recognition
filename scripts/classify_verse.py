import requests
import json
import os

with open('chapter_range.json', 'r') as f: 
    chapter_range = json.load(f)

verse_labels = {}
n_chapter = "1" # Al-Fatihah
for n_verse in range(1, 6224):
    verse_mp3 = f'https://cdn.islamic.network/quran/audio/128/ar.alafasy/{n_verse}.mp3'
    if chapter_range[n_chapter][0] <= n_verse and n_verse <= chapter_range[n_chapter][1]:
        verse_labels[verse_mp3] = n_chapter
        print(f'Labelled verse {n_verse} with {n_chapter}')
    else:
        n_chapter = int(n_chapter)
        n_chapter += 1
        
        verse_labels[verse_mp3] = n_chapter
        n_chapter = str(n_chapter)

if not os.path.isdir('data'):
    os.mkdir('data')

with open('data/verse_labels.json', 'w') as f:
    json.dump(verse_labels, f) 