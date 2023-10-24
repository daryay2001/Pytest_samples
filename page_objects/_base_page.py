from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait_element_is_presence(self, locator: tuple, timeout=3) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def scroll_into_view(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def send_key(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)




