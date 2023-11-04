import json
from api_collections.schemas._base_api import BaseApi


class NotesApi(BaseApi):
    def __init__(self, base_url="https://practice.expandtesting.com/notes/api"):
        super().__init__(base_url)
        self.__url = "/notes"
        self.__headers = {
            "Content-Type": "application/json",
            "x-auth-token": "7f3a06fa12e6449b8c3fd6b9f6f35c1443ce21a6fef54456a8113f6641b66c06"
        }

    @staticmethod
    def change_completed_status(data):
        if "completed" in data and isinstance(data["completed"], bool):
            data["completed"] = not data["completed"]
        return data

    def get_all_notes(self):
        return self._get(url=self.__url, headers=self.__headers)

    def get_note_by_id(self, note_id: str):
        return self._get(url=f"{self.__url}/{note_id}", headers=self.__headers)

    def post_new_note(self, note_data: dict):
        return self._post(self.__url, data=json.dumps(note_data), headers=self.__headers)

    def update_existing_note(self, note_id: str, new_note_data: dict):
        try:
            resp = self._put(f"{self.__url}/{note_id}", data=json.dumps(new_note_data), headers=self.__headers)

            return resp
        except Exception as error:
            print(error)

    def delete_note(self, note_id: str):
        return self._delete(url=f"{self.__url}/{note_id}", headers=self.__headers)

    def update_note_status(self, note_id: str, data: dict):
        return self._patch(url=f"{self.__url}/{note_id}", data=json.dumps(data), headers=self.__headers)

    def get_all_notes_with_custom_token(self, my_headers):
        return self._get(url=self.__url, headers=my_headers)

    def delete_note_with_custom_headers(self, note_id: str, my_headers):
        return self._delete(url=f"{self.__url}/{note_id}", headers=my_headers)

    @staticmethod
    def change_completed_status(data):
        if "completed" in data and isinstance(data["completed"], bool):
            data["completed"] = not data["completed"]
        return data
