from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from utilities.deco import auto_step


@auto_step
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
    __word_to_find = "pattern"  # щоб потім доробити з iframe, коли дойдемо
    __loc_forum_search_input = (By.XPATH, "//*[@id='search']")  # щоб потім доробити з iframe, коли дойдемо
    __loc_add_topic_btn = (By.XPATH, "//*[@id='add-topic-button']")  # щоб потім доробити з iframe, коли дойдемо
    __loc_new_topic_header = (By.XPATH, "(//h4[@class='modal-title'])[1]")  # щоб потім доробити з iframe, коли дойдемо
    __loc_iframe = (By.XPATH, '//iframe[contains(@src, "//feedback")]')  # щоб потім доробити з iframe, коли дойдемо
    __loc_email_input = (By.XPATH, "//div[@class='input-group']/input")
    __loc_submit_email_btn = (By.XPATH, "//button[@type='submit']")
    __loc_header_confirm = (By.XPATH, "//div[@class='text center-block']/h2")

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

    def click_input_email_btn(self):
        self._page.scroll_to_element(self.__loc_email_input)
        self._page.click_by_js(self.__loc_email_input)

    def set_email(self):
        my_email = "myemail@gmail.com"
        self._page.send_keys(self.__loc_email_input, my_email)
        return self

    def click_submit_email_btn(self):
        self._page.click_by_js(self.__loc_submit_email_btn)

    def get_submit_header_text(self):
        return self._page.get_text(self.__loc_header_confirm)

    def click_forum_btn(self):
        self._page.scroll_to_element(self.__loc_forum_btn)
        self._page.click(self.__loc_forum_btn)

    def add_forum_topic(self, my_word=None):
        if my_word is None:
            my_word = self.__word_to_find
        try:
            el_frame = self._page.wait_element_is_visible(self.__loc_iframe, timeout=7)
            self._page.driver.switch_to.frame(el_frame)
            self._page.send_keys(self.__loc_forum_search_input, my_word)
            self._page.click(self.__loc_add_topic_btn)
            return self._page.get_text(self.__loc_new_topic_header)
        finally:
            self._page.driver.switch_to.default_content()
