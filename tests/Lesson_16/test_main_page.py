import allure
import pytest


@allure.title("Test header text")
@allure.description("Checking header text")
@allure.tag("Header", "Text")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_biggest_header_text(open_main_page):
    main_page = open_main_page
    assert main_page.get_biggest_header_text() == "Hello, world! Привіт!", "Incorrect header"


@allure.description("Checking img is visible")
@allure.tag("Image")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_boy_top_img_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_boy_top_img_displayed(), "Boy top img is not displayed"


@allure.description("Checking img is visible")
@allure.tag("Image")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_wine_top_img_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_wine_img_displayed(), "Wine top img is not displayed"


@allure.description("Checking btn is visible")
@allure.tag("Button")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_is_lang_btn_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_lang_btn_displayed(), "Lang button is not displayed"


@allure.title("Test signature text")
@allure.description("Checking signature text")
@allure.tag("Signature", "Text")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_signature_text(open_main_page):
    main_page = open_main_page
    assert main_page.get_signature_name_text() == "— Олександр Швець", "Not correct signature"


# писати більш функціональні тести, а не лише що щось відображається

@allure.title("Test changing page lang to english")
@allure.description("Checking if it`s possible to change page language to english")
@allure.tag("Language")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_change_lang_to_eng(open_main_page):
    main_page = open_main_page
    main_page.click_lang_btn()
    main_page.click_engl_btn()
    current_url = main_page.get_main_page_url()
    assert current_url == "https://refactoring.guru/", "Incorrect url for english lang"
    assert main_page.get_biggest_header_text() == "Hello, world!", "Incorrect header1 for english lang"


@allure.title("Test changing button 'Go to patterns'")
@allure.description("Trying to go to the pattern page using 'Go to patterns' button")
@allure.tag("Button")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_go_to_pattern_page_btn(open_main_page):
    page = open_main_page
    page.click_go_to_pattern_btn()
    current_url = page.get_main_page_url()
    assert current_url == "https://refactoring.guru/uk/design-patterns", "Incorrect url for patterns page"
    assert page.get_biggest_header_text() == "ПАТЕРНИ\nПРОЕКТУВАННЯ", "Incorrect header1 for patterns page"


@allure.title("Test subscribe via email")
@allure.description("Trying to subscribe on the news using email button")
@allure.tag("Email", "Button")
@allure.label("owner", "Mary Gold")
@pytest.mark.smoke
def test_email_form(open_main_page):
    page = open_main_page
    page.click_input_email_btn()
    page.set_email()
    page.click_submit_email_btn()
    assert page.get_main_page_url() == "https://refactoring.guru/uk/sendy/subscribe", "Incorrect subscribe url"
    assert page.get_submit_header_text() == "Ви підписані!", "Incorrect confirmation"


@allure.title("Test Add new topic to the forum")
@allure.description("Trying to add new topic to the forum, adding it to the input form.")
@allure.tag("Forum", "Input", "Iframe")
@allure.label("owner", "Mary Gold")
@pytest.mark.regression
def test_iframe_add_forum_topic(open_main_page):
    page = open_main_page
    page.click_forum_btn()
    assert page.add_forum_topic() == "Створити нову тему", "Incorrect title of the new topic form"
    assert page.get_main_page_url() == "https://refactoring.guru/uk", "Can`t go to default page"
