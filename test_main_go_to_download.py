from .pages.pages_sbis.base_page_sbis import BasePageSBIS
from .pages.pages_sbis.download_page_sbis import DownloadPageSBIS


class TestSBISGoToDownload:
    '''
    TODO: maybe we need to delete downloaded files
    '''
    def test_download_plugin_for_windows(self, browser):
        link = 'https://sbis.ru/'

        page = BasePageSBIS(browser, link)
        page.open()
        page.go_download_page()

        download_page = DownloadPageSBIS(page.browser, page.browser.current_url)
        download_page.download_plugin_web_setup()
