from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage


class StorePage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_books_imges = (By.XPATH, "//div[@class='image3d-cover']")
    __loc_under_books_text = (By.XPATH, "//*[@class='offer-text']")
    __loc_books_price = (By.XPATH, "//*[@class='new-price font-money']")
    __loc_show_more_btns = (By.XPATH, "//a[@class='btn btn-block btn-outline-primary']")
    __loc_div_show_more_btns = (By.XPATH, "//div[@class='more-info']")
    __loc_buy_now_btn = (By.XPATH, "(//i[@class='fa fa-shopping-cart'])[2]/..")
    __loc_cart_refactor_book_input = (By.XPATH, "(//input[@type='number'])[1]")
    __loc_cart_minus_refactor_btn = (By.XPATH, "(//*[@class='w-6 h-6'])[1]/..")
    __loc_cart_plus_refactor_btn = (By.XPATH, "(//*[@class='w-6 h-6'])[2]/..")
    __loc_clear_cart_btn = (By.XPATH, "//a[@class='cart-item-action cart-item-action-remove btn btn-sm btn-danger']")
    __loc_empty_cart_message = (By.XPATH, "//*[@class='cart-empty']")

    def books_get_count(self):
        return self._page.get_elements_count(self.__loc_books_imges)

    def get_page_url(self):
        return self._page.get_current_url()

    def book_get_info(self, index=1):
        _by, _loc = self.__loc_under_books_text
        self._page.scroll_into_view((_by, f"({_loc})[{index}]"))
        data = {
            "sale": self._page.get_text_with_index(self.__loc_under_books_text, index),
            "price": self._page.get_text_with_index(self.__loc_books_price, index)
        }
        return data

    def button_show_more_get_count(self):
        self._page.scroll_into_view(self.__loc_div_show_more_btns)
        return self._page.get_elements_count(self.__loc_div_show_more_btns)

    def button_show_more_get_text(self, index=1):
        _by, _loc = self.__loc_show_more_btns
        self._page.scroll_into_view((_by, f"({_loc})[{index}]"))
        data = {
            "info": self._page.get_text_with_index(self.__loc_show_more_btns, index),
        }
        return data

    def add_product_to_cart(self):
        self._page.click(self.__loc_buy_now_btn)

    def cart_get_counter(self):
        return self._page.get_attribute(self.__loc_cart_refactor_book_input)

    def click_plus_btn(self):
        self._page.click_by_js(self.__loc_cart_plus_refactor_btn)

    def click_minus_btn(self):
        self._page.click_by_js(self.__loc_cart_minus_refactor_btn)

    def click_clear_cart_btn(self):
        self._page.wait_element_is_presence(self.__loc_clear_cart_btn)
        self._page.click(self.__loc_clear_cart_btn)

    def empty_cart_get_text(self):
        data = self._page.get_text(self.__loc_empty_cart_message)
        return data


