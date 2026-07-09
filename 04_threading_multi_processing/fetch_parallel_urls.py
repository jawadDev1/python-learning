# Project excercise

import time
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return f"Fetched {url} successfully!!!"
    except Exception as e:
        print(f"Faile to fetch data: Url: {url}, Error: {e} ")


urls = [
    "https://fakestoreapi.com/products",
    "https://fakestoreapi.com/products/1",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos",
    "https://fakestoreapi.com/products/2",
]

t1 = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    for result in executor.map(fetch_data, urls):
        print(result)

t1_done_in = time.time() - t1
print("ThreadPool Done Fetching!!!! ", t1_done_in)

# Sequential time

t2 = time.time()

for url in urls:
    result = fetch_data(url)
    print(result)


t2_done_in = time.time() - t2
print("Squential Done Fetching!!!! ", t2_done_in)

print("SpeedUP :: ", t2_done_in / t1_done_in)
