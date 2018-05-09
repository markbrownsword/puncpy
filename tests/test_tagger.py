import unittest.mock
from puncpy.tagger import Tagger


class TaggerTestCase(unittest.TestCase):
    # Tests for `tagger.py`

    @unittest.mock.patch('puncpy.tagger.word_tokenize', return_value=['This', 'is', 'my', 'own', 'invention'])
    @unittest.mock.patch('puncpy.tagger.pos_tag', return_value=[('This', 'DT'), ('is', 'VBZ'), ('my', 'PRP$'), ('own', 'JJ'), ('invention', 'NN')])
    def test_tag_text(self, pos_tag_mock, word_tokenize_mock):
        # Arrange
        stop_words = ['is']
        tagger = Tagger(stop_words)

        # Act
        result = tagger.tag_text('This is my own invention')

        # Assert nltk.word_tokenize received correct input
        args, kwargs = word_tokenize_mock.call_args_list[0]
        assert args == ('This is my own invention',)

        # Assert nltk.pos_tag received correct input ('is' should be removed by stop_words)
        args, kwargs = pos_tag_mock.call_args_list[0]
        assert args == (['This', 'my', 'own', 'invention'],)

        # Assert tag_text output
        self.assertTrue(len(result) == 5)

