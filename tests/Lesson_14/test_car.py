SSSSSSSSSSSSSSSSSSSSSSSSS# Test the Car class in the attached file. I will check the coverage.
# Write as many TCs as possible - minimum 10.

import pytest
from random import randint
from .car import Car


@pytest.mark.smoke
def test_create_car_instance(get_new_car):
    new_car = get_new_car
    assert isinstance(new_car, Car)


@pytest.mark.smoke
def test_create_car_with_default_parameters(get_default_car):
    new_car = get_default_car
    assert new_car.miles_limit == 0


@pytest.mark.smoke
def test_start_engine(get_new_car):
    new_car = get_new_car
    assert new_car.start_engine() == "Engine started."


@pytest.mark.sanity
def test_start_engine_twice(get_new_car_running):
    new_running_car = get_new_car_running
    assert new_running_car.start_engine() == "Engine is already running."


@pytest.mark.smoke
def test_stop_engine(get_new_car_running):
    new_running_car = get_new_car_running
    assert new_running_car.stop_engine() == "Engine stopped."


@pytest.mark.sanity
def test_stop_disabled_engine(get_new_car):
    new_car = get_new_car
    assert new_car.stop_engine() == "Engine is already off."


@pytest.mark.sanity
def test_drive_with_stopped_engine(get_new_car):
    new_car = get_new_car
    assert new_car.drive(randint(1, 100)) == "Cannot drive. Engine is off."


@pytest.mark.sanity
def test_drive(get_new_car_params):
    new_car = get_new_car_params("Audi", "A2", 90)
    new_car.start_engine()
    miles_to_drive = 60
    assert new_car.drive(miles_to_drive) == f"Driving {miles_to_drive} miles."


@pytest.mark.sanity
def test_change_miles_limit(get_new_car_params):
    new_car = get_new_car_params("Opel", "Astra", 130)
    new_car.start_engine()
    miles_to_drive = 90
    new_car.drive(miles_to_drive)
    assert new_car.miles_limit == 40


@pytest.mark.sanity
def test_drive_exceed_miles_limit(get_new_car_params):
    new_car = get_new_car_params("Opel", "Ampera", 150)
    new_car.start_engine()
    miles_to_drive = 155
    assert new_car.drive(miles_to_drive) == "The miles limit has been exceeded"
    assert new_car.miles_limit == 150
