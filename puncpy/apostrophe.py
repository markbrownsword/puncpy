from puncpy.model import ApostropheItem, ApostropheItemCollection
from puncpy.tagger import Tagger


class Apostrophe:
    # Rules
    d1 = {
        "Apostrophe_Rule_1": ("PRP", "VBZ", "VBG")
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
        # Tag
        tagger = Tagger(self.stop_words)
        tagged_text = tagger.tag_text(sentence)

        # Match
        apostrophe_pairs = self.__match_apostrophe_pairs(tagged_text)
        if not apostrophe_pairs:
            raise ValueError('No apostrophes in text.')

        # Validate
        for (item1, item2, item3) in apostrophe_pairs:
            # TODO - add item to ApostropheItem
            item1_pos1 = item1[1] # TODO: Use Ternary to guard against None
            item2_pos2 = item2[1] # TODO: Use Ternary to guard against None
            item3_pos3 = item3[1] # TODO: Use Ternary to guard against None
            for key, (pos1, pos2, pos3) in self.d1.items():
                if item1_pos1 == pos1 and item2_pos2 == pos2 and item3_pos3 == pos3:
                    # TODO - add matched rule to ApostropheItem
                    print("????")

            # TODO - add ApostropheItem to ApostropheItemCollection

        return [ApostropheItem("It's", "Apostrophe_Rule_1")]

    @staticmethod
    def __match_apostrophe_pairs(tagged_text):
        apostrophe_pairs = []
        apostrophe_token = "'s"

        for current_index, current_token in enumerate(tagged_text):
            if current_token[0] != apostrophe_token:
                continue

            current = current_token
            previous = None
            after = None

            # Find token before apostrophe_token
            for previous_index, previous_token in enumerate(tagged_text):
                if previous_index == current_index - 1:
                    previous = previous_token
                    break

            # Find token after apostrophe_token
            for after_index, after_token in enumerate(tagged_text):
                if after_index == current_index + 1:
                    after = after_token
                    break

            apostrophe_pairs.append([previous, current, after])

        return apostrophe_pairs
