# import os 
# from playsound import playsound
# import requests

# # if not os.path.isdir('testing'):
# #     os.mkdir('testing')

# # dir_path = 'testing'
# # file_path = 'kjdhakjda.mp3'
# # with open(dir_path, 'w') as f:
# #     open(file_path, 'x')

# # open(r'testing/https://cdn.islamic.network/quran/audio/128/ar.alafasy/262.mp3', 'x')

# # open('testing/test.mp3', 'x')

# audio = requests.get(f'https://cdn.islamic.network/quran/audio/{...}/{edition}}/{n_verse}.mp3') 

# with open(f'{n_verse}.mp3', 'wb') as f:
#     f.write(audio.content)


from time import perf_counter, sleep
from threading import Thread
import requests

# synchronous (waiting for a response before sending next request)
start = perf_counter()
for i in range(1, 101):
    status = requests.get('https://www.pythontutorial.net/python-concurrency/python-threading/').status_code
end = perf_counter()

print(f'Time taken: {end - start}') # 11.227395999943838


# threaded (not wasting time; sends the next request while waiting)
def make_request():
    status = requests.get('https://www.pythontutorial.net/python-concurrency/python-threading/').status_code

start = perf_counter()
threads = []
for i in range(1, 101):
    t = Thread(target=make_request, args=())
    threads.append(t)
    t.start()
end = perf_counter()

for t in threads:
    t.join()

print(f'Time taken: {end - start}') # x`0.5419381000101566



