from selenium.common.exceptions import (NoSuchElementException)


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def check_current_url_equal_enter_url(self, enter_url):
        current_url = self.browser.current_url
        assert current_url == enter_url, f"Current url {current_url} != enter_url{enter_url}"
