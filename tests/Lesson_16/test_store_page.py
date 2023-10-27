import pytest


@pytest.mark.smoke
def test_check_books_count(open_store_page):
    store_page = open_store_page
    exc_book_count = 2
    assert store_page.books_get_count() == exc_book_count, "Number of books should be 2"


@pytest.mark.regression
def test_check_book_info(open_store_page):
    store_page = open_store_page
    book_info = store_page.book_get_info(index=1)
    assert book_info["sale"] == "Осінній РОЗПРОДАЖ", "Incorrect sale message"
    assert book_info["price"] == "Осінній РОЗПРОДАЖ\n539 ₴", "Incorrect sale price"


@pytest.mark.smoke
def test_show_more_btns(open_store_page):
    store_page = open_store_page
    exc_count = 2
    exc_info = "Дізнатися більше"
    button_info = store_page.button_show_more_get_text(index=1)
    assert store_page.button_show_more_get_count() == exc_count, "Incorrect number of buttons, should be 2"
    assert button_info["info"] == exc_info, "Incorrect button info"


@pytest.mark.regression
def test_add_to_cart(open_store_page):
    store_page = open_store_page
    store_page.add_product_to_cart()
    exc_count = 1
    assert store_page.cart_get_counter() == str(exc_count), "Wrong number of goods in cart"


@pytest.mark.regression
def test_remove_from_cart(open_store_page):
    store_page = open_store_page
    store_page.add_product_to_cart()
    store_page.click_plus_btn()
    store_page.click_minus_btn()
    exc_count = 1
    assert store_page.cart_get_counter() == str(exc_count), "Wrong number of goods in cart after deleting"


@pytest.mark.regression
def test_empty_cart_message(open_store_page):
    store_page = open_store_page
    store_page.add_product_to_cart()
    store_page.click_clear_cart_btn()
    assert store_page.empty_cart_get_text() == "Ваш кошик порожній (і сумний)", "Incorrect empty cart message"
