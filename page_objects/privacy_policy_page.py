from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from utilities.deco import auto_step


@auto_step
class PolicyPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_biggest_header = (By.XPATH, "//h1")
    __loc_google_policies_link = (By.XPATH, "//h3[text()='Behavioral Remarketing']/preceding-sibling::p[1]/a")
    __loc_google_policies_first_paragraph = (By.XPATH, "//div[@class='nrAB0c KMMDve']/p[@class='q0cs9b']")
    __loc_personal_data_li = (By.XPATH, "(//h4/following-sibling::ul)[1]/li")
    __loc_cookies_data = (By.XPATH, "((//h4/following-sibling::ul)[1]/li)[5]")
    __loc_advert_policy_link = (By.XPATH, "(//h3[text()='Behavioral Remarketing']/following-sibling::p[9]/a)[2]")
    __loc_advert_introduct_paragraph = (By.XPATH, "(//div[@class='sqs-html-content'])[1]/p[1]")
    __loc_content_usage_link = (By.XPATH, "//span[text()='Використання контенту']/..")
    __loc_citation_info = (By.XPATH, "(//article/ul/li)[1]")
    __loc_illustration_info = (By.XPATH, "(//article/ul/li)[2]")

    def get_page_url(self):
        return self._page.get_current_url()

    def get_biggest_header_text(self):
        return self._page.get_text(self.__loc_biggest_header)

    def click_google_policies_link(self):
        self._page.scroll_to_element(self.__loc_google_policies_link)
        self._page.click(self.__loc_google_policies_link)

    def get_google_policies_first_paragraph_text(self):
        self._page.wait_element_is_visible(self.__loc_google_policies_first_paragraph)
        return self._page.get_text(self.__loc_google_policies_first_paragraph)

    def get_personal_data_li_text(self, index=1):
        _by, _loc = self.__loc_personal_data_li
        self._page.scroll_to_element((_by, f'({_loc})[{index}]'))
        data = {
            'info': self._page.get_text_with_index(self.__loc_personal_data_li, index),
        }
        return data

    def get_count_personal_data(self):
        self._page.scroll_to_element(self.__loc_cookies_data)
        return self._page.get_elements_count(self.__loc_personal_data_li)

    def click_advert_policy_link(self):
        self._page.scroll_to_element(self.__loc_advert_policy_link)
        self._page.click_by_js(self.__loc_advert_policy_link)

    def get_adver_introduct_text(self):
        return self._page.get_text(self.__loc_advert_introduct_paragraph)

    def click_usage_content_link(self):
        self._page.scroll_to_element(self.__loc_content_usage_link)
        self._page.click_by_js(self.__loc_content_usage_link)

    def get_citation_info_text(self):
        return self._page.get_text(self.__loc_citation_info)

    def get_illustration_info_text(self):
        return self._page.get_text(self.__loc_illustration_info)
