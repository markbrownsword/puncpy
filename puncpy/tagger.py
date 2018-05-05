from nltk import word_tokenize
from nltk import pos_tag


class Tagger():
    def __init__(self, text):
        self.text = text

    def tag_text(self):
        # TODO: Validate self.text is single sentence

        tokens = word_tokenize(self.text)
        return pos_tag(tokens)
