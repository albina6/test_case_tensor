import os
import pytest
from .pages.pages_sbis.base_page_sbis import BasePageSBIS
from .pages.pages_sbis.download_page_sbis import DownloadPageSBIS


class TestSBISGoToDownload:
    '''
    TODO: maybe we need to delete downloaded files
    '''
    FILE_NAME = "file_for_check.exe"
    @pytest.fixture()
    def base_page(self, browser):
        link = 'https://sbis.ru/'
        page = BasePageSBIS(browser, link)
        page.open()
        yield page

        try:
            os.remove(self.FILE_NAME)
        except OSError:
            pass

    def test_download_plugin_for_windows(self, base_page):
        #        This Third Script (question)
        base_page.go_download_page()

        download_page = DownloadPageSBIS(base_page.browser, base_page.browser.current_url)
        download_page.download_plugin_web_setup(self.FILE_NAME)
