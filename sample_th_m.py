import threading
import requests
import time

def download_content(url):
    response = requests.get(url)
    print(f'Finished downloading {url}')

def multi_thread_download(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_content, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f'Multithreading přístup trval {end_time - start_time} sekund.')

if __name__ == '__main__':
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.github.com',
        'https://www.stackoverflow.com'
    ]
    print("Multithreading přístup:")
    multi_thread_download(urls)
