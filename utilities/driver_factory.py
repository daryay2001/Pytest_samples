from selenium.webdriver import Chrome, Edge, ChromeOptions, Keys

_CHROME_ID = 1
_EDGE_ID = 2


class DriverFactory:
    def __init__(self, browser_id: int):
        self.__browser_id = browser_id

    def get_driver(self):
        if int(self.__browser_id) == _CHROME_ID:
            return self.__get_chrome_driver()
        elif int(self.__browser_id) == _EDGE_ID:
            return self.__get_edge_driver()
        else:
            return self.__get_chrome_driver()

    @staticmethod
    def __get_chrome_driver():
        _options = ChromeOptions()
        _options.browser_version = "114"
        driver = Chrome(options=_options)
        return driver

    @staticmethod
    def __get_edge_driver():
        driver = Edge()
        return driver
    
