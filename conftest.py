import pytest
from faker import Faker

from page_objects.main_page import MainPage
from page_objects.patterns_page import PatternsPage
from page_objects.privacy_policy_page import PolicyPage
from page_objects.refactoring_page import RefactoringPage
from utilities.config_reader import AppConfig
from utilities.driver_factory import DriverFactory
from page_objects.store_page import StorePage


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )
    config.addinivalue_line(
        "markers", "regression: mark test regression"
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


@pytest.fixture
def open_refactor_page(create_driver):
    create_driver.get(AppConfig.refactor_url)
    return RefactoringPage(create_driver)


@pytest.fixture
def open_store_page(create_driver):
    create_driver.get(AppConfig.store_page_url)
    return StorePage(create_driver)


@pytest.fixture
def open_patterns_page(create_driver):
    create_driver.get(AppConfig.patterns_url)
    return PatternsPage(create_driver)


@pytest.fixture
def open_policy_page(create_driver):
    create_driver.get(AppConfig.privacy_policy_url)
    return PolicyPage(create_driver)
