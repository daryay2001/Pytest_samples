def test_logo_main_page(open_main_page):
    main_page = open_main_page
    assert main_page.is_top_logo_displayed(), "Logo is not displayed"
