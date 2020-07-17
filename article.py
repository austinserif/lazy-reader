import requests
from requests import HTTPError

import spacy

from bs4 import BeautifulSoup
from nlp import textualize
from metadata import Metadata

class Article:
    """Article Class, instantiated with two strings: the title and body url of an article"""
    def __init__(self, title: str, body: str):
        self.title = textualize(title)
        self.body = textualize(body)
    
    @classmethod
    def read(cls, url: str) -> 'Article':
        """takes url as an argument and returns instance of an Article, otherwise raising an HTTPError"""
        try:
            response = requests.get(url)
            html = response.text
            text = cls.article_text(html)
            return Article(text['title'], text['body'])
        except HTTPError as e:
            print(e)

    @classmethod
    def article_text(cls, html: str) -> dict:
        """takes html string as an argument and returns the article content as plain text.
        **NOTE** Current iteration of this method only supports parsing of HTML scraped 
        from CNN, or other sites with same HTML tags."""
        structured_data = BeautifulSoup(html, 'html.parser')
        title = structured_data.find('h1').text

        #join list into string and remove escape characters ('/')
        body = "".join([sentence.text for sentence in structured_data.find_all('div',{'class':'zn-body__paragraph'})]).replace("/", "")
        return {'title': title, 'body': body}
    
    def get_nouns(self, doc: spacy.tokens.doc.Doc) -> list:
        """returns array of nouns for passed Doc instance"""
        return [chunk.text for chunk in doc.noun_chunks]
    
    def get_verbs(self, doc: spacy.tokens.doc.Doc) -> list:
        """returns array of verbs for passed Doc instance"""
        return [token.lemma_ for token in doc if token.pos_ == "VERB"]

    def get_ents(self, doc: spacy.tokens.doc.Doc) -> dict:
        """returns dict of {entity: entity_type} key/value pairs for passed Doc instance"""
        return {entity.text : entity.label_ for entity in doc.ents}
    
    def get_metadata(self) -> Metadata:
        """returns Metadata object"""
        # TODO: finish method
        return