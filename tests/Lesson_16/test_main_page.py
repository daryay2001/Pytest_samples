def test_biggest_header_text(open_main_page):
    main_page = open_main_page
    assert main_page.get_biggest_header_text() == "Hello, world! Привіт!", "Incorrect header"


def test_boy_top_img_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_boy_top_img_displayed(), "Boy top img is not displayed"


def test_wine_top_img_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_wine_img_displayed(), "Wine top img is not displayed"


def test_is_lang_btn_displayed(open_main_page):
    main_page = open_main_page
    assert main_page.is_lang_btn_displayed(), "Lang button is not displayed"


def test_signature_text(open_main_page):
    main_page = open_main_page
    assert main_page.get_signature_name_text() == "— Олександр Швець", "Not correct signature"


# писати більш функціональні тести, а не лише що щось відображається

def test_change_lang_to_eng(open_main_page):
    main_page = open_main_page
    main_page.click_lang_btn()
    main_page.click_engl_btn()
    current_url = main_page.get_main_page_url()
    assert current_url == "https://refactoring.guru/", "Incorrect url for english lang"
    assert main_page.get_biggest_header_text() == "Hello, world!", "Incorrect header1 for english lang"


def test_go_to_pattern_page_btn(open_main_page):
    page = open_main_page
    page.click_go_to_pattern_btn()
    current_url = page.get_main_page_url()
    assert current_url == "https://refactoring.guru/uk/design-patterns", "Incorrect url for patterns page"
    assert page.get_biggest_header_text() == "ПАТЕРНИ\nПРОЕКТУВАННЯ", "Incorrect header1 for patterns page"


def test_open_new_topic_form(open_main_page):
    page = open_main_page
    page.click_forum_btn()
    # page.click_find_input()
    page.set_word_to_find()
    page.click_add_topic_btn()
    assert page.get_forum_form_header_text() == "Створити нову тему", "Incorrect form header"
