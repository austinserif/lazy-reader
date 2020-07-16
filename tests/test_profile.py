from unittest import TestCase
from _profile import Profile

import spacy
import requests
from bs4 import BeautifulSoup


class TestProfile(TestCase):

    @classmethod
    def setUpClass(cls):
        """set up method for test profile testing class"""

        #scrape with requests
        url = "https://www.cnn.com/2020/07/08/politics/trump-cdc-school-guidelines-funding/index.html"
        response = requests.get(url)
        html = response.text

        #parse with bs4
        structured_data = BeautifulSoup(html, 'html.parser')
        body = "".join([sentence.text for sentence in structured_data.find_all('div',{'class':'zn-body__paragraph'})])

        #nlp with spacy
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(body)

        cls.ents = {entity.text : entity.label_ for entity in doc.ents}

    def test_new(self):
        """test the Profile.new() class method, should test whether a correct Profile instance is returned"""
        profile_obj = Profile.new('Donald Trump', self.ents['Trump'])
        self.assertEqual("Donald Trump", profile_obj.entity)
        self.assertEqual("PERSON", profile_obj.entity_type)