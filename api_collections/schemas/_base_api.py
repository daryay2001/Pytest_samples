import requests
from jsonschema import validate


class BaseApi:
    def __init__(self, base_url):
        self.__base_url = base_url
        self.__headers = {}
        self.__requests = requests

    @staticmethod
    def _validate_json(instance, schema):
        validate(instance, schema)

    def _get(self, url, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def _post(self, url, data, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.post(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

    def _patch(self, url, data, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.patch(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

    def _put(self, url, data, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.put(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

    def _delete(self, url, data=None, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.delete(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

