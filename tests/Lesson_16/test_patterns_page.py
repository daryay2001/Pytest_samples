import allure
import pytest


@allure.title("Test check creational patterns count")
@allure.description("Go to the patterns catalog and check the count of creational patters.")
@allure.tag("Patterns", "Count")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_creational_patterns_count(open_patterns_page):
    patterns_page = open_patterns_page
    patterns_page.click_catalog_patterns_btn()
    assert patterns_page.creational_patterns_get_count() == 5, "There should be 5 creational patterns"


@allure.title("Test Go to abstract factory page")
@allure.description("Go to abstract factory page via btn.")
@allure.tag("Button", "Patterns")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_abstract_factory(open_patterns_page):
    patterns_page = open_patterns_page
    patterns_page.click_catalog_patterns_btn()
    patterns_page.click_factory_method_btn()
    patterns_page.click_abstract_factory_link()
    assert patterns_page.get_page_url() == "https://refactoring.guru/uk/design-patterns/abstract-factory", \
        "Incorrect abstract factory url"
    assert patterns_page.get_abstract_factory_header() == "Абстрактна фабрика", "Incorrect abstract factory header"


@allure.title("Test open book in browser")
@allure.description("Go to the page 'Deep to patterns' and open book in the browser using btn.")
@allure.tag("Button", "Patterns", "Book", "Browser")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_open_book_in_browser(open_patterns_page):
    patterns_page = open_patterns_page
    patterns_page.click_deep_to_patterns_btn()
    patterns_page.click_open_book_in_browser_btn()
    assert patterns_page.get_page_url() == "https://refactoring.guru/files/design-patterns-uk-demo.pdf", \
        "Can't open book in browser"


@allure.title("Test check number and text of 'Go to article btns'")
@allure.description("Open patterns page and check number and text of 'Go to article btns'")
@allure.tag("Button", "Text", "Number", "Patterns")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_go_to_articles_btns(open_patterns_page):
    patterns_page = open_patterns_page
    exc_count = 6
    assert patterns_page.buttons_go_to_articles_get_count() == exc_count, "There should be 6 article buttons"
    assert patterns_page.get_catalog_patterns_btn_text() == "Зазирнути у каталог", "Incorrect catalog button text"
    assert patterns_page.get_what_is_pattern_btn_text() == "Що таке патерн?", "Incorrect what is pattern button text"
    assert patterns_page.get_patterns_group_btn_text() == "Докладніше про групи", "Incorrect patterns group button text"
    assert patterns_page.get_pattern_usage_btn_text() == "Докладніше про користь", \
        "Incorrect patterns usage button text"
    assert patterns_page.get_pattern_story_btn_text() == "Докладніше про історію", "Incorrect pattern story button text"
    assert patterns_page.get_pattern_downsides_btn_text() == "Докладніше про критику", \
        "Incorrect pattern downsides button text"


@allure.title("Test bridge code example is visible'")
@allure.description("Open patterns page and go to the patterns catalog. Go to the pattern bridge page,"
                    " choose python code example and check if it`s visible.")
@allure.tag("Patterns", "Bridge", "Code", "Visible")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_pattern_bridge_code_example(open_patterns_page):
    pattern_page = open_patterns_page
    pattern_page.click_catalog_patterns_btn()
    pattern_page.click_pattern_bridge_btn()
    pattern_page.click_python_bridge_bth()
    assert pattern_page.get_python_header_text() == "main.py: Приклад структури патерна"
    assert pattern_page.python_code_is_displayed(), "Python code is not displayed"
    assert pattern_page.get_page_url() == "https://refactoring.guru/uk/design-patterns/bridge/python/example", \
        "Incorrect python bridge code example url"
