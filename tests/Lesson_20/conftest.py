import random
import pytest

from api_collections.data_classes.notes_dataclass import NotesData
from api_collections.schemas.notes_api import NotesApi


@pytest.fixture()
def get_fake_note_payload(fake):
    return {
        "title": fake.sentence(5),
        "description": fake.sentence(15),
        "category": random.choice(["Home", "Work", "Personal"])
    }


@pytest.fixture()
def get_fake_note_payload_with_status(fake):
    return {
        "title": fake.sentence(5),
        "description": fake.sentence(15),
        "completed": random.choice([True, False]),
        "category": random.choice(["Home", "Work", "Personal"])
    }


@pytest.fixture()
def get_new_note_id(get_fake_note_payload):
    resp = NotesApi().post_new_note(note_data=get_fake_note_payload)
    return resp.json().get("data")["id"]


@pytest.fixture()
def get_mock_note_by_id():
    def __inner(note_id):
        resp = NotesApi().get_note_by_id(note_id=note_id)  # like data from DB
        return NotesData(**resp.json().get("data"))

    return __inner


@pytest.fixture()
def get_random_id():
    return random.randint(10000, 9999999)


@pytest.fixture()
def get_headers_without_token():
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": None
    }

    return headers


@pytest.fixture()
def get_headers_without_content_type():
    headers = {
        "Content-Type": None,
        "x-auth-token": "7f3a06fa12e6449b8c3fd6b9f6f35c1443ce21a6fef54456a8113f6641b66c06"
    }
    return headers
