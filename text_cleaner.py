import spacy
import string
import nltk
from nltk.corpus import stopwords
import re
class TextCleaner:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        nltk.download('stopwords', quiet=True)
        self.stop_words = stopwords.words('english')
        
    def remove_special_characters(self, text):
        # Remove all newlines from the text
        text = text.replace('\n', '')
    
        # Remove hyphenated line breaks
        text = re.sub(r'(\w+)-\s*(\w+)', r'\1\2', text)
    
        # Add a space after periods where the next character is a capital letter without a preceding space
        text = re.sub(r'(?<=\.)(?=[A-Z])', ' ', text)
    
        # Insert a space between concatenated proper nouns or a proper noun followed by a capital letter
        text = re.sub(r'(?<=\w)([A-Z])([a-z]+)', r' \1\2', text)
    
        return text

    def lowercase_text(self, text):
        return text.lower()

    def remove_entities(self, text):
        doc = self.nlp(text)
        return " ".join([token.text for token in doc if not token.ent_type_ in ["ORG", "DATE", "PERSON", "GPE"]])

    def remove_punctuation(self, text):
        punctuation_free = "".join([i for i in text if i not in string.punctuation])
        return punctuation_free

    def remove_stopwords(self, text):
        word_tokens = text.split()
        filtered_text = [word for word in word_tokens if word not in self.stop_words]
        return " ".join(filtered_text)
