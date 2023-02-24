import requests
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

toc = os.getenv('TOKEN')
path_to_file = 'Test'

def upload(file_path):
    base_host = 'https://cloud-api.yandex.net'
    heders = {'Authorization': f'OAuth {toc}'}
    params = {'path': file_path, 'overwrite': True}
    uri = '/v1/disk/resources'
    request_url = base_host + uri
    response = requests.put(request_url, headers=heders, params=params)
    link = response.json()
    return [link['href'], response.status_code]

# print(upload(path_to_file))

