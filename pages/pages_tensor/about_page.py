from .base_page_tensor import BasePageTensor
from .locators_tensor import AboutLocatorsTensor


class AboutPageTensor(BasePageTensor):
    def should_be_equal_size_img_in_works_block(self):
        works_block = self.browser.find_element(*AboutLocatorsTensor.BLOCK_WORKS)
        img_list_works_block = works_block.find_elements(*AboutLocatorsTensor.IMG_IN_BLOCKS)

        width_img = img_list_works_block[0].get_attribute("width")
        height_img = img_list_works_block[0].get_attribute("height")

        for ind, img in enumerate(img_list_works_block[1:], 2):
            assert width_img == img.get_attribute("width"), f"Width img_{ind} not equal width img_0"
            assert height_img == img.get_attribute("height"), f"Height img_{ind} not equal height img_0"
