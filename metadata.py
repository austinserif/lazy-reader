"""file containing class spec for Metadata Article"""
import extruct
from w3lib.html import get_base_url

class Metadata:
    """Create Metadata instance from html string and url string"""
    def __init__(self, html: str, url: str):
        self.html = html
        self.base_url = get_base_url(html, url)

    def parse(self) -> dict:
        """parse metadata and return JSON/dict containing metadata"""
        data = extruct.extract(self.html, base_url=self.base_url)
        return data
        
