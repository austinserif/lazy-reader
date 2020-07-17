from unittest import TestCase
from metadata import Metadata

class TestMetadata(TestCase):

    @classmethod
    def setUpClass(cls):
        """set up method for test metadata testing class"""
        with open('/Users/austin/Desktop/lazy-reader/tests/sample_html.txt', 'r') as infile:
            sample_url = infile.read() 
        cls.url = sample_url

    def test__parse(self):
        """test whether Metadata.parse() returns JSON containing from html 
        passed to the constructor metadata"""
        
        with open('/Users/austin/Desktop/lazy-reader/tests/sample_html.txt', 'r') as infile:
            html = infile.read()
        
        metadata_obj = Metadata(html, self.url)
        data = metadata_obj.parse()
        self.assertIn('author', data['microdata'][0]['properties'].keys())
        self.assertIn('headline', data['microdata'][0]['properties'].keys())
        self.assertIn('NewsArticle', data['microdata'][0]['type'])




