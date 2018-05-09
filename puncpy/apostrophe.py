from puncpy.model import ApostropheItem, ApostropheItemCollection
from puncpy.tagger import Tagger


class Apostrophe:

    # Rules
    d1 = {
        "Apostrophe_Rule_1": ("NNN", "POS")
    }

    stop_words = []

    '''
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself',
    'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they',
    'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am',
    'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 
    'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
    'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there',
    'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
    'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
    'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn',
    'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
    '''

    def execute(self, sentence: str) -> ApostropheItemCollection:
        # Tokenize, Tag
        tagger = Tagger(self.stop_words)
        tagged_text = tagger.tag_text(sentence)

        # Match tokens
        # TODO: Add the token after apostrophe_token - so result is List of Tuple(3) [('NNS', 'POS', 'VRB')]
        apostrophe_pairs = self.__match_apostrophe_pairs(tagged_text)

        # TODO: Build response
        return [ApostropheItem("It's", "Apostrophe_Rule_1")]

    @staticmethod
    def __match_apostrophe_pairs(tagged_text):
        apostrophe_pairs = []
        apostrophe_token = "'s"

        for current_index, current_token in enumerate(tagged_text):
            if current_token[0] != apostrophe_token:
                continue

            for previous_index, previous_token in enumerate(tagged_text):
                if previous_index == current_index - 1:
                    apostrophe_pairs.append([previous_token, current_token])
                    break

        if len(apostrophe_pairs) == 0:
            raise ValueError('No apostrophes in text.')
        else:
            print(apostrophe_pairs)

        return apostrophe_pairs
