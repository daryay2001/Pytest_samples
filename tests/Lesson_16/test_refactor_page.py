import pytest
import allure


@allure.title("Test clean code page")
@allure.description("Open refactor page, go to the clean code page by btn."
                    " Check the first paragraph is in page text and check url of the page.")
@allure.tag("Refactor", "Text", "Url")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_clean_code_page(open_refactor_page):
    page = open_refactor_page
    page.click_clean_code_btn()
    clean_code_paragr = page.get_clean_code_first_paragr_text()
    assert page._page.get_current_url() == "https://refactoring.guru/uk/refactoring/what-is-refactoring", \
        "Incorrect clean code page url"
    assert clean_code_paragr in page._page.get_page_source(), "No refactoring definition"


@allure.title("Test url of the privacy policy page")
@allure.description("Open refactor page, go to privacy policy page via link. Check its url")
@allure.tag("Refactor", "Url", "Policy", "Link")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_privacy_policy_page_load(open_refactor_page):
    page = open_refactor_page
    page.click_polityka_konf_link()
    assert page.get_page_url() == "https://refactoring.guru/uk/privacy-policy", "Incorrect url for policy"


@allure.title("Test home button is functioning")
@allure.description("Open refactor page, go to the, dirty code page,"
                    " go to main page via 'home button'. Check main page url.")
@allure.tag("Refactor", "Url", "Button", "Home page")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_home_btn(open_refactor_page):
    page = open_refactor_page
    page.click_show_more_dirty_code_btn()
    page.click_home_btn()
    assert page.get_page_url() == "https://refactoring.guru/", "Incorrect url, should be main page"


@allure.title("Test go to technical debt article page")
@allure.description("Open refactor page, go to start from the beginning btn,"
                    " go to technical debt page via btn,  go to technical debt article page. Check its url.")
@allure.tag("Refactor", "Url", "Technical", "Article")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_go_to_techn_debt_article(open_refactor_page):
    page = open_refactor_page
    page.click_start_from_beginning_btn()
    page.click_techn_debt_btn()
    page.click_techn_debt_article_btn()
    assert page.get_page_url() == "https://wiki.c2.com/?WardExplainsDebtMetaphor", "Incorrect article url"


@allure.title("Test check code containers count")
@allure.description("Open refactor page, click 'show more technics' btn,"
                    " go to extract method via link, check number of code containers.")
@allure.tag("Refactor", "Url", "Number", "Code", "Container")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_check_code_containers_count(open_refactor_page):
    page = open_refactor_page
    page.click_refactor_techn_show_more_btn()
    page.click_extract_method_link()
    exc_cont_count = 2
    assert page.code_containers_get_count() == exc_cont_count, "Incorrect number of code containers"
