import pytest
from faker import Faker

from page_objects.main_page import MainPage
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture
def create_driver():
    driver = DriverFactory(AppConfig.browser_id).get_driver()
    driver.maximize_window()
    driver.get(AppConfig.url)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(create_driver):
    return MainPage(create_driver)
