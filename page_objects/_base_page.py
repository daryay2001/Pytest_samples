from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from utilities.deco import auto_step


@auto_step
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator, timeout=5)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator, timeout=10)
        el.click()

    def get_text(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.text

    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    # self.driver.current_url - повертає поточну url
    # self.driver.page_source - повертає повністю тектс сторінки html (перевірити)
    # і потім if text in self.driver.page_source

    def wait_element_is_presence(self, locator: tuple, timeout=5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def get_current_url(self):  # повертає поточну url
        return self.driver.current_url

    def scroll_into_view(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def send_key(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def get_elements_count(self, locator: tuple):
        self.wait_element_is_presence(locator)
        elements = self.driver.find_elements(*locator)
        return len(elements)

    def get_text_with_index(self, locator: tuple, index=1):
        self.wait_element_is_visible(locator)
        element = self.driver.find_elements(*locator)
        if len(element) < index-1:
            raise NoSuchElementException(str(locator) + f"by index=({index})")
        return element[index-1].text

    def get_attribute(self, locator: tuple, attribute="value"):
        el = self.wait_element_is_presence(locator)
        return el.get_attribute(attribute)

    def click_by_js(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].click()', el)

    def scroll_to_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        ActionChains(self.driver).scroll_to_element(el).perform()

    def get_page_source(self):
        return self.driver.page_source  # повертає повністю тектс сторінки html

    def switch_to_iframe(self, locator: tuple):
        iframe_element = self.driver.find_element(locator)
        self.driver.switch_to.frame(iframe_element)

    def switch_to_default_page(self):
        self.driver.switch_to.default_content()
