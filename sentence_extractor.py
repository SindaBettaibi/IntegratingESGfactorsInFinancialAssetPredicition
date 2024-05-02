import string
import re
import spacy

class SentenceExtractor:
    def __init__(self):
        # Load the spaCy language model in the constructor
        self.nlp = spacy.load("en_core_web_sm")

    def remove_non_ascii(self, text):
        """Remove non-ASCII characters from the text."""
        printable = set(string.printable)
        return ''.join(filter(lambda x: x in printable, text))

    def extract_sentences(self, text):
        """
        Clean the input text and extract sentences using spaCy,
        suitable for further analysis or data processing.
        """
        pages = text.split('##PAGE_BREAK##')
        sentences = []  # Store all sentences here
    
        for page in pages:
            # Remove non-ASCII characters
            cleaned_text = self.remove_non_ascii(page)
    
            # Skip pages with too few words
            if len(cleaned_text.split()) < 300:
                continue
    
            # Process each line in the page
            for line in cleaned_text.split('\n\n'):
                line = re.sub(r'\s+', ' ', line)  # Normalize whitespace
                line = re.sub(r'[^\x00-\x7F]+', ' ', line)  # Remove non-ASCII again after manipulation
    
                # Use spaCy to segment the cleaned text into sentences
                doc = self.nlp(line)
                for sent in doc.sents:
                    clean_sentence = sent.text.strip()
                    if 10 < len(clean_sentence.split()) < 100:  # Sentence length constraints
                        sentences.append(clean_sentence)
    
        return sentences
