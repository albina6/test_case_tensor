import os
import requests

from .base_page_sbis import BasePageSBIS
from .locators_sbis import DownloadLocatorsSBIS


__FILE_NAME_WEB_PLUGIN = "web_plugin_windows"
class DownloadPageSBIS(BasePageSBIS):
    def download_file(self, a_web_elem, file_name):
        file_url = a_web_elem.get_attribute("href")
        # file_name = file_url.rsplit("/", maxsplit=1)[1]
        file_size_in_web = self.size_file_in_text_ref(a_web_elem.text)

        response = requests.get(file_url)
        response.raise_for_status()

        with open(file_name, 'wb') as file:
            file.write(response.content)

        file_size_in_os = os.path.getsize(file_name)
        difference = abs((file_size_in_os / 1048576) - file_size_in_web)
        assert difference < 0.05, \
            f"The difference between the expected and actual file size is more than acceptable {difference}"

    def download_plugin_web_setup(self, file_name):
        ref_download = self.browser.find_element(*DownloadLocatorsSBIS.DOWNLOAD_WEB_SETUP)
        self.download_file(ref_download, file_name)




    def size_file_in_text_ref(self, text):
        '''
        Input text in format like "Скачать (Exe 11.05 МБ) "
        We want to get only float number (We think size only in МБ)
        '''
        size_in_text = text.split("(")[1].split(maxsplit=1)[1].split()[0]
        size = float(size_in_text)
        return size
