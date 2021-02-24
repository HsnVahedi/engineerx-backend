import os

import requests


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
