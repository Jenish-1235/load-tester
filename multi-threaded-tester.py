from threading import Thread as T
import requests
import random
import concurrent.futures

def random_page_id():
    return 'page_' + str(random.randint(0, 1000))

def get_request():
    try:
        get_request = requests.get('http://localhost:8000/api/v1/counter/visits/' + random_page_id())
        print(get_request.json())
    except Exception as e:
        print(e)

def post_request():
    try:
        post_request = requests.post('http://localhost:8000/api/v1/counter/visit/' + random_page_id())
        print(post_request.json())
    except Exception as e:
        print(e)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(0, 1000):
        executor.submit(get_request)
        executor.submit(post_request)


