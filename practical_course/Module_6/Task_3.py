import requests
import time
import threading

def get_html(url):
    response = requests.get(url) # server data
    if response.status_code == 200: # status is ok
        return response 
    else:
        print(f"Status code: {response.status_code}\n Request failed\n")
        return None

links = [
    'https://ru.pinterest.com', 
    'https://ya.ru', 
    'https://www.youtube.com', 
    'https://github.com',
    'https://brunoyam.com'
]

def get_urls_data(url):
    html = get_html(url)
    if html is not None:
        print(f"Got data from {url}") # can add some more info or data
    else:
        print(f"Failed to get data from {url}")

start_time = time.time() #parallel time

threads = []
for url in links:
    thread = threading.Thread(target=get_urls_data, args=(url, ))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

parallel_time = time.time() - start_time
print(f"Time of the parallel run: {parallel_time} sec.\n")


start_time = time.time() # synch time

for link in links:
    get_urls_data(link)

synchron_time = time.time() - start_time
print(f"Time of the synchronous run: {synchron_time} sec.")
