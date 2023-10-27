from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage


class RefactoringPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_mail_logo = (By.XPATH, "//*[@class='fa fa-fw fa-envelope']")
    __loc_format_btn = (By.XPATH, '//*[@class="re-icon-format"]/..')
    __loc_format_header2 = (By.XPATH, "//*[text()='Заголовок 2']")
    __loc_polityka_konf_link = (By.XPATH, "//*[text()='Політика конфіденційності']/..")
    __loc_show_more_dirty_code_btn = (By.XPATH, "//div[@class='ref2-b ref-abs ref-l ref-b']/span/a")
    __loc_home_btn = (By.XPATH, "//a[@class='home']")
    __loc_start_from_beginning_btn = (By.XPATH, "(//a[@class='btn btn-primary'])[1]")
    __loc_techn_debt_btn = (By.XPATH, "//a[@rel='next']")
    __loc_techn_debt_article_btn = (By.XPATH, "//p[2]/a")
    __loc_refactor_techn_show_more_btn = (By.XPATH, "(//a[@class='btn btn-primary'])[6]")
    __loc_extract_method_btn = (By.XPATH, "//a[text()='Extract Method']")
    __loc_python_btn = (By.XPATH, "//a[@data-lang='python']")
    __loc_code_containers = (By.XPATH, "//pre[@lang='java']")
    __loc_show_more_clean_code = (By.XPATH, '(//*[@class="btn btn-primary"])[3]')
    __loc_clean_code_first_paragr = (By.XPATH, "(//div[@class='page text']/article/p)[1]")

    def get_page_url(self):
        return self._page.get_current_url()

    def get_header_btn_text(self):
        self._page.wait_element_is_presence(self.__loc_format_header2)
        return self._page.get_text(self.__loc_format_header2)

    def click_polityka_konf_link(self):
        self._page.scroll_into_view(self.__loc_polityka_konf_link)
        self._page.click(self.__loc_polityka_konf_link)

    def click_show_more_dirty_code_btn(self):
        self._page.click(self.__loc_show_more_dirty_code_btn)

    def click_home_btn(self):
        self._page.click(self.__loc_home_btn)

    def click_start_from_beginning_btn(self):
        self._page.click(self.__loc_start_from_beginning_btn)

    def click_techn_debt_btn(self):
        self._page.scroll_into_view(self.__loc_techn_debt_btn)
        self._page.click(self.__loc_techn_debt_btn)

    def click_techn_debt_article_btn(self):
        self._page.click(self.__loc_techn_debt_article_btn)

    def click_refactor_techn_show_more_btn(self):
        self._page.scroll_into_view(self.__loc_refactor_techn_show_more_btn)
        self._page.click(self.__loc_refactor_techn_show_more_btn)

    def click_extract_method_link(self):
        self._page.click(self.__loc_extract_method_btn)

    def code_containers_get_count(self):
        return self._page.get_elements_count(self.__loc_code_containers)

    def click_clean_code_btn(self):
        self._page.scroll_to_element(self.__loc_show_more_clean_code)
        self._page.click(self.__loc_show_more_clean_code)

    def get_clean_code_first_paragr_text(self):
        return self._page.get_text(self.__loc_clean_code_first_paragr)
