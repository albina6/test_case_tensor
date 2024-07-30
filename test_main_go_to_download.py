import os
import pytest
from .pages.pages_sbis.base_page_sbis import BasePageSBIS
from .pages.pages_sbis.download_page_sbis import DownloadPageSBIS


class TestSBISGoToDownload:
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
        '''
        This Third Script (question)

        1) Перейти на https://sbis.ru/
        2) В Footer'e найти и перейти "Скачать локальные версии"
        3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом
        4) Убедиться, что плагин скачался
        5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте (в примере 3.64 МБ).

        В данной реализации было принято решение осуществлять проверку размера скаченного файла
            внутри функции скачивания (автор считает что в данном случае можно нарушить правило
            одна функция – одна ответственность, возможно в будущем при расширении функции,
            реализация проверки будет выделена в отдельную функцию )
        '''
        base_page.go_download_page()

        download_page = DownloadPageSBIS(base_page.browser, base_page.browser.current_url)
        download_page.download_plugin_web_setup(self.FILE_NAME)
