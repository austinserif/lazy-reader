from unittest import TestCase
from article import Article

class TestArticle(TestCase):

    @classmethod
    def setUpClass(cls):
        """set up method for test article testing class"""
        cls.test_url = "https://www.cnn.com/2020/07/08/politics/trump-cdc-school-guidelines-funding/index.html"

    def test_read(self):
        """test the Article.read() class method for correctly retrieving title and body text from an article"""
        article_obj = Article.read(self.test_url)
        self.assertIn("Trump trashes CDC", article_obj.title.text)
        self.assertIn("The move came as the Trump administration makes a concerted", article_obj.body.text)

    def test_article_text(self):
        """test the Article.article_test() class method"""
        with open('/Users/austin/Desktop/lazy-reader/tests/sample_html.txt', 'r') as infile:
            html = infile.read()
        article_dict = Article.article_text(html)
        self.assertIsInstance(article_dict, dict)
        self.assertIn('title', article_dict)
        self.assertIn('body', article_dict)
        self.assertIn('The move came as the Trump administration makes a concerted', article_dict['body'])
        self.assertIn('Trump trashes CDC', article_dict['title'])
        self.assertIn("'\'", html)
        self.assertNotIn("'/'", article_dict['body'])

    def test_get_nouns(self):
        """test the Article.get_nouns() method"""
        # TODO: Write Test
        return

    def test_get_verbs(self):
        """test the Article.get_verbs() method"""
        # TODO: Write Test
        return

    def test_get_ents(self):
        """test the Article.get_ents() method"""
        # TODO: Write Test
        return
    
    def test_get_metadata(self):
        """teset the Artile.get_metadata() method"""
        # TODO: Write Test
        return