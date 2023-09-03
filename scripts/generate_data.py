import requests
import json
import os

import winsound # To test play samples

'''
Create the dataset directory with the organization:

data/
    1/ # 1st chapter
        1/ # 1st verse in 1st chapter
            sample1.mp3 # An audio sample of the 1st verse in the 1st chapter
            sample2.mp3 # Another audio sample
            ...
        2/ # 2nd verse in 2nd chapter
            ... # Audio samples
        ... # More verse directories
    2/
        1/ # 1st verse in 2nd chapter
            ...
        2/ 
            ...
        ...
    ...

========== OUTLINE ============
For each chapter
    For each verse in each chapter
        For each audio edition of each verse
            Create a string representing the .mp3 sample with all the information needed
            Store this .mp3 sample in this innermost directory

We need to check the bitrates because they are not consistent for the samples.

Reference:
https://raw.githubusercontent.com/islamic-network/cdn/master/info/cdn.txt
'''

with open('json/chapter_range.json', 'r') as f: 
    chapter_range = json.load(f)

with open('json/bitrates_for_reciters.json', 'r') as f:
    bitrates_for_reciters = json.load(f)

if not os.path.isdir('data'):
    os.mkdir('data')

total_verses_acc = 0 # Should be 6223 in the end
def create_data_dirs():
    for n_chapter in range(14, 114 + 1):
        print(f'In chapter {n_chapter}') # should be in [1,114]
        # if not os.path.isdir(f'data/{n_chapter}'):
        # os.mkdir(f'data/{n_chapter}')
        for n_verse in range(chapter_range[str(n_chapter)][0], chapter_range[str(n_chapter)][1] + 1):
            print(f'In verse {n_verse} in chapter {n_chapter}') # n_verse should be within chapter's range
            print(total_verses_acc)
            if not os.path.isdir(f'data/{n_chapter}_{n_verse}'):
                os.mkdir(f'data/{n_chapter}_{n_verse}')
                for reciter in bitrates_for_reciters.keys():
                    cdn_link = f'https://cdn.islamic.network/quran/audio/{min(bitrates_for_reciters[reciter])}/{reciter}/{n_verse}.mp3'
                    audio = requests.get(cdn_link)
                    # reciter[3:] excludes ar. from the string "ar.reciter_name"
                    with open(f'data/{n_chapter}_{n_verse}/{n_chapter}_{n_verse}_{reciter[3:]}.mp3', 'wb') as f:
                        f.write(audio.content)

create_data_dirs()
print(total_verses_acc) # Should be 6223

