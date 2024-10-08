import requests
import threading
import time

urls = ['https://t.me/python3k',
        'https://www.youtube.com/channel/UCQ1YbfMA6jeGamfA1RHMWHQ',
        'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
        'https://docs.python.org/3/library/asyncio.html',
        'https://habr.com/ru/articles/671602/',]


def download(url):
    responce = requests.get(url)
    filename = 'thread_' + url.replace('https://',
                            '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(responce.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
