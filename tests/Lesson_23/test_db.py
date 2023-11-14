import pytest
import sqlite3


def test_get_all_phones(phones_repo):
    db = phones_repo
    all_phones = db.get_all()
    assert isinstance(all_phones, list), "Incorrect type of data, should be list"
    for phone in all_phones:
        print(phone)


def test_get_phone_by_brand(phones_repo):
    db = phones_repo
    brand_phones = db.get_phone_by_brand("Samsung")
    assert isinstance(brand_phones, list), "Incorrect type of data, should be list"
    for phone in brand_phones:
        print(phone)


def test_add_phone(phones_repo, fake_phone):
    db = phones_repo
    db.insert_one(**fake_phone)
    phone = db.get_one_by_id()
    assert isinstance(phone, tuple), "Incorrect type of phone data, should be tuple"
    print(phone)


def test_update_full_phone(phones_repo, fake_phone):
    db = phones_repo
    db.insert_one(**fake_phone)
    new_phone = ("V20", "LG", "Snapdragon 820", 2018, 750.0)
    db.update_full_phone(*new_phone)
    upd_phone = list(db.get_one_by_id())
    assert upd_phone[1:] == ["V20", "LG", "Snapdragon 820", 2018, 750.0], "The changes were not saved"
    print(upd_phone)


def test_update_phone_model(phones_repo, fake_phone):
    db = phones_repo
    db.insert_one(**fake_phone)
    db.partial_phone_update(model="Galaxy S22")
    upd_phone = list(db.get_one_by_id())
    assert upd_phone[1] == "Galaxy S22", "Incorrect phone model"
    print(upd_phone)


def test_delete_phone(phones_repo, fake_phone):
    db = phones_repo
    first_max_id = db.get_max_phone_id()
    db.insert_one(**fake_phone)
    db.delete_phone_by_id()
    second_max_id = db.get_max_phone_id()
    assert first_max_id == second_max_id, "Incorrect max index or item was not deleted"


def test_get_phone_by_invalid_brand_fails(phones_repo):
    db = phones_repo
    inv_brand = "Hello"
    brand_phones = db.get_phone_by_brand(inv_brand)
    assert brand_phones is None, f"Value of brand_phones should be None, because there is no brand {inv_brand}"


def test_add_phone_without_model_fails(phones_repo):
    db = phones_repo
    with pytest.raises(sqlite3.IntegrityError, match="NOT NULL constraint failed: PHONES.MODEL"):
        db.insert_one(model=None, brand="Huawei", processor="Kirin", year=2020, price=500.0)


def test_delete_phone_by_wrong_id_fails(phones_repo):
    db = phones_repo
    first_max_id = db.get_max_phone_id()
    inv_id = "word"
    db.delete_phone_by_id(inv_id)
    second_max_id = db.get_max_phone_id()
    assert first_max_id == second_max_id, f"Item was deleted by incorrect id {inv_id}, but should`t!"



