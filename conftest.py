import json

import allure
import pytest
from faker import Faker
import requests

from constants import ROOT_PATH
from page_objects.main_page import MainPage
from page_objects.patterns_page import PatternsPage
from page_objects.privacy_policy_page import PolicyPage
from page_objects.refactoring_page import RefactoringPage
from utilities.driver_factory import DriverFactory
from page_objects.store_page import StorePage
from utilities.json_to_dict import DictToClass


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Choose your env")


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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def env(request):
    _env_name = request.config.getoption("--env")
    with open(f"{ROOT_PATH}/configs/{_env_name}.json") as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture
def create_driver(env, request):
    driver = DriverFactory(env.browser_id).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name='Fail_screenshot',
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def open_main_page(create_driver):
    return MainPage(create_driver)


@pytest.fixture
def open_refactor_page(create_driver, env):
    create_driver.get(env.refactor_url)
    return RefactoringPage(create_driver)


@pytest.fixture
def open_store_page(create_driver, env):
    create_driver.get(env.store_page_url)
    return StorePage(create_driver)


@pytest.fixture
def open_patterns_page(create_driver, env):
    create_driver.get(env.patterns_url)
    return PatternsPage(create_driver)


@pytest.fixture
def open_policy_page(create_driver, env):
    create_driver.get(env.privacy_policy_url)
    return PolicyPage(create_driver)


@pytest.fixture
def fake():
    fake = Faker()
    return fake
