import json
import os
import time
import datetime
import requests
import random

def random_page_id():
    return 'page_' + str(random.randint(0, 1000))


for i in range(0, 1000):
    get_request = requests.get('http://localhost:8000/api/v1/counter/visits/' + random_page_id())
    print(get_request.json())
    post_request = requests.post('http://localhost:8000/api/v1/counter/visit/' + random_page_id())
    print(post_request.json())

