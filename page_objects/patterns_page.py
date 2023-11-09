from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from utilities.deco import auto_step


@auto_step
class PatternsPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_catalog_patterns_btn = (By.XPATH, "(//a[@class='btn btn-primary'])[2]")
    __loc_creational_patterns_links = (By.CSS_SELECTOR, "div.creational-patterns a")
    __loc_factory_method_btn = (By.CSS_SELECTOR, "div.creational-patterns > :first-child")
    __loc_abstract_factory_link = (By.XPATH, "//*[@class='section pseudocode']/p/a")
    __loc_biggest_header = (By.XPATH, "//h1")
    __loc_deep_to_patterns_btn = (By.CSS_SELECTOR, "div.dp7-b.dp-abs.dp-c.dp-b a")
    __loc_open_book_in_browser_btn = (By.CSS_SELECTOR, ".demo div > :first-child")
    __loc_go_to_article_btns = (By.XPATH, "//a[starts-with(@class, 'btn btn-primary')]")
    __loc_what_is_pattern_btn = (By.XPATH, "(//a[starts-with(@class, 'btn btn-primary')])[1]")
    __loc_patterns_group_btn = (By.XPATH, "(//a[starts-with(@class, 'btn btn-primary')])[4]")
    __loc_pattern_usage_btn = (By.XPATH, "(//a[starts-with(@class, 'btn btn-primary')])[3]")
    __loc_pattern_story_btn = (By.XPATH, "(//a[starts-with(@class, 'btn btn-primary')])[5]")
    __loc_pattern_downsides_btn = (By.XPATH, "(//a[starts-with(@class, 'btn btn-primary')])[6]")
    __loc_pattern_bridge_btn = (By.CSS_SELECTOR, "a.pattern-card.bridge")
    __loc_bridge_python_btn = (By.XPATH, "(//div[@class='section implementations']/p/a)[6]")
    __loc_python_header = (By.XPATH, "(//h4)[1]")
    __loc_code_container = (By.XPATH, '(//pre[@class="code cm-s-default CodeMirror"])[1]')

    def get_page_url(self):
        return self._page.get_current_url()

    def creational_patterns_get_count(self):
        return self._page.get_elements_count(self.__loc_creational_patterns_links)

    def click_catalog_patterns_btn(self):
        self._page.scroll_to_element(self.__loc_catalog_patterns_btn)
        self._page.wait_element_is_visible(self.__loc_catalog_patterns_btn)
        self._page.click(self.__loc_catalog_patterns_btn)

    def click_factory_method_btn(self):
        self._page.click(self.__loc_factory_method_btn)

    def click_abstract_factory_link(self):
        self._page.scroll_to_element(self.__loc_abstract_factory_link)
        self._page.click(self.__loc_abstract_factory_link)

    def get_abstract_factory_header(self):
        return self._page.get_text(self.__loc_biggest_header)

    def click_deep_to_patterns_btn(self):
        self._page.scroll_to_element(self.__loc_deep_to_patterns_btn)
        self._page.click(self.__loc_deep_to_patterns_btn)

    def click_open_book_in_browser_btn(self):
        self._page.scroll_to_element(self.__loc_open_book_in_browser_btn)
        self._page.click(self.__loc_open_book_in_browser_btn)

    def buttons_go_to_articles_get_count(self):
        self._page.scroll_to_element(self.__loc_go_to_article_btns)
        return self._page.get_elements_count(self.__loc_go_to_article_btns)

    def get_catalog_patterns_btn_text(self):
        self._page.scroll_to_element(self.__loc_catalog_patterns_btn)
        return self._page.get_text(self.__loc_catalog_patterns_btn)

    def get_what_is_pattern_btn_text(self):
        return self._page.get_text(self.__loc_what_is_pattern_btn)

    def get_patterns_group_btn_text(self):
        self._page.scroll_to_element(self.__loc_patterns_group_btn)
        return self._page.get_text(self.__loc_patterns_group_btn)

    def get_pattern_usage_btn_text(self):
        self._page.scroll_to_element(self.__loc_pattern_usage_btn)
        return self._page.get_text(self.__loc_pattern_usage_btn)

    def get_pattern_story_btn_text(self):
        self._page.scroll_to_element(self.__loc_pattern_story_btn)
        return self._page.get_text(self.__loc_pattern_story_btn)

    def get_pattern_downsides_btn_text(self):
        self._page.scroll_to_element(self.__loc_pattern_downsides_btn)
        return self._page.get_text(self.__loc_pattern_downsides_btn)

    def click_pattern_bridge_btn(self):
        self._page.scroll_to_element(self.__loc_pattern_bridge_btn)
        self._page.click(self.__loc_pattern_bridge_btn)

    def click_python_bridge_bth(self):
        self._page.scroll_to_element(self.__loc_bridge_python_btn)
        self._page.click(self.__loc_bridge_python_btn)

    def get_python_header_text(self):
        self._page.scroll_to_element(self.__loc_python_header)
        return self._page.get_text(self.__loc_python_header)

    def python_code_is_displayed(self):
        self._page.scroll_to_element(self.__loc_code_container)
        return self._page.is_displayed(self.__loc_code_container)
