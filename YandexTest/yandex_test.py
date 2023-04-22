import requests

token_yandex = 'token'
url = 'https://cloud-api.yandex.net/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Authorization': token_yandex}
    create_direct = requests.api.put(url, headers=headers, params=params)
    return create_direct.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Authorization': token_yandex}
    create_direct = requests.api.delete(url, headers=headers, params=params)
    return create_direct.status_code
