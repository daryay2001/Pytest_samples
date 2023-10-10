import pytest
from .car import Car


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture(scope="function")
def get_default_car():
    new_car = Car("Mazda", "C3")
    return new_car


@pytest.fixture(scope="function")
def get_new_car():
    new_car = Car("Nissan", "Qashqai", 100)
    return new_car


@pytest.fixture(scope="function")
def get_new_car_running():
    new_car = Car("Honda", "Civic", 80)
    new_car.start_engine()
    return new_car


@pytest.fixture
def get_new_car_params():
    def __inner_new_car(brand, model, miles_limit):
        new_car = Car(brand, model, miles_limit)
        return new_car

    return __inner_new_car
