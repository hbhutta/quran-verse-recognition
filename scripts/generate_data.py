import requests
import json
import os

from time import perf_counter, sleep
from threading import Thread

with open('json/chapter_range.json', 'r') as f: 
    chapter_range = json.load(f)

with open('json/bitrates_for_reciters.json', 'r') as f:
    bitrates_for_reciters = json.load(f)

if not os.path.isdir('data_v2'):
    os.mkdir('data_v2')
'''
Returns audio content
'''
def make_request(n_chapter: int, n_verse: int, reciter: str):
    cdn_link = f'https://cdn.islamic.network/quran/audio/{min(bitrates_for_reciters[reciter])}/{reciter}/{n_verse}.mp3'
    content = requests.get(cdn_link).content  # Takes 1 ~ 1.5 seconds per request (deduced from visual observation of folder changes)
    with open(f'data_v2/{n_chapter}_{n_verse}/{n_chapter}_{n_verse}_{reciter[3:]}.mp3', 'wb') as f:
        f.write(content) 


start = perf_counter()
threads = []
for n_chapter in range(23, 115):
    print(f'In chapter {n_chapter}') 

    for n_verse in range(chapter_range[str(n_chapter)][0], chapter_range[str(n_chapter)][1] + 1):
        print(f'In verse {n_verse} in chapter {n_chapter}')

        if not os.path.isdir(f'data_v2/{n_chapter}_{n_verse}'):
            os.mkdir(f'data_v2/{n_chapter}_{n_verse}')

            for reciter in bitrates_for_reciters.keys():
                t = Thread(target=make_request, args=[n_chapter, n_verse, reciter])
                threads.append(t)
                t.start()   
end = perf_counter()

for t in threads:
    t.join()

# Threading reduced time from ~50 hours to 12 minutes
print(f'Time taken: {end - start}')



