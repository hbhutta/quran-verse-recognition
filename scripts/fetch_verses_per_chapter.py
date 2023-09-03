import requests
import json
import os

'''
Get the range of verses for each chapter.
Ranges are disjoint covers of the Quran.

ex) Al-Fatihah's range is [1, 7], Al-Baqarah's range is [8, 263]
'''
n_chapter_range = {} # {Chapter: [range_start, range_end]}
range_start = 1
range_end = -1
for chapter in range(1, 115):
    chapter_api_link = f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{chapter}'

    chapter_api = requests.get(chapter_api_link)
    chapter_json = chapter_api.json()
    
    n_verses = len(chapter_json['result'])
    range_end = n_verses + range_start - 1
    # print(type(chapter))
    n_chapter_range[int(chapter)] = [range_start, range_end]
    print(f'Ranged Chapter {chapter}')

    range_start = range_end + 1
    
if not os.path.isdir('json'):
    os.mkdir('json')

with open('json/chapter_range.json', 'w') as fp1:
    json.dump(n_chapter_range, fp1) # n_chapter_range should have length 114

 
    

    


