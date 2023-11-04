from http import HTTPStatus
from api_collections.data_classes.notes_dataclass import NotesData
from api_collections.schemas.notes_api import NotesApi


# Find public API with several endpoints (Can use Notes or Gorest API)
#
# Add API testing to your test framework (BaseAPI, API collection)
#
# Write several API tests (minimum 10)

# Приклади з лекції
def test_get_all_notes():
    resp = NotesApi().get_all_notes()
    assert resp.status_code == HTTPStatus.OK, f"Failed! {resp.text}"
    data = resp.json()
    assert isinstance(data, dict)


def test_post_new_note(get_fake_note_payload):
    payload = get_fake_note_payload
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"
    data = resp.json().get("data")
    assert data["title"] == payload["title"]


def test_get_note_by_id(get_new_note_id, get_mock_note_by_id):
    _id = get_new_note_id
    resp = NotesApi().get_note_by_id(note_id=_id)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"
    notes_data = NotesData(**resp.json().get("data"))
    actual_data_from_db = get_mock_note_by_id(_id)
    assert notes_data.get_dict() == actual_data_from_db.get_dict()


def test_post_new_note_without_title():
    payload = NotesData.get_fake_note_payload()
    payload.pop("title")
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == 400


# Мої тести

def test_update_existing_note(get_new_note_id):
    payload = NotesData.get_fake_note_payload_with_status()
    _id = get_new_note_id
    resp = NotesApi().get_note_by_id(note_id=_id)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"
    new_note_resp = NotesApi().update_existing_note(_id, payload)
    assert new_note_resp.status_code == 200, f"Request fail! {resp.text}"


def test_post_new_note_without_description(get_fake_note_payload):
    payload = get_fake_note_payload
    payload.pop("description")
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == 400, f"Incorrect error status code {resp.text}"


def test_post_empty_note():
    payload = {}
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == 400, f"Incorrect error status code {resp.text}"
    assert resp.json()["message"] == "Title must be between 4 and 100 characters", "Incorrect error message"


def test_delete_note_by_id(get_new_note_id):
    _id = get_new_note_id
    resp = NotesApi().delete_note(note_id=_id)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"


def test_delete_note_without_id():
    _id = ""
    resp = NotesApi().delete_note(note_id=_id)
    assert resp.status_code == 404, f"Incorrect error status code {resp.text}"
    er_message = "Page Not Found"
    assert er_message in resp.text, "Incorrect error message"


def test_delete_note_without_content_type(get_new_note_id, get_headers_without_content_type):
    _id = get_new_note_id
    new_headers = get_headers_without_content_type
    resp = NotesApi().delete_note_with_custom_headers(note_id=_id, my_headers=new_headers)
    assert resp.status_code == 200, f"Request fail! {resp.text}"
    data = resp.json()
    assert data["message"] == "Note successfully deleted", "Incorrect response message"


def test_get_note_with_wrong_id(get_random_id):
    _id = get_random_id
    resp = NotesApi().get_note_by_id(note_id=_id)
    assert resp.status_code == 400, f"Incorrect error status code {resp.text}"
    er_message = "Note ID must be a valid ID"
    assert er_message in resp.text, "Incorrect error message"


def test_get_all_notes_without_token(get_headers_without_token):
    inv_headers = get_headers_without_token
    resp = NotesApi().get_all_notes_with_custom_token(inv_headers)
    assert resp.status_code == HTTPStatus.UNAUTHORIZED, f"Incorrect error status code {resp.text}"
    er_message = "No authentication token specified in x-auth-token header"
    assert er_message in resp.text, "Incorrect error message"


def test_change_note_status(get_fake_note_payload_with_status):  # разобрать
    payload = get_fake_note_payload_with_status
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"
    data = resp.json().get("data")
    updated_data = NotesApi.change_completed_status(data=data)
    resp_change_status = NotesApi().update_note_status(note_id=updated_data["id"], data=updated_data)
    assert resp_change_status.status_code == 200, f"Request fail! {resp.text}"
    new_data = resp_change_status.json().get("data")
    assert new_data["completed"] == data["completed"]


def test_change_note_status_to_str(get_fake_note_payload_with_status):
    payload = get_fake_note_payload_with_status
    resp = NotesApi().post_new_note(note_data=payload)
    assert resp.status_code == HTTPStatus.OK, f"Request fail! {resp.text}"
    data = resp.json().get("data")
    data["completed"] = "Hello"
    resp_change_status = NotesApi().update_note_status(note_id=data["id"], data=data)
    assert resp_change_status.status_code == 400, f"Incorrect error status code {resp.text}"
    er_message = "Note completed status must be boolean"
    assert er_message in resp_change_status.text, "Incorrect error message"
