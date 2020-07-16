import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_lg")

def textualize(text: str) -> spacy.tokens.doc.Doc:
    """takes a string and returns instance of a spacy Doc object"""
    doc = nlp(text)
    return doc