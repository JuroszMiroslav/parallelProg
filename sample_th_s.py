import requests
import time

def download_content(url):
    response = requests.get(url)
    print(f'Finished downloading {url}')

def single_thread_download(urls):
    start_time = time.time()
    for url in urls:
        download_content(url)

    end_time = time.time()
    print(f'Jednovláknový přístup trval {end_time - start_time} sekund.')

if __name__ == '__main__':
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.github.com',
        'https://www.stackoverflow.com'
    ]
    print("Jednovláknový přístup:")
    single_thread_download(urls)