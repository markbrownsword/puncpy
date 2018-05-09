from nltk import word_tokenize
from nltk import pos_tag


class Tagger():
    def __init__(self, stop_words: list):
        self.stop_words = stop_words

    def tag_text(self, text: str):
        tokens = word_tokenize(text)

        if self.stop_words:
            tokens = [t for t in tokens if t.lower() not in self.stop_words]

        return pos_tag(tokens)
