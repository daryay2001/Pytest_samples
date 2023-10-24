from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage


class MainPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_top_logo = (
    By.XPATH, "//aside[@class='sidebar main-menu']/following-sibling::nav/div/a")  # Верхній логотип єнота
    __loc_biggest_header = (By.XPATH, "//h1")
    __loc_boy_top_img = (By.XPATH, "//div[starts-with(@class, 'announ')]/a/img[1]")
    __loc_wine_top_img = (By.CSS_SELECTOR, "span[class*='announ'] + img")
    __loc_lang_btn = (By.XPATH, "//button[@class='dropdown-toggle']")
    __loc_signature_name_text = (By.CSS_SELECTOR, "p.col-12.col-sm-6.col-md-4.signature b")
    __loc_eng_lang = (By.XPATH, "//*[@data-locale='en']")
    __loc_patterns_btn = (By.XPATH, "//a[text()='Патерни']")
    __loc_forum_btn = (By.XPATH, "//a[text()='Форум']")
    __word_to_find = "pattern"
    __loc_forum_search_input = (By.XPATH, "//*[@id='search']")
    __loc_add_topic_btn = (By.XPATH, "//*[@id='add-topic-button']")
    __loc_new_topic_header = (By.XPATH, "(//h4[@class='modal-title'])[1]")

    def is_top_logo_displayed(self):
        return self._page.is_displayed(self.__loc_top_logo)

    def get_biggest_header_text(self):
        data = self._page.get_text(self.__loc_biggest_header)
        return data

    def is_boy_top_img_displayed(self):
        return self._page.is_displayed(self.__loc_boy_top_img)

    def is_wine_img_displayed(self):
        return self._page.is_displayed(self.__loc_wine_top_img)

    def is_lang_btn_displayed(self):
        return self._page.is_displayed(self.__loc_lang_btn)

    def get_signature_name_text(self):
        return self._page.get_text(self.__loc_signature_name_text)

    def is_eng_lang_choice_displayed(self):
        return self._page.is_displayed(self.__loc_eng_lang)

    def click_lang_btn(self):
        self._page.click(self.__loc_lang_btn)

    def click_engl_btn(self):
        self._page.wait_element_is_presence(self.__loc_eng_lang)
        self._page.click(self.__loc_eng_lang)

    def get_main_page_url(self):
        return self._page.get_current_url()

    def click_go_to_pattern_btn(self):
        self._page.scroll_into_view(self.__loc_patterns_btn)
        self._page.wait_element_is_presence(self.__loc_patterns_btn)
        self._page.click(self.__loc_patterns_btn)

    def click_forum_btn(self):
        self._page.scroll_into_view(self.__loc_forum_btn)
        self._page.click(self.__loc_forum_btn)

    def click_find_input(self):
        self._page.click(self.__loc_forum_search_input)

    def set_word_to_find(self):
        self._page.send_keys(self.__loc_forum_search_input, self.__word_to_find)
        return self

    def click_add_topic_btn(self):
        self._page.click(self.__loc_add_topic_btn)

    def get_forum_form_header_text(self):
        return self._page.get_text(self.__loc_new_topic_header)
