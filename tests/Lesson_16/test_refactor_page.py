import pytest


@pytest.mark.regression
def test_clean_code_page(open_refactor_page):
    page = open_refactor_page
    page.click_clean_code_btn()
    clean_code_paragr = page.get_clean_code_first_paragr_text()
    assert page._page.get_current_url() == "https://refactoring.guru/uk/refactoring/what-is-refactoring", \
        "Incorrect clean code page url"
    assert clean_code_paragr in page._page.get_page_source(), "No refactoring definition"


@pytest.mark.smoke
def test_privacy_policy_page_load(open_refactor_page):
    page = open_refactor_page
    page.click_polityka_konf_link()
    assert page.get_page_url() == "https://refactoring.guru/uk/privacy-policy", "Incorrect url for policy"


@pytest.mark.smoke
def test_home_btn(open_refactor_page):
    page = open_refactor_page
    page.click_show_more_dirty_code_btn()
    page.click_home_btn()
    assert page.get_page_url() == "https://refactoring.guru/", "Incorrect url, should be main page"


@pytest.mark.regression
def test_go_to_techn_debt_article(open_refactor_page):
    page = open_refactor_page
    page.click_start_from_beginning_btn()
    page.click_techn_debt_btn()
    page.click_techn_debt_article_btn()
    assert page.get_page_url() == "https://wiki.c2.com/?WardExplainsDebtMetaphor", "Incorrect article url"


@pytest.mark.regression
def test_check_code_containers_count(open_refactor_page):
    page = open_refactor_page
    page.click_refactor_techn_show_more_btn()
    page.click_extract_method_link()
    exc_cont_count = 2
    assert page.code_containers_get_count() == exc_cont_count, "Incorrect number of code containers"
