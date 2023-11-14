import pytest
import random

from constants import ROOT_PATH
from db.sqlite_pack.phones_repo import PhonesRepo


@pytest.fixture(scope="module")
def phones_repo(env):
    return PhonesRepo(f"{ROOT_PATH}{env.db_param['path']}")


@pytest.fixture()
def fake_phone(fake):
    model_name = random.choice(["Iphone 15 Pro", "Iphone 12", "Iphone 14 Plus",
                                "Galaxy S20", "A50", "Note 10 Lite"])
    data = {
        "model": model_name,
        "brand": "Apple" if model_name.startswith("Iphone") else "Samsung",
        "processor": random.choice(["A16 Bionic", "A15 Bionic", "A14 Bionic"]) if model_name.startswith("Iphone")
        else random.choice(["Exynos 990", "Exynos 9610", "Samsung Exynos 9825"]),
        "year": fake.pyint(2018, 2023),
        "price": float(fake.pyint(750, 1600))
    }

    return data


